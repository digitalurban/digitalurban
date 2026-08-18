---
title: "Ships Lamp Wind Speed Gauge"
date: 2025-11-12 11:39:29
slug: "ships-lamp-wind-speed-gauge"
permalink: "/blog/2025/11/12/ships-lamp-wind-speed-gauge/"
author: "Andy"
categories: ["Making"]
tags: ["Data", "iot", "micropytho", "physical objects"]
excerpt: "Our MicroPython project turns a strip of NeoPixel LEDs into a “ship's lamp\" style wind speed gauge. It connects to an MQTT broker to receive real-time wind speed data and translates it into a…"
hero: "/assets/uploads/2025/11/shipslamp2025.jpeg"
---

Our MicroPython project turns a strip of NeoPixel LEDs into a “ship's lamp" style wind speed gauge. It connects to an MQTT broker to receive real-time wind speed data and translates it into a flickering, color-coded light.

The light simulates an oil lamp by staying "steady" for a random period and then "flickering" for a short time by rapidly dimming and brightening - the flicker speed changes acording to the wind speed. The full code and details are available on <a href="https://github.com/ucl-casa-ce/Open-Gauges">Github as part of the ever growing Open Gauges Project</a>.

<figure><img class="wp-image-170079120 size-large" src="/assets/uploads/2025/11/shipslamp2025-1024x768.jpeg" alt="Ships Lamp" width="1024" height="768" /><figcaption>Ships Lamp</figcaption></figure>
<h2>Features</h2>
<ul>
 	<li><strong>Real-time Data:</strong> Connects to an MQTT broker to subscribe to a wind speed topic.</li>
 	<li><strong>Weather Map Gradient:</strong> Displays wind speed using an intuitive "weather map" color gradient:
<ul>
 	<li><strong>0 mph:</strong> Off (Black)</li>
 	<li><strong>1-10 mph:</strong> Solid Green</li>
 	<li><strong>10-20 mph:</strong> Fades from Green → Yellow</li>
 	<li><strong>20-30 mph:</strong> Fades from Yellow → Orange</li>
 	<li><strong>30-40 mph:</strong> Fades from Orange → Red</li>
 	<li><strong>40+ mph:</strong> Solid Red</li>
</ul>
</li>
 	<li><strong>Realistic Flicker Effect:</strong> The light doesn't just stay solid; it cycles between a "steady" phase (10-60s) and a "flicker" phase (5-15s) to simulate a real lamp.</li>
 	<li><strong>Asynchronous &amp; Resilient:</strong> Built using <code>uasyncio</code> and <code>mqtt_as</code>. The <code>mqtt_as</code> library automatically handles and recovers from WiFi or MQTT broker disconnections, re-subscribing to topics as needed.</li>
 	<li><strong>Hardware Watchdog:</strong> Uses the Pico's built-in <code>machine.WDT</code> (Watchdog Timer) to automatically reboot the device <em>only</em> if the main code loop freezes, ensuring high reliability. (This replaces the old 60-minute timer).</li>
 	<li><strong>Status LEDs:</strong> Provides a heartbeat flash on one LED and a WiFi status indicator on another.</li>
</ul>
<h2>Hardware Requirements<strong style="font-size: 16px;"><img style="font-weight: 400;" src="https://github.com/ucl-casa-ce/Open-Gauges/raw/main/Contributed/ShipsLamp/shipslamp.jpeg" alt="MQTT Ships Lamp" /></strong></h2>
<ul>
 	<li><strong>Raspberry Pi Pico W:</strong> (or any Pico with a WiFi-capable board).</li>
 	<li><strong>NeoPixel LED Strip:</strong> The code is configured for a strip, but can be any WS812B/NeoPixel compatible LEDs.</li>
 	<li><strong>Power Supply:</strong> A sufficient power supply for your LED strip (a strip of 60 LEDs can draw several amps at full brightness).</li>
 	<li><strong>A Ships Lamp (old or new).</strong></li>
</ul>
<h3>Default Pinout (Pico W)</h3>
<ul>
 	<li><strong>NeoPixel Data:</strong> <code>GP15</code></li>
 	<li><strong>Blue LED (Heartbeat):</strong> <code>blue_led</code> (defined in <code>config.py</code>, often the onboard LED).</li>
 	<li><strong>WiFi LED:</strong> <code>wifi_led</code> (defined in <code>config.py</code>).</li>
</ul>
<h2>Software &amp; Dependencies</h2>
This project relies on a few key MicroPython libraries that you must have on your Pico:
<ol>
 	<li><strong><code>neopixel.py</code>:</strong> The standard Adafruit NeoPixel library for MicroPython.</li>
 	<li><strong><code>mqtt_as.py</code>:</strong> A robust, asynchronous MQTT client. You can find it <a href="https://github.com/peterhinch/micropython-mqtt/blob/master/mqtt_as/mqtt_as.py" target="_blank" rel="noopener noreferrer">here</a>.</li>
 	<li><strong><code>config.py</code>:</strong> A file you must create to hold your credentials and pin definitions.</li>
</ol>
<h2>Configuration</h2>
You <strong>must</strong> create a <code>config.py</code> file in the root of your Pico's filesystem. This file should contain:
<ol>
 	<li>Your WiFi and MQTT broker credentials.</li>
 	<li>Definitions for your <code>wifi_led</code> and <code>blue_led</code>.</li>
</ol>
The <code>mqtt_as</code> library expects the <code>config.py</code> to contain a <code>config</code> dictionary.

<strong>Example <code>config.py</code>:</strong>
<pre class="wp-block-code"><code># config.py
from machine import Pin

# --- WiFi Configuration ---
config['wifi_led'] = Pin("WL_GPIO0", Pin.OUT) # Onboard LED on Pico W
config['ssid'] = 'YOUR_WIFI_SSID'
config['wifi_pw'] = 'YOUR_WWIFI_PASSWORD'

# --- MQTT Configuration ---
# This example is for the open broker mqtt.cetools.org
config['server'] = 'mqtt.cetools.org'
config['port'] = 1884
config['client_id'] = 'pico_ships_lamp' # Or any unique ID

# --- Optional: For Secured Brokers ---
# If your broker requires a username and password, add these lines:
# config['user'] = 'YOUR_MQTT_USER'
# config['password'] = 'YOUR_MQTT_PASSWORD'

# --- Other Hardware ---
# This is for the heartbeat LED
blue_led = Pin(10, Pin.OUT) # Example: an external LED on GP10
</code></pre>
<h2>Running the Project</h2>
<ol>
 	<li>Upload <code>main.py</code>, <code>neopixel.py</code>, <code>mqtt_as.py</code>, and your <code>config.py</code> to your Raspberry Pi Pico.</li>
 	<li>Reset the device.</li>
 	<li>The device will automatically connect to your WiFi and MQTT broker.</li>
 	<li>It will subscribe to the topic <code>personal/ucfnaps/downhamweather/windSpeed_mph</code>.</li>
 	<li>As messages are published to that topic, the ship's lamp will spring to life!</li>
</ol>
<h2>Customizing</h2>
<ul>
 	<li><strong>LED Count:</strong> Change the <code>numpix</code> variable at the top of <code>main.py</code> to match your strip.</li>
 	<li><strong>Data Pin:</strong> Change the <code>15</code> in <code>pixels = Neopixel(numpix, 0, 15, "GRB")</code> to match your data pin.</li>
 	<li><strong>MQTT Topic:</strong> Change the a topic name in the <code>conn_han</code> function to subscribe to your own data source.</li>
</ul>
