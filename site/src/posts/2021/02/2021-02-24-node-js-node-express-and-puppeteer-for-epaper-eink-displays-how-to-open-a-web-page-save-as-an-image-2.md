---
title: "Node.JS, Node Express and Puppeteer for Epaper / EInk Displays: How to Open a Web Page & Save as an Image"
date: 2021-02-24 22:40:44
slug: "node-js-node-express-and-puppeteer-for-epaper-eink-displays-how-to-open-a-web-page-save-as-an-image-2"
permalink: "/blog/2021/02/24/node-js-node-express-and-puppeteer-for-epaper-eink-displays-how-to-open-a-web-page-save-as-an-image-2/"
author: "Andy"
categories: ["Posts"]
tags: ["eink", "epaper", "inkpate", "kindle", "node express", "node.js", "puppeteer"]
excerpt: "Sometimes there is a need to step back and do things as simply as possible. EInk / Epaper screens are amazing, they carrying on showing an image with zero power and the screens have a certain clarity…"
hero: "/assets/uploads/2021/02/Nighttimeside-scaled-1.jpg"
---

<p><!-- wp:paragraph {"dropCap":true} --></p>
<p class="has-drop-cap">Sometimes there is a need to step back and do things as simply as possible. EInk / Epaper screens are amazing, they carrying on showing an image with zero power and the screens have a certain clarity that is hard to achieve with more standard LED offerings. The more difficult part is getting content onto them, especially content that is well designed and fits the screen.</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:pullquote -->
<figure class="wp-block-pullquote">
<blockquote>
<p>Puppeteer can do many things but for our use it allows the Pi to open a webpage, take a screengrab, save it as an image and then close. This image can subsequently be served via Node Express and viewed on an eInk screen.</p>
</blockquote>
</figure>
<!-- /wp:pullquote -->
<p><!-- wp:paragraph -->To make the most of eInk/epaper screens you generally grab some information using a microcontroller, such as a Node MCU or ESP32, send it to the screen and then power down. This means you can check for new information over a period of time, say, every 15 minutes, display it and then sleep, allowing your screen to be battery powered for weeks on end.</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:media-text {"mediaId":5942,"mediaLink":"http://www.digitalurban.org/?attachment_id=5942","mediaType":"image"} -->
<div class="wp-block-media-text alignwide is-stacked-on-mobile">
<figure class="wp-block-media-text__media"><img class="wp-image-5942 size-full" src="/assets/uploads/2021/02/Nighttimeside-1024x867.jpg" alt="Inkplate 6 Case" /></figure>
<div class="wp-block-media-text__content">
<p><!-- wp:paragraph -->At the moment we are using the amazing <a href="https://inkplate.io/">InkPlate 6.</a> The InkPlate 6 is built around a recycled Kindle Screen and has a built-in ESP32 controller, a lithium battery connecter/charger and perhaps, more importantly, an easy to understand library to display an image and then sleep. In the world of eInk screens, the importance of an easy to understand library really cannot be understated, some of them are notably complex. We have published the <a href="https://www.thingiverse.com/thing:4729759">3D printable case to Thingiverse</a> so all you need is the InkPlate (or any other screen you want to display an image on), a script to load a webpage and some Node JS to grab the information you want to display.</p>
<!-- /wp:paragraph --></div>
</div>
<!-- /wp:media-text -->
<p>&nbsp;</p>
<!-- wp:media-text {"mediaPosition":"right","mediaId":5933,"mediaLink":"http://www.digitalurban.org/?attachment_id=5933","mediaType":"image"} -->
<div class="wp-block-media-text alignwide has-media-on-the-right is-stacked-on-mobile">
<figure class="wp-block-media-text__media"><img class="wp-image-5933 size-full" src="/assets/uploads/2021/02/IMG_2865-1024x768.jpg" alt="windy.com on an eink screen" /></figure>
<div class="wp-block-media-text__content">
<p><!-- wp:paragraph -->We are using 3 variations of the same script on our ePaper display, one to grab a webpage showing environmental information, a second decoding a weather forecast from the Met Office, another showing a Rainfall radar and we cycle these every 15 minutes with the environmental information showing twice in the hour.</p>
<!-- /wp:paragraph --></div>
</div>
<p><!-- /wp:media-text --><!-- /wp:media-text -->The information can of course be any web page you want to display, from a news site,  a social network feed, transport information or anything you want to show.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph --><strong>Ingredients</strong></p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:list {"ordered":true} -->
<ol>
<li>You will need a device capable of running Node JS, we are using a Raspberry Pi 4. We assume here that you have a Pi up and running with the full operating system installed, if not then take a look at the main<a href="https://www.raspberrypi.org/documentation/installation/installing-images/" target="_blank" rel="noreferrer noopener"> Pi site</a> for details on how to set up. If you need any help then drop us a line in the comments and we can expand this section as needs be.</li>
<li>Optional: An eInk screen and controller - we are using the <a href="https://inkplate.io/" target="_blank" rel="noreferrer noopener">InkPlate 6</a> and our code to load the image once grabbed is now <a href="https://github.com/digitalurban/InkPlate6WebImage">available on GitHub</a>. There are a number of eInk/epaper screens, the most popular ones being made by WaveShare. These will also work if you edit the example code from the libraries that allow the display of online images. Of course, you may simply want to have an automated screengrab of a webpage. Such things are useful in Unity3D to make Augmented Reality displays, for example.</li>
</ol>
<!-- /wp:list -->
<p><!-- wp:paragraph --><strong>Installing Node JS</strong></p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->The first part is to install Node.JS, thankfully Node is quick and easy to install - in your terminal enter:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>$ curl -sL https://deb.nodesource.com/setup_15.10.0 | sudo -E bash -</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->The 15.10.0 represent the current version as of February 2021, change this number to the latest version as needs be - you can find out the current release via the <a href="https://nodejs.org/en/download/current/" target="_blank" rel="noreferrer noopener">main Node JS site.</a> You have now made your Pi aware of where to find Node.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph --> The next step is to install it:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>sudo apt install nodejs</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->To check all is in place you can run:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>node -v</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->This will tell you the version of Node you are running. You have installed Node, well done, now for the Puppeteer library.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph --><strong>Installing and Configuring Puppeteer</strong></p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->Puppeteer is a library for Node.js that allows for the control of the Chrome browser in headerless mode (i.e. you dont see it happening). This allows you to open a web page, do something with it - in our case take a screenshot - and then close chrome, all via a simple script.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->Installing Puppeteer is all via a single line in the terminal:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>npm i puppeteer --save</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->Now you have Node.js and Puppeteer installed, all you need now is to create a script to tell Node what to do:</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->We like to start a new script in a new directory called 'Scripts' (although it can be anywhere).</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->So firstly create a new directory via the terminal:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>mkdir Scripts</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->Now create your first empty script, we are going to call ours 'webpage.js':</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>sudo nano webpage.js</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->Below is the javascript to cut and paste into your new script:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>const puppeteer = require('puppeteer');
async function timeout(ms) {
  return new Promise(resolve =&gt; setTimeout(resolve, ms));
}
(async () =&gt; {
let browser = await puppeteer.launch({
          headless: true,
          executablePath: '/usr/bin/chromium-browser',
//          args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.goto('http:YourWebPageURL');
// 5 second timeout: allows the page to fully render before taking the screenshot
  await timeout(5000);
  await page.setViewport({ width: 800, height: 600});
  await page.screenshot({path: '/home/pi/Scripts/eink.jpg'});
  await browser.close();
})();
</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->The main parts to note above are the http: where you need to add in the webpage you want to capture and the width and height of the page. This should be changed according to the resolution of your screen, the InkPlate 6 runs at 800x600 resolution. The script opens the URL, waits 5 seconds for it to fully load and then saves a screenshot as a jpg to the location of your choice.</p>
<p>To run your script:</p>
<p><code>node webpage.js</code><br /><!-- /wp:paragraph --></p>
<p>The script should now run, load a webpage and save the image to your Pi.</p>
<p><!-- wp:paragraph -->If you are running your eInk display direct from your Pi (such as using a Waveshare screen) you can stop here and point your display to the new image. If however, you are using a screen elsewhere on your network you will need to host it, this is where Node Express comes in.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph --><strong>Installing Node Express</strong></p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->As with Node and Puppeteer installing is via a simple one line command:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>npm install express --save</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->To start the server and host the image, you need another script. So the same as before, create a script, we called ours server.js:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>sudo nano server.js</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->Cut and paste the following:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>var express = require('express');
var app = express();
var path = require('path');
var public = path.join(__dirname, 'public');
// viewed at http://localhost:8080
app.get('/', function(req, res) {
    res.sendFile(path.join(public, 'index.html'));
});
app.use('/', express.static(public));
app.listen(8080);</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->The above script runs a server at http://localhost:8080 where you can install a welcome page (index.html) if you wish but more importantly you can serve static files, in our case our screen grab eink.jpg. Note that the folder address is 'public' this is where you will host your files.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->In our first script we now want to edit the folder where our image is saved, so we can host it as soon as it is created, so simply edit the file, (again using sudo nano webpage.js) to include the 'public' directory -ie /home/pi/Scripts/public/eink.jpg</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->If you now go to either http://localhost:8080/eink.jpg on the host machine or your http://<em>Your IP of the PI:</em>8080/eink.jpg you should be able to view the jpg.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->All that needs to be done now is to start the server when the Pi boots and to run the webpage script every set period of time. To load different webpages simply clone the webpage.js script but with a different URL to grab and run it at a different time, as mentioned, we run 4 scripts an hour via cron jobs.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph --><strong>Cron Jobs</strong></p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->The final part is to run the server at boot and the script every 15 minutes.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->Firstly go to your root directory by typing:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>cd:</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->Now we want to install a new Cron Job, or edit one we have already set up:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>sudo crontab -e</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->At the end of the file that opens add the following lines:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:code -->
<pre class="wp-block-code"><code>@reboot sudo /usr/bin/node /home/pi/Scripts/server.js
15 * * * * /usr/bin/node /home/pi/Scripts/webpage.js</code></pre>
<!-- /wp:code -->
<p><!-- wp:paragraph -->Whenever the Pi reboots it will now start the server - via your server.js script and every 15 minutes run your webpage.js script to take an image of a webpage, which you can subsequently point your eInk screen to load.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->It may feel like a number of hoops to jump through for a simple screengrab, but once running it opens up the wider world of Node.js and Puppeteer as well as the ability to use your eInk screen to display any webpage you want.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->I hope this has been useful, do drop me a line in the comments with any thoughts or tweet me <a href="https://twitter.com/digitalurban" target="_blank" rel="noreferrer noopener">@digitalurban</a>. It's part of a series of new 'how to's' here on <a href="https://digitalurban.org/">digitalurban.org </a>and over at <a href="https://connected-environments.org/" target="_blank" rel="noreferrer noopener">https://connected-environments.org/</a></p>
<p><!-- /wp:paragraph --><br /><!-- wp:paragraph --><!-- /wp:paragraph --> </p>
<p></p>
