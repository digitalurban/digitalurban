---
title: "Chasing the Tween: My 25-Year Obsession with Weather Data"
date: 2025-07-25 13:04:19
slug: "chasing-the-tween-my-25-year-obsession-with-weather-data"
permalink: "/blog/2025/07/25/chasing-the-tween-my-25-year-obsession-with-weather-data/"
author: "Andy"
categories: ["Weather", "Weather Display"]
tags: []
excerpt: "From Adobe Flash through to Vibe Coding and back again to Physical Displays"
hero: "/assets/uploads/2025/08/c9222c82-63e0-4ee7-9c73-3f9074cdac56_1378x1040.png"
---

<!-- wp:heading -->
<h2 class="wp-block-heading">From Adobe Flash through to Vibe Coding and back again to Physical Displays</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For those of us who run a personal weather station (PWS), the obsession isn't just about collecting data; it's about seeing it and sharing it, and that often means an online data dashboard. At the Connected Environments Lab based within the Centre for Advanced Spatial Analysis, University College London, we have been running weather stations in Central London since the early 2000s, each one uploading and communicating data every 3 seconds - that's approximately 268,918,537 measures of wind speed, air pressure, temperature, and solar intensity, amoungst others, including cloud height and now air quality etc. Getting the data online, however, has never been quite as easy as it should be…</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">The Past: The Golden Age of Tweens and Live Dials</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>So, back in the early 2000s, getting a Davis, Oregon Scientific, or La Crosse station online was a rite of passage for anyone interested in environmental data. The challenge wasn't just mounting the hardware; it was wrestling with software to display the information. In this era, two names stood out for many hobbyists: Cumulus and Weather Display, and we have used them both extensively over the years.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Weather Display</strong>, the long-standing creation of New Zealand-based developer Brian Hamilton, is a testament to the remarkable longevity of software. First appearing around 1999, it has been continuously developed for over two decades with hundreds of updates, making it a cornerstone of the personal weather station community. Its web component, <strong>Weather Display Live</strong>, became the golden standard for its time. Built entirely on Adobe Flash, it presented a fully featured dashboard of analogue-style gauges and tickers updating in real-time. The wind speed needle would smoothly tween with every gust, the rain gauge would visibly fill, and a ticker tape would scroll with the latest observations, creating a dynamic and immersive view of the weather that was unparalleled in its era. I’ve been chasing that smooth ‘tween’ ever since in dashboards, and indeed, further into this article that tween is still the ultimate draw in real-time data.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/6e0f7ac1-9c5c-4146-975e-6040b344b15e_555x414.gif" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>By today's standards, Weather Display Live perhaps looks cluttered, as design language shifts, indeed we are about to enter the era of ‘glass’ with the latest iOS updates and that will bring about a whole new look to apps and displays. Despite Adobe Flash requiring a browser plugin it allows dashboard that using the then HTML standard would simply not have been possible.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For a brief time Flash burned bright and was the basis of data on a little desktop device known as the Chumby - the Chumby was a device ahead of its time, providing realtime data updates via a series of rotating dashboards. As such it was the perfect device for displaying weather data, although the technical knowledge at the time, escaped me. Luckly a computer scientist, now <a href="https://profiles.ucl.ac.uk/4441-steven-gray">Professor Steven Gray</a> had recently joined our lab and kindly wrote a custom script to display the data.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/d52d9de1-6609-4b62-9a21-48e749430e74_400x294.jpeg" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>However, Flash’s days were numbered when Steve Jobs famously called it a ‘bag of hurt’, ushering in a new age of HTML5 and laying the foundations to the web we see today.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Alongside Weather Display was <strong>Cumulus</strong> (now <strong>Cumulus MX</strong>), which carved out a huge following, particularly for Windows users. It was, and is, a robust piece of software for processing PWS data. Its approach to web display was more traditional. It used a system of web templates and tags. You could design a basic HTML page, insert special tags like <code>&lt;#temp&gt;</code>, and Cumulus would periodically process this file, replacing the tags with current data and uploading it to your web server. While it lacked the fluid dynamism of Flash, it was reliable and customisable if you knew your way around HTML and CSS. It represented, arguably the dawn of the template-driven, self-hosted dashboard. Adobe Flash dials were replaced with new plugin free gauges via a system known as Steel Gauges.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/47099276-d732-43e5-8f17-0765c9781acc_1146x1363.jpeg" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The Steel Gauges are a much-loved part of the Cumulus software legacy, while not part of the official template that came with the software, they were a hugely popular style that the Cumulus community created and shared, made possible by the software's flexible templating system. They are the perfect example of a design philosophy called <strong>skeuomorphism</strong> - which came and went but is actually one we end this article on with perhaps the best example of a weather dashboard, but more on that later.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Skeuomorphism's goal is to make digital items resemble their real-world counterparts. The Steel Gauges aesthetic was heavily influenced by the design trends of the late 2000s and early 2010s, aiming to make a web page look like a physical, high-end piece of hardware. The designs were rich with photorealistic detail: brushed metal or carbon fibre backgrounds, glistening chrome bezels with drop shadows, and precisely rendered needles and tick marks. The goal was to create a sense of tangible reality on the screen.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The implementation was a clever two-part process:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li>
<p><strong>The Visuals:</strong> A user would first design the entire dashboard as a single, static background image in a graphics program like Photoshop. This image contained all the "steel" dials, gauges, and labels, but with no data.</p>
</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>
<p><strong>The Data:</strong> They would then use this image as a background in an HTML file. The magic happened by using Cumulus's simple but powerful templating engine. Users would strategically place Cumulus's special "web tags" (e.g., <code>&lt;#temp&gt;</code>, <code>&lt;#windspeed&gt;</code>, <code>&lt;#press&gt;</code>) over the blank areas on the gauges.</p>
</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>When Cumulus processed this file, it would replace the tags with the live weather data. The software would then automatically upload the updated HTML file and the background image to the user's web server.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Today, the Steel Gauges are perhaps a time capsule of a specific design era. They were built for a desktop-first world and were not responsive, often looking cluttered on mobile screens. As web design shifted towards minimalism, flat design, and mobile-first principles, the Steel Gauge aesthetic was largely superseded by clean, abstract, and data-dense interfaces like the Belchertown skin for WeeWX, which we come to next. However, they remain a nostalgic and important step in the evolution of personal weather data visualisation.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">The Current: Between Open and Closed Systems</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Standing down our Weather Display and Cumulus systems, we moved onto software known as WeeWX, running on a Raspberry Pi and sending data to a variety of online sources. It remains the system we use today. <strong>WeeWX</strong> (often stylised as weewx ) is a foundational piece of software in the modern personal weather station (PWS) world, but it's fundamentally different from its predecessors. It is best understood not as a single application, but as an open-source software engine for collecting, processing, and displaying weather data.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It was created earlier than we at first thought - by Tom Keffer, with initial development beginning in the winter of 2008, with the first official release of WeeWX in 2009.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>WeeWX is written entirely in Python and designed to run on Linux-based systems. This makes it the go-to choice for hobbyists who want to run their weather station on a low-power, single-board computer like a Raspberry Pi, operating 24/7 with minimal energy consumption, making it a notable move away from our previous power-hungry Windows machines.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The core philosophy is based around modularity and extensibility. It treats the different parts of managing a weather station as separate, interconnected components:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li>
<p><strong>The Engine:</strong> At its heart, weewx runs a main loop that communicates directly with the weather station hardware. It polls the station every few seconds for live data (like wind speed) and stores this information in a database (typically SQLite by default, though others are supported).</p>
</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>
<p><strong>The Reporting Cycle:</strong> At a regular, user-defined interval (the "archive interval," often every 5 minutes), the reporting engine wakes up. It pulls the latest data from the database and uses it to generate reports.</p>
</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>
<p><strong>Skins and Generators:</strong> This is where the user-facing magic happens. A "skin" in weewx is a complete template for a website, containing HTML files, CSS, images, and configuration settings. Using the powerful Cheetah templating engine, weewx fills these templates with data to generate static HTML pages. It can also run "generators" that push data to public services like Weather Underground, PWSWeather, and in our case custom MQTT brokers - this is key as it opens up the new world of Vibe Coding, which we come to next.</p>
</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>
<p><strong>Extensibility:</strong> The most powerful feature of weewx is its architecture, which is designed to be extended. Users can write their own services in Python to calculate new variables (e.g., custom fire danger indices), add new sensor types, or create entirely new report formats. This makes it a flexible platform for tinkerers and data enthusiasts.</p>
</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Out of the box, weewx comes with a simple, functional skin. However, its skinning architecture is has been key to community projects. The most used by far is the <strong>Belchertown skin</strong>, created by Pat O'Brien. First gaining widespread popularity around early 2019, Belchertown provides a clean, modern, mobile-responsive interface with dark mode, interactive charts, and real-time streaming updates via MQTT. It has become the de-facto "face" of weex for many users and perfectly embodies the modernist design principles of clarity and function.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/c2962b81-6ed6-4e7d-94f4-e1d967c6d90d_2078x1310.png" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>At the polar opposite of weewx are the more propoietry systems that are run by the weather station hardware providers - Davis, being one key example with their live data system via Weatherlink.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Davis Instruments is a respected name in the personal weather station market, occupying the premium "prosumer" space. Based in California, the company is renowned for producing accurate, durable, and reliable hardware that is arguably considered a gold standard by serious hobbyists, educators, and agricultural professionals.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Their flagship products are the <strong>Vantage Pro2</strong> (their expandable, top-of-the-line model) and the <strong>Vantage Vue</strong> (a more compact, all-in-one unit). For decades, the main challenge for Davis owners was getting the rich data from this excellent hardware onto a computer and the internet - we have run their Vantage Pro line since the 2000’s and now use weewx - but they do have their own ‘out of the box’ system for people who do not want to tinker with a Raspberry Pi.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Originally, connecting a Davis station required a piece of hardware called the <strong>WeatherLink Data Logger</strong>. This was a small module that slotted into the back of the weather station console, attached via a serial or USB cable to a PC. To get data online 24/7, a user had to leave a computer running constantly with the WeatherLink PC software. The data logger itself was a one-time hardware purchase, costing around £150-£250 - our data logger used to plug into our Windows machine and Weather Display.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/e9477f3e-033f-4101-910c-e235f1689a95_832x802.png" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The modern solution is thankfully far more elegant. Davis replaced the data logger with their <strong>WeatherLink Live </strong>unit in 2019. This small, standalone box acted as an internet bridge. It independently listened for the radio signals from the outdoor sensors and sent the data directly to their WeatherLink Cloud. This was the first device to eliminate the need for a console to be connected to a computer - it basically took the computer out of the workflow.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This was superseded by the <strong>WeatherLink Console (model 6313)</strong> in early 2023, updating the previous and notably dated previous iteration.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/c9222c82-63e0-4ee7-9c73-3f9074cdac56_1378x1040.png" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Today, WeatherLink refers to the entire cloud-based ecosystem (<code>WeatherLink.com</code> and the mobile app). When you buy and connect a WeatherLink Live device, you get access to this platform. It allows you to view your data from anywhere, see historical charts, and share your station publicly.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The web-based dashboard is, however, slightly ‘clunky’ and arguably badly designed:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/10cac172-5be4-4dac-84e6-19e93c18ee95_2858x1250.png" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>It also operates on a tiered subscription model, and to view your data in real-time, costs.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li><p><strong>Basic Tier (Free):</strong> When you purchase your hardware (e.g., a Vantage Vue station + a WeatherLink Live device), you get the Basic tier for free. This includes:</p><!-- wp:list -->
<ul><!-- wp:list-item -->
<li>
<p>Your current, live data updated every minute.</p>
</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>
<p>A 24-hour chart of your data.</p>
</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>
<p>The ability to see your data on the app and website.</p>
</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><p><strong>Pro Tier (Paid):</strong> This is the most common upgrade for enthusiasts. For a recurring fee, it unlocks much deeper access to your own data.</p><!-- wp:list -->
<ul><!-- wp:list-item -->
<li>
<p><strong>Cost:</strong> Approximately <strong>$3.95/month</strong> or <strong>$42.50/year</strong> (with prices subject to change and regional variation).</p>
</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><p><strong>Features:</strong></p><!-- wp:list -->
<ul><!-- wp:list-item -->
<li>
<p>Access to your full, detailed historical data archive.</p>
</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>
<p>Advanced, customisable charting tools to analyse your history.</p>
</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>
<p>More frequent "live" data updates on the web (every 2.5 seconds).</p>
</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>
<p>The ability to download your data archive as a CSV file.</p>
</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>As such, we still have our Davis Vantage Pro plugged into a WeeWX system, which enables the transmission of data through an MQTT server and bypasses any paywalls to view our own data.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Towards Personal Templates with Vibe Coding</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This would normally leave us with the Belchertown Skin, and while excellent, the itch to edit and innovate is always strong, and with it the desire to pull in increasingly customised data feeds, pulling in multiple sources of data to gain a better overview of the current environmental conditions. This would normally require a good understanding of data structures, application protocol interfaces, cascading style sheets, JavaScript and perhaps a bit of Firebase and databases. All of course are good to know and learn but if you want a new look to your data and only have a hour free then Vibe Coding is the current route to take. As in <a href="https://open.substack.com/pub/digitalurban/p/vibe-coding-from-ios-apps-to-an-asteroid?r=u7cv&amp;utm_campaign=post&amp;utm_medium=web&amp;showWelcomeOnShare=true">our previous substack post</a>, the term ‘Vibe Coding’ was defined Andrej Karpathy, a co-founder at OpenAI in Early 2025. The basic idea is to rely entirely on Large Language Models - LLMs - and code by using only natural language prompting, rather than writing the code yourself. At the moment we are exploring this new way to develop Weather Dashboards and are in the process of adding examples to our GitHub.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/97dbcfce-e0bd-45a3-9545-004e2794b0b8_2172x1434.png" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Our first example (see <a href="https://digitalurban.github.io/VibeWeatherDashboards/mixed_dashboard.html">https://digitalurban.github.io/VibeWeatherDashboards/mixed_dashboard.html</a>), pictured above, was created using Gemini 2.5 Pro, which is currently available for free for a month. The Pro version provides sufficient usage to create an unlimited number of dashboards. Vibe Coding is good - but it's not that good, it won’t create the dashboard above in a single prompt, it takes a number of iterations, starting small and building up. It was built using the Canvas feature, which allows both a view of the code and a live preview, making it quick and easy to make changes. For example, our first prompt into Gemini was ‘make a 5-day forecast for ‘our area’ using a free weather api and use flat icons’. This created the 5-day forecast, using the Open-Meteo API, we subsequently pointed Gemini to our weewx data feed and asked it to use the same icon style to provide a dashboard using the key weather data indicators of Temperature, Wind, Rain, Pressure and Solar. Once that was working, with a few edits back and forth, we then added the coloured background, which changes colour according to the outside temperature, ranging from a dark blue for -10 °C through to a deep red for 35 degrees and above.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>At the moment, we have it running on an old iPad, which we have mounted in a frame, sitting on a bookshelf in the corner of the room:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/d5d36992-40bc-4b19-bfc3-1e2f02bf3bb5_4032x3024.jpeg" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Vibe coding has also enabled us to explore the creation of AI Weather Landscape dashboards, which take the raw output of the UK Met Office forecast and send it to the Google Vertex AI platform to interpret it as an image of an English Landscape, twice a day.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/04e83eb9-9581-4337-85c1-34f6ea5b0c07_2878x1502.png" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Finally, Vibe Coding has allowed us to experiment with real-time graphing, something that harks back to Cumulus, as their templates integrated a series of graphs as part of a drop-down menu. Our graphing displays data in real-time over a period of 24 hours, allowing trends to be visualised and also the graphs to update as new data points come in.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/5ff88b88-0d27-49ea-8a91-e5ebb001582e_2526x1464.png" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The creation of a real-time graphing required the setting up of Firebase - something which is not overly self-explanatory. However, using Vibe Coding it only took an hour and a half from knowing little to nothing, to have a full system set up and running - it is all in the human language prompts and taking things in small steps. Our first prompt was ‘we have this data feed (insert mqtt feed link) and want to view it as a real-time graph, probably using Firebase, can you show us how to set it up and provide me with full code to view the data on a webpage’ - this was 6 months ago using ChatGPT, things move rapdily in this space and now there is <a href="https://firebase.google.com/docs/studio">Firebase Studio</a> which makes it even easier to get up and running.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Having been using and making weather dashboards in 25 years it is only in the last 6 months with the invention of Vibe Coding that innovation has speeded up. We have moved from clunky Windows PC looking interfaces through Flash, skeuomorphism, flat designs and now into hyper-customised dashboards using vibe computing. Yet there is one dashboard that I have kept looking at over the years and so far have been unable to replicate (mainly due to copyright issues, but also the code) - and that is an online version of the classic Intromet Climatica Weather System.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/0ad7a09e-94b3-4f51-80fb-4ca5b437fae1_2126x996.png" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>It is perhaps the ultimate digital-analogue physical display, and one that is likely on every weather data enthusiast's wish list. While the physical system remains out of reach for us, the developer over at <a href="https://weather.wilmslowastro.com/test/instromet/climatica/climatica.php">Wimslow Weather has made an online version</a> (hidden away under his developer section) and it is lovely:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2025/08/51199862-05f6-4d50-bc90-c07c3df461fc_2862x1354.png" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Sure, it's full on skeuomorphism - but the tween on the wind direction and wind speed is one of the best we have seen - so despite having access to the new opportunities of AI, it's a physical design from a small <a href="https://instromet.co.uk/climatica-weather-station/">British company, Instromet</a>, that somehow still remains the best, in our view.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We would love to know what dashboard you like or us, do tell us in the comments, and if you like this article, the subscribe link is of course below.</p>
<!-- /wp:paragraph -->
