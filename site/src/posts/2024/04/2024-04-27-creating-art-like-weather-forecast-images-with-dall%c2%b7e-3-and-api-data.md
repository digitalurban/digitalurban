---
title: "Creating Art Like Weather Forecast Images with DALL·E 3 and API Data"
date: 2024-04-27 14:12:43
slug: "creating-art-like-weather-forecast-images-with-dall%c2%b7e-3-and-api-data"
permalink: "/blog/2024/04/27/creating-art-like-weather-forecast-images-with-dall%c2%b7e-3-and-api-data/"
author: "Andy"
categories: ["Art", "Making", "Weather"]
tags: ["AI", "API", "Dall-E", "FrameTV", "MetOffice", "Python", "Weather"]
excerpt: "Introduction The Met Office, as the national meteorological service for the United Kingdom, provides valuable weather data through its API called DataPoint. This API caters to a wide range of users,…"
hero: "/assets/uploads/2023/12/image.jpeg_20231216122052.jpeg"
---

<h2>Introduction</h2>
The Met Office, as the national meteorological service for the United Kingdom, provides valuable weather data through its API called DataPoint. This API caters to a wide range of users, including professionals, scientists, students, and amateur developers. One of its notable features is the availability of text-based regional weather forecasts.

However, traditional text-to-image systems often struggle with accurately representing descriptive language. Users often find themselves navigating the complexities of prompt engineering to achieve their desired visual output. However, things are rapidly chaning with the use of AI and OpenAI’s latest release, DALL·E 3, simplifies this process by generating images that align with the provided text.

In this blog post, we’ll explore how to combine Met Office weather forecasts with DALL·E 3 via its API using Python. Our goal? To create captivating landscape imagery that reflects the weather conditions described in the forecast. Our images are then uploaded to our webserver, using FTP for viewing online. If you simply want to create an image, then you can leave the FTP section out.
<h2>The Workflow</h2>
<ol>
 	<li><strong>Met Office Data Retrieval</strong>:
<ul>
 	<li>We fetch the weather forecast data from the Met Office DataPoint API. Specifically, we focus on today’s weather conditions. We are using the UK metoffice, but it could be any weather api, from any country, that returns forecast text.</li>
</ul>
</li>
 	<li><strong>Creating the Image Prompt</strong>:
<ul>
 	<li>We construct an image prompt that encapsulates the essence of the weather. Our prompt includes the landscape type (e.g., “rural Norfolk landscape”) and the specific weather details obtained from the Met Office. The landscape type can be edited accordingly</li>
</ul>
</li>
 	<li><strong>DALL·E 3 Image Generation</strong>:
<ul>
 	<li>Leveraging OpenAI’s DALL·E 3 model, we generate an image based on the provided prompt. The image should realistically depict cloud formations, sunlight, precipitation, and wind effects, all while capturing the mood suggested by the weather.</li>
</ul>
</li>
 	<li><strong>FTP Upload</strong>:
<ul>
 	<li>Finally, we upload the generated image to an FTP server for public access.</li>
</ul>
</li>
</ol>
We run the script every 12 hours (ours runs on a Raspberry Pi) with the images archived on the websever - the gallery below shows some of the images from the last few months:The full code can be seen below, with the latest version available via our GitHub repository.
<pre class="EnlighterJSRAW" data-enlighter-language="generic"># Import necessary libraries
import ftplib
import requests
from PIL import Image
import io
from bs4 import BeautifulSoup
from datetime import datetime

# Get Met Office Data and Strip Today/Tonight Text
url = 'http://datapoint.metoffice.gov.uk/public/data/txt/wxfcs/regionalforecast/xml/512?key=YOURMETOFFICEAPIKEY'
document = requests.get(url)
soup = BeautifulSoup(document.content, "lxml-xml")

# Extract today's weather forecast
todayraw = soup.find_all("Paragraph", attrs={'title': 'Today:'})
todaystr = str(todayraw)
today = (todaystr.replace('[&lt;Paragraph title="Today:"&gt;', '').replace('&lt;/Paragraph&gt;', '').replace(']', ''))

# Set up OpenAI API key
from openai import OpenAI
client = OpenAI(api_key='YourOpenAIAPIKey')

# FTP server details
ftp_server = 'YourFTPServer'
ftp_username = 'FTPUserName'
ftp_password = 'FTPPassword'

