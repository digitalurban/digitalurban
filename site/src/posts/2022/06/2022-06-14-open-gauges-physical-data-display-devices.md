---
title: "Open Gauges - Physical and Digital Data Display Devices"
date: 2022-06-14 17:49:06
slug: "open-gauges-physical-data-display-devices"
permalink: "/blog/2022/06/14/open-gauges-physical-data-display-devices/"
author: "Andy"
categories: ["Data Visualisation", "Github", "Physical Data Devices"]
tags: ["Data Dial", "Dials", "iot", "Open Gauges", "Physical Data Devices"]
excerpt: "Developed at the Connected Environments Lab at The Centre for Advanced Spatial Analysis , University College London , the Open Gauges Project was launched in October 2021 as part of the Module on…"
hero: "/assets/uploads/2022/06/5DialsFrontsm-1.webp"
---

<p>Developed at the <a href="https://connected-environments.org/" rel="nofollow">Connected Environments Lab</a> at <a href="https://www.ucl.ac.uk/bartlett/casa" rel="nofollow">The Centre for Advanced Spatial Analysis</a>, <a href="https://www.ucl.ac.uk/" rel="nofollow">University College London</a>, the Open Gauges Project was launched in October 2021 as part of the Module on Sensor Data Visualisation (CASA0019) within the <a href="https://www.ucl.ac.uk/bartlett/casa/study/msc-connected-environments">MSc in Connected Environments</a>.</p>

<p>The <a href="https://github.com/ucl-casa-ce/Open-Gauges">Open Gauges Github Repository</a> provides full access to the original Fusion 360 design files, .STL files to 3D print gauges, code and graphics for the gauge dials. It also allows new gauges/code to be uploaded into new branches via the Gibhub page.<br />
<blockquote>The project aims to allow open-source data gauges to be built, modified, and viewed as both physical (3d printed) and digital gauges.</blockquote><br />
Depending on the user’s preference the models can be made to run from any online data source  - such as an MQTT feed - from Weather Data with Air Pressure, Temperature, Wind Speed etc though to Air Quality Gauges, Noise Meters, Energy etc. The project was created by <a href="https://connected-environments.org/people/" rel="nofollow">Professor Andrew Hudson-Smith</a> and <a href="https://connected-environments.org/people/" rel="nofollow">Dr Valerio Signorelli</a>.</p>

<p>A total of 5 Dial Graphics are provided in this initial release - sized to fit into the 3D printed cases.</p>

<p>The 5 Dial Graphics are - Temperature (-10 to 40 oC), Wind Speed (0-60 mph), Wind Dir (0 - 360), Air Pressure (950 - 1050 mb) and Co2 (400 - 1400 ppm).</p>

<p>In addition to reading the MQTT data and using the Servo Easing Library for the servo, the code also includes a time function, allowing the gauge to turn the LED lights/Servo on and off at set times. This is used to turn off at night and on again in the morning.</p>

<p>The code can be used to create any gauge with a range from 180 to 360 degrees using a standard SG90 servo. A gear train is used to extend the servo range with the ability to calibrate in the code. On load, the servo performs a sweep function, to aid the calibration process.</p>

<p>JTNDY2VudGVyJTNFJTNDZGl2JTIwc3R5bGUlM0QlMjJhbGlnbiUzQSUyMGNlbnRlciUyMiUzRSUyMCUzQ2lmcmFtZSUyMHRpdGxlJTNEJTIyT3BlbiUyMEdhdWdlcyUyMC0lMjBXaW5kJTIwU3BlZWQlMjBHYXVnZSUyMHdpdGglMjBTdGFuZCUyMiUyMGZyYW1lYm9yZGVyJTNEJTIyMCUyMiUyMGFsbG93ZnVsbHNjcmVlbiUyMG1vemFsbG93ZnVsbHNjcmVlbiUzRCUyMnRydWUlMjIlMjB3ZWJraXRhbGxvd2Z1bGxzY3JlZW4lM0QlMjJ0cnVlJTIyJTIwYWxsb3clM0QlMjJhdXRvcGxheSUzQiUyMGZ1bGxzY3JlZW4lM0IlMjB4ci1zcGF0aWFsLXRyYWNraW5nJTIyJTIweHItc3BhdGlhbC10cmFja2luZyUyMGV4ZWN1dGlvbi13aGlsZS1vdXQtb2Ytdmlld3BvcnQlMjBleGVjdXRpb24td2hpbGUtbm90LXJlbmRlcmVkJTIwd2ViLXNoYXJlJTIwd2lkdGglM0QlMjI2NDAlMjIlMjBoZWlnaHQlM0QlMjI0ODAlMjIlMjBzcmMlM0QlMjJodHRwcyUzQSUyRiUyRnNrZXRjaGZhYi5jb20lMkZtb2RlbHMlMkZhMTgxYjZmMjZjYTc0ZWExOGFkMjYwNjk4ZjVjNmVlYiUyRmVtYmVkJTNGYXV0b3N0YXJ0JTNEMSUyNnRyYW5zcGFyZW50JTNEMSUyMiUzRSUzQyUyRmlmcmFtZSUzRSUzQyUyRmRpdiUzRSUzQyUyRmNlbnRlciUzRQ==The aim was to make displaying data, via both a physical and digital device, as easy as possible - to recreate the simplicity of a gauge but to update it to use current data standards.</p>

