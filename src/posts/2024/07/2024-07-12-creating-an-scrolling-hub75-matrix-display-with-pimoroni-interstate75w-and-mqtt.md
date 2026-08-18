---
title: "Make a Scrolling Hub75 Matrix Display using a Pimoroni Interstate75W and MQTT"
date: 2024-07-12 09:30:06
slug: "creating-an-scrolling-hub75-matrix-display-with-pimoroni-interstate75w-and-mqtt"
permalink: "/blog/2024/07/12/creating-an-scrolling-hub75-matrix-display-with-pimoroni-interstate75w-and-mqtt/"
author: "Andy"
categories: ["Making", "Posts"]
tags: ["Data", "home assistant", "iot", "making", "MQTT Scroller"]
excerpt: "There are many tutorials online on using an LED Matrix to display data—many of them require wiring up a screen, external power supplies, or flashing boards. We wanted to highlight a slightly more…"
hero: "/assets/uploads/2024/07/interstate-75-w-2_1500x1500_crop_center-300x300.webp"
---

There are many tutorials online on using an LED Matrix to display data—many of them require wiring up a screen, external power supplies, or flashing boards. We wanted to highlight a slightly more accessible way to get an LED Matrix—in our case, a Hub 75, 32x64 pixel up and running using an <a href="https://shop.pimoroni.com/products/interstate-75-w?variant=40453881299027">Interstate75W from Pimoroni.</a> The benefit of the Interstate is that it plugs indirectly into the matrix and can power a single screen directly from the board.

<figure><img class="size-medium wp-image-7838" src="/assets/uploads/2024/07/interstate-75-w-2_1500x1500_crop_center-300x300.webp" alt="Interstate75W " width="300" height="300" /><figcaption>Interstate75W</figcaption></figure>

We wanted a way to display any data we wanted on the screen with the screen lighting up and data scrolling up as it arrives and then turning off. To use this we use MQTT to load our data (a test feed is included in the scripts - which displays Time, News and Environmental Information) - see below for a demo:

&nbsp;
<div style="text-align: center;"><iframe src="https://www.youtube.com/embed/kG3OStmfXLk" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe></div>
We also incorporate manual brightness control and reconnecting for the MQTT for message handling, making it easy to update the display from anywhere. Setting up your own MQTT is beyond this post, but its easier than you may think and once you have one it can be used to display any data, from external feeds such as weather apis through to data from systems such as Home Assistant. Edit April 2025, we have added additional files to allow use with the new <a href="https://shop.pimoroni.com/products/interstate-75-w?variant=55006518411643">Pimoroni Intersate Starter Kit 128x128 Matrix</a>, allowing a larger format screen, as pictured below.

<figure><img class="wp-image-7914 size-large" src="/assets/uploads/2024/07/Matrix128x128-1024x576.jpeg" alt="Matrix128x128" width="1024" height="576" /><figcaption>Matrix128x128</figcaption></figure>
<h3>Features</h3>
<ul>
 	<li><strong>Scrolling Text Messages:</strong> Display messages that scroll across the HUB75 LED matrix.</li>
 	<li><strong>Manual Brightness Control:</strong> Adjust the brightness of the display manually.</li>
 	<li><strong>MQTT Integration:</strong> Receive and display messages via MQTT.</li>
</ul>
<h3>Hardware Requirements</h3>
To get started, you'll need the following hardware:
<ul>
 	<li><a href="https://shop.pimoroni.com/products/interstate-75-w?variant=40453881299027">Pimoroni Interstate75W</a></li>
 	<li><a href="https://shop.pimoroni.com/products/rgb-led-matrix-panel?variant=42312764298">A HUB75 LED matrix display</a></li>
 	<li><a href="https://www.printables.com/model/939763-hub75-display-case-for-the-interstate75w-32x64-4mm">3D Printed Case</a></li>
 	<li>MQTT broker (local or cloud-based) - we provide our own feed so you can test the set up.</li>
</ul>
There is also room in the 3D printed case to attach a cloth cover, acting a diffuser (a grey t-shirt works well, cut to size):

<figure><img class="wp-image-7879 size-large" src="/assets/uploads/2024/07/Photoroom_20250128_104636-1024x576.png" alt="LED Matrix with Cloth Cover" width="1024" height="576" /><figcaption>LED Matrix with Cloth Cover</figcaption></figure>
<h2>Software Requirements</h2>
You'll also need the following software - all available from our GitHub
<ul>
 	<li>MicroPython</li>
 	<li>Required MicroPython libraries:
<ul>
 	<li><code>interstate75</code></li>
 	<li><code>mqtt_as</code></li>
 	<li><code>uasyncio</code></li>
</ul>
</li>
</ul>
<h3>Setup</h3>
<h3>1. Clone the Repository</h3>
First, clone the project repository from GitHub, or just download the files directly:

"`sh
git clone <a href="https://github.com/digitalurban/Interstate75W_MQTT_Scroller">https://github.com/digitalurban/Interstate75W_MQTT_Scroller</a>
cd interstate75w-mqtt-display
"`
<h3>2. Upload the Code</h3>
Next, upload the code to your microcontroller. You can use tools like Thonny or ampy to do this.
<h3>3. Configure WiFi and MQTT</h3>
Update the <code>config.py</code> file with your WiFi credentials, the MQTT details can also be updated if you have your own server, if not then leave them for our demo feed.

"`python
config = {
'ssid': 'your_wifi_ssid',
'wifi_pw': 'your_wifi_password',
'server': 'mqtt_broker_address',
'user': 'mqtt_user',
'password': 'mqtt_password',
'port': 1883,
'keepalive': 60,
}
"`
<h3>Usage</h3>
<h3>Run the Script</h3>
The script will automatically connect to WiFi and the MQTT broker, then start displaying messages - our MQQ feed displays messages approximatly every 3 minutes.
<h3>Constants and Initial Setup</h3>
The script defines constants for controlling the scrolling text speed, how long the screen says on for after displaying the message and brightness settings. It also initializes the Interstate75W object:
<h4>Constants for controlling scrolling text</h4>
BACKGROUND_COLOUR = (0, 0, 0) # Black background to turn off the screen
HOLD_TIME = 2.0
BLANK_SCREEN_TIME = 10.0
BUFFER_PIXELS = 2 # Increased buffer to ensure full scroll off
SCROLL_SPEED_LEVEL = 8 # Set the desired scrolling speed level (1 to 10)
SCROLL_SPEED = 1 / SCROLL_SPEED_LEVEL # Convert to a delay in seconds
<h4>Brightness settings</h4>
brightness = 50 # Initial brightness (0 to 100)

Do let us know if you make one - we would love to see images of your own set up and we hope this made it a little easier for anyone new looking to run an LED matrix using MQTT.