# Specify the type of Norfolk landscape (e.g., rural, coastal, urban)
landscape_type = "rural Norfolk landscape"  # Change this as per your preference

# Create the image prompt
image_prompt = (
    f"A photorealistic single, cohesive scene image of a {landscape_type}, showcasing the following weather conditions: {today}. "
    "The image should realistically depict elements like cloud formations, sunlight or lack thereof, any precipitation, and wind effects. "
    "It should convey the atmosphere and mood suggested by the weather, with appropriate lighting and color tones. No numerical data or text should be included, just a pure visual representation of the weather in the landscape."
)

# Generate an image using OpenAI's DALL·E
def generate_image(prompt):
    response = client.images.generate(prompt=prompt, n=1, model="dall-e-3", quality="standard", style="vivid", size="1792x1024")
    image_url = response.data[0].url
    return image_url

# Function to generate a datestamp
def get_datestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")

# Modified FTP upload function
def upload_to_ftp(image_url, remote_path):
    with ftplib.FTP(ftp_server) as ftp:
        ftp.login(user=ftp_username, passwd=ftp_password)
        response = requests.get(image_url)
        image = Image.open(io.BytesIO(response.content))
        datestamp = get_datestamp()
        original_image = io.BytesIO()
        image.save(original_image, format='JPEG')
        original_image.seek(0)
        ftp.storbinary(f'STOR {remote_path}_{datestamp}.jpeg', original_image)
        resized_image = image.resize((1792, 1024))
        jpeg_image = io.BytesIO()
        resized_image.save(jpeg_image, format='JPEG')
        jpeg_image.seek(0)
        ftp.storbinary('STOR public_html/image.jpeg', jpeg_image)
        resized_image = image.resize((800, 480))
        jpeg_image = io.BytesIO()
        resized_image.save(jpeg_image, format='JPEG')
        jpeg_image.seek(0)
        ftp.storbinary('STOR public_html/image_eink.jpeg', jpeg_image)

# Generate the image and upload it
image_url = generate_image(image_prompt)
upload_to_ftp(image_url, 'public_html/image.jpeg')
</pre>

<h3>Breaking down the steps in the code -</h3>
<ol>
 	<li><strong>Importing Libraries</strong>: We start by importing necessary Python libraries for HTTP requests, image processing, FTP interaction, and data parsing.</li>
 	<li><strong>Fetching Weather Data</strong>: The script retrieves weather data from the Met Office using an API key. It extracts relevant information using BeautifulSoup and cleans up the output to get the weather forecast for today.</li>
 	<li><strong>OpenAI API Key</strong>: The OpenAI API key is set up to use the DALL·E model for image generation.</li>
 	<li><strong>FTP Server Details</strong>: FTP server credentials (server address, username, and password) are provided for image uploads.</li>
 	<li><strong>Weather Details and Landscape Type</strong>: The weather description obtained earlier is stored in weather_details . A landscape type (e.g., “rural Norfolk landscape”) is specified.</li>
 	<li><strong>Image Prompt Creation</strong>: The image_prompt  is constructed by combining weather details and landscape type. It describes the desired image.</li>
 	<li><strong>Image Generation with DALL·E</strong>: The  generatrate_image function uses DALL·E to create and return an image based on the prompt.</li>
 	<li><strong>Datestamp Generation</strong>: A datestamp is generated for archiving purposes.</li>
 	<li><strong>FTP Image Upload</strong>: The upload_to_ftp function connects to the FTP server, downloads the generated image, and uploads it to specific directories - this is optional, only of use if you are hosting your images.</li>
 	<li><strong>Running the Script</strong>: We run the script every 12 hours, using a cron job on a Raspberry Pi. We additional send it to our iPhone and our FrameTV, so the latest image is viewable either as a widget or on screen</li>
</ol>
Finally we also display it on our iPad, using the <a href="https://frame-it.framer.website/">FrameIT app</a> - this auto updates the image when a new one is uploaded to the web server.

&nbsp;

<figure><img class="wp-image-7782 size-large" src="/assets/uploads/2024/04/Photoroom_20240326_132608-e1714226219256-1024x732.jpg" alt="Dall-E 3 image on an iPad using Frame-IT" width="1024" height="732" /><figcaption>Dall-E 3 image on an iPad using Frame-IT</figcaption></figure>

Do let us know if you create you own AI based weather images using data inputs - it would be interesting to see how different landscapes and counties compare.
