---
title: "Open Weather Map NeoPixel Barometer - Open Gauges"
date: 2022-05-31 12:53:33
slug: "owmbarometer"
permalink: "/blog/2022/05/31/owmbarometer/"
author: "Andy"
categories: ["Blog", "Making", "Open Gauges"]
tags: []
excerpt: "Open Weather Map Barometer The Open Gauges project aims to allow open-source data gauges to be built, modified, and viewed as both physical (3d printed) and digital gauges. Depending on the user’s…"
hero: "/assets/uploads/external/connected-environments.org/wp-content/uploads/2022/05/Owmbaroplain-79x1024.png"
---

<figure><img class="wp-image-6540 size-large" src="/assets/uploads/external/connected-environments.org/wp-content/uploads/2022/05/Owmbaroplain-79x1024.png" alt="Open Weather Map Barometer" width="79" height="1024" /><figcaption>Open Weather Map Barometer</figcaption></figure>

The <a href="https://connected-environments.org/portfolio/6172/">Open Gauges project</a> aims to allow open-source data gauges to be built, modified, and viewed as both physical (3d printed) and digital gauges. Depending on the user’s preference the models can be made to run from any online data source with a data feed - from Weather Data with Air Pressure, Temperature, Wind Speed etc though to Air Quality Gauges, Noise Meters, Energy etc.

Part of the initial release, from the <a href="https://connected-environments.org/people/">Connected Environments Team</a> at <a href="https://www.ucl.ac.uk/bartlett/casa">The Bartlett Centre for Advanced Spatial Analysis</a>, <a href="https://www.ucl.ac.uk/">University College London</a>, and alongside the more traditional 'dial style' gauges, is our new <em><strong>Neopixel Barometer, updated for Open Weather Map. </strong></em>Back in October we published the Weather Flow version, this new, open source version is specifically designed to use the free Open Weather Map API, making it easier to use.

Designed to be as simple as possible it is powered by a Raspberry Pi and uses the data feed from the Open Weather Map Single Call API, making it open to anyone with data available world world, according to your choice of location. So you could chose to display local Barometric Pressure or have a series of them on display showing locations around the world. Each gauges updates every 5 minutes with a Green Pixel to note successful data collection and Red for unsuccessful

Full code and files can be found in the <a href="https://github.com/ucl-casa-ce/Open-Gauges/tree/main/Contributed/OpenWeatherMapNeoPixelBarometer">Open Gauges Github Repository.</a>
<h3>Data Source</h3>
The barometer uses the One Call API from Open Weather Map, provided as JSON.
<h3><a id="user-content-data-displayed" class="anchor" href="https://github.com/ucl-casa-ce/Open-Gauges/tree/main/Contributed/NeoPixelBarometer#data-displayed" aria-hidden="true"></a>Data displayed</h3>
The Neopixel Barometer displays current sea level air pressure (Mb) and the current pressure trend - Rising, Steady, Falling.

The data updates every five minutes with a sweep of blue/yellow neopixels on power up. The pressure trend is calculated in the Python script, as its not part of the API. As such it takes 3 hours to calibrate - with 'Rising' shown initially and then changing to the current trend after 3 hours of data has been downloaded.
<h3><a id="user-content-3d-printed-model" class="anchor" href="https://github.com/ucl-casa-ce/Open-Gauges/tree/main/Contributed/NeoPixelBarometer#3d-printed-model" aria-hidden="true"></a>3D printed model</h3>
The main barometer markers - ie STORM, FAIR, CHANGE, as well as the numbers - 950, 960 etc are provided as separate .stl files to 3D print. This is to allow easy alignment with the Neopixel strip with the correct pixel.