<p><img class="wp-image-6210 alignright" src="/assets/uploads/external/connected-environments.org/wp-content/uploads/2021/10/techdraw3-1024x724.png" alt="Open Gauges - Technical Drawing" width="411" height="290" /></p>

<p>Due to its simplicity, the design can be edited to accommodate a range of styles, from dual displays through to retrofitting old devices. Indeed retrofitting (<em>only if a device is beyond repair of course</em>) can give new life to old barometers, barographs, pressure gauges etc, all with the same code and design.</p>

<p>At the present time (October 22nd, 2021) this page is under development with new designs, a full walkthrough of how to make one, an Augmented Reality Version and new examples (such as Air Quality) incoming.<br />
<blockquote>To underline the developing nature of the project - see our <a href="https://connected-environments.org/open-gauges/neopixel-barometer/">Neopixel Barometer Open Gauge,</a> included 28th October 2021, the <a href="https://github.com/ucl-casa-ce/Open-Gauges/blob/main/Graphics%20Files/Energy_Gauge.png">Open Energy Gauge graphic</a>, included 9th November 2021 and the <a href="https://connected-environments.org/making/open-gauges-the-voltmeter-gauge/">Voltmeter Gauge</a>, added 11th November 2021 over at the Connected Environments site and the<a href="https://www.digitalurban.org/blog/2022/05/31/owmbarometer/"> Open Weather Map NeoPixel Barometer</a>, here on Digital Urban (June, 2022).</blockquote><br />
The gauges are made to be as simple as possible to make but allow enough flexibility to allow them to be used to display a wide range of data types, the parts list below provides details for the full gauge, with lighting.<br />
<h2><a id="user-content-parts-list" class="anchor" href="https://github.com/ucl-casa-ce/Open-Gauges/blob/main/README.md#parts-list" aria-hidden="true"></a>Parts List</h2><br />
The main parts are:<br />
<ul><br />
 	<li>Node MCU Arduino Board - we have been using the (<a href="https://www.amazon.co.uk/MakerHawk-Internet-Development-Wireless-Micropython/dp/B07M8Q38LK/ref=sr_1_4?dchild=1&amp;keywords=nodemcu&amp;qid=1634650644&amp;sr=8-4" rel="nofollow">MakerHawk boards</a>). However, any Arduino compatiable board will suffice, the ease of using the above boards is the code will work without and changes to the pins.</li><br />
 	<li>SG90 Servo - any SG90 style servo will work, we would however recommend the MG90S Micro Servo as it provides a smoother travel to the gauage pointer.</li><br />
 	<li>Lights - <a href="https://shop.pimoroni.com/products/white-led-backlight-module?variant=36999548170" rel="nofollow">Pimorini White LED Backlight Module – 38.7mm x 11.9mm x 2mm</a>, although any low power led will also suffice</li><br />
 	<li>PLA for 3D Printing - Any PLA for the main parts, the dials graphics are printed on paper and laid flat on a disc (see 3D Printer Files) printed in transparent PLA. This can be left out but it allows the dial to lay flat and provides a nice diffused light. eSun Transparent PLA works well.</li><br />
</ul><br />
<h2></h2></p>

<p><!-- /wp:paragraph --></p>