The conditions come in a single section, again to be aligned once the Neopixel strip is mounted, the Trend titles are also provided. We also provide the end caps for the Acrylic Tube (optional, see below).
<h3><a id="user-content-wood" class="anchor" href="https://github.com/ucl-casa-ce/Open-Gauges/tree/main/Contributed/NeoPixelBarometer#wood" aria-hidden="true"></a>Wood</h3>
The Neopixel strip is can be mounted either onto a thin strip of wood approx 125 centimetres long by 4.5 cm wide using the fixings that come with the Neopixel Strip, or with a wider block. The Text/Numbers are 3D printed and glued on the wood. It is a standard wood strip that most DIY/Hardware stores stock. The use of wood/mounting is to allow flexibility - ie mount it however you like.
<blockquote>As an update to this post (June 22nd, 2022) we now include mounting 'Feet' for a table top horizontal display - as illustrated below, angled at 30 degrees to provide a clear viewing angle of the air pressue.</blockquote>

<h3><strong>Acrylic Tube</strong></h3>
For this updated version we adapted the model to allow the additional use of an 1m x 28mm Acrylic Tube, widely available it allows the LED strip to be mounted into the tube (we used a piece of conduit to straighten the led strip). This give the barometer a more 'finished look' and provides more of a nod towards the mercury barometers of old.
<h3><a id="user-content-hardware" class="anchor" href="https://github.com/ucl-casa-ce/Open-Gauges/tree/main/Contributed/NeoPixelBarometer#hardware" aria-hidden="true"></a>Hardware</h3>
The hardware has been selected to be as low cost as possible -
<ul>
 	<li>A Raspberry Pi - We used the Raspberry Pi Zero W</li>
 	<li>1 Meter 144 Addressable Neopixel Strip (NeoPixel/WS2812/SK6812 compatible) - <a href="https://thepihut.com/products/flexible-rgb-led-strip-neopixel-ws2812-sk6812-compatible-144-led-meter" rel="nofollow">Example here from The PiHut</a></li>
</ul>
JTNDZGl2JTIwY2xhc3MlM0QlMjJza2V0Y2hmYWItZW1iZWQtd3JhcHBlciUyMiUzRSUyMCUzQ2lmcmFtZSUyMHRpdGxlJTNEJTIyT3BlbiUyMFdlYXRoZXIlMjBNYXAlMjBOZW9waXhlbCUyMEJhcm9tZXRlciUyMiUyMGZyYW1lYm9yZGVyJTNEJTIyMCUyMiUyMGFsbG93ZnVsbHNjcmVlbiUyMG1vemFsbG93ZnVsbHNjcmVlbiUzRCUyMnRydWUlMjIlMjB3ZWJraXRhbGxvd2Z1bGxzY3JlZW4lM0QlMjJ0cnVlJTIyJTIwYWxsb3clM0QlMjJhdXRvcGxheSUzQiUyMGZ1bGxzY3JlZW4lM0IlMjB4ci1zcGF0aWFsLXRyYWNraW5nJTIyJTIweHItc3BhdGlhbC10cmFja2luZyUyMGV4ZWN1dGlvbi13aGlsZS1vdXQtb2Ytdmlld3BvcnQlMjBleGVjdXRpb24td2hpbGUtbm90LXJlbmRlcmVkJTIwd2ViLXNoYXJlJTIwd2lkdGglM0QlMjIxMjAwJTIyJTIwaGVpZ2h0JTNEJTIyNDgwJTIyJTIwc3JjJTNEJTIyaHR0cHMlM0ElMkYlMkZza2V0Y2hmYWIuY29tJTJGbW9kZWxzJTJGZTE4OWIwZTBkMzVmNGMwMDhlODY5MzZkMTUxNWM2MDAlMkZlbWJlZCUzRmF1dG9zdGFydCUzRDElMjZjYW1lcmElM0QwJTI2dHJhbnNwYXJlbnQlM0QxJTIyJTNFJTIwJTNDJTJGaWZyYW1lJTNFJTIwJTNDcCUyMHN0eWxlJTNEJTIyZm9udC1zaXplJTNBJTIwMTNweCUzQiUyMGZvbnQtd2VpZ2h0JTNBJTIwbm9ybWFsJTNCJTIwbWFyZ2luJTNBJTIwNXB4JTNCJTIwY29sb3IlM0ElMjAlMjM0QTRBNEElM0IlMjIlM0UlMjAlM0NhJTIwaHJlZiUzRCUyMmh0dHBzJTNBJTJGJTJGc2tldGNoZmFiLmNvbSUyRjNkLW1vZGVscyUyRm9wZW4td2VhdGhlci1tYXAtbmVvcGl4ZWwtYmFyb21ldGVyLWUxODliMGUwZDM1ZjRjMDA4ZTg2OTM2ZDE1MTVjNjAwJTNGdXRtX21lZGl1bSUzRGVtYmVkJTI2dXRtX2NhbXBhaWduJTNEc2hhcmUtcG9wdXAlMjZ1dG1fY29udGVudCUzRGUxODliMGUwZDM1ZjRjMDA4ZTg2OTM2ZDE1MTVjNjAwJTIyJTIwdGFyZ2V0JTNEJTIyX2JsYW5rJTIyJTIwc3R5bGUlM0QlMjJmb250LXdlaWdodCUzQSUyMGJvbGQlM0IlMjBjb2xvciUzQSUyMCUyMzFDQUFEOSUzQiUyMiUzRSUyME9wZW4lMjBXZWF0aGVyJTIwTWFwJTIwTmVvcGl4ZWwlMjBCYXJvbWV0ZXIlMjAlM0MlMkZhJTNFJTIwYnklMjAlM0NhJTIwaHJlZiUzRCUyMmh0dHBzJTNBJTJGJTJGc2tldGNoZmFiLmNvbSUyRmRpZ2l0YWx1cmJhbiUzRnV0bV9tZWRpdW0lM0RlbWJlZCUyNnV0bV9jYW1wYWlnbiUzRHNoYXJlLXBvcHVwJTI2dXRtX2NvbnRlbnQlM0RlMTg5YjBlMGQzNWY0YzAwOGU4NjkzNmQxNTE1YzYwMCUyMiUyMHRhcmdldCUzRCUyMl9ibGFuayUyMiUyMHN0eWxlJTNEJTIyZm9udC13ZWlnaHQlM0ElMjBib2xkJTNCJTIwY29sb3IlM0ElMjAlMjMxQ0FBRDklM0IlMjIlM0UlMjBkaWdpdGFsdXJiYW4lMjAlM0MlMkZhJTNFJTIwb24lMjAlM0NhJTIwaHJlZiUzRCUyMmh0dHBzJTNBJTJGJTJGc2tldGNoZmFiLmNvbSUzRnV0bV9tZWRpdW0lM0RlbWJlZCUyNnV0bV9jYW1wYWlnbiUzRHNoYXJlLXBvcHVwJTI2dXRtX2NvbnRlbnQlM0RlMTg5YjBlMGQzNWY0YzAwOGU4NjkzNmQxNTE1YzYwMCUyMiUyMHRhcmdldCUzRCUyMl9ibGFuayUyMiUyMHN0eWxlJTNEJTIyZm9udC13ZWlnaHQlM0ElMjBib2xkJTNCJTIwY29sb3IlM0ElMjAlMjMxQ0FBRDklM0IlMjIlM0VTa2V0Y2hmYWIlM0MlMkZhJTNFJTNDJTJGcCUzRSUzQyUyRmRpdiUzRQ==It is made to be mounted either vertically or horizontally - the 3D model above details the make (click and drag to examine the model/zoom in). The tabletop version with <a href="https://skfb.ly/ovCDN">30-degree angled legs can now be viewed directly on Sketchfab</a>.
<h3>Code and library</h3>
The full code/3d printing files etc are provided on the <a href="https://github.com/ucl-casa-ce/Open-Gauges/tree/main/Contributed/NeoPixelBarometer">Github page</a>, which also includes the other Open Gauges to 3D print and make.

<strong>Libraries used</strong>
<ul>
 	<li>requests</li>
 	<li>json</li>
 	<li>time</li>
 	<li>neopixel</li>
 	<li>board</li>
</ul>
<h2 dir="auto">Digital model</h2>
<p dir="auto">The model is also provided in Fusion 360 for any edits to wording, sizing etc (note the Pi is not included due to separate licensing).</p>
