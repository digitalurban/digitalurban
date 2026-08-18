---
title: "Just Weather for The Pebble Watch: Making a Data Watch Face"
date: 2025-10-30 12:59:40
slug: "just-weather-for-the-pebble-watch-making-a-data-watch-face"
permalink: "/blog/2025/10/30/just-weather-for-the-pebble-watch-making-a-data-watch-face/"
author: "Andy"
categories: ["Apps"]
tags: ["copilot", "Data", "github", "Pebble Watch", "Weather"]
excerpt: "It's an exciting time to be a Pebble fan. After years of being kept alive by the dedicated Rebble community, the Pebble is officially back. The new Pebble 2 Duo watches (the black-and-white model)…"
hero: "/assets/uploads/2025/10/Screenshot-2025-10-30-at-12.49.33.png"
---

<p></p>
<p><!-- wp:paragraph -->It's an exciting time to be a Pebble fan. After years of being kept alive by the dedicated Rebble community, the Pebble is officially back. The <a href="https://store.repebble.com/">new Pebble 2 Duo watches</a> (the black-and-white model) are officially shipping to the first backers, with the high-resolution color Pebble Time 2 set to follow.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->So, I decided to make one myself.</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:heading -->
<h2 class="wp-block-heading">Introducing 'Just Weather'</h2>
<!-- /wp:heading -->
<p><!-- wp:paragraph -->I wanted a face that was clean, digital, and gave me all the key data at a glance, formatted to look great on the 144x168 screen of the Pebble 2. I call it <strong>"Just Weather."</strong></p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->It uses the free Open-Meteo API to pull in a ton of useful, hyperlocal data right to your wrist:</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:list -->
<ul>
<li style="list-style-type: none;">
<ul><!-- wp:list-item -->
<li>Current Location (from your phone's GPS)</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Temperature</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Current Conditions ("Partly Cloudy," "Rain," etc.)</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Barometric Pressure &amp; 3-Hour Trend</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Wind Speed &amp; Precipitation</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>...and of course, the time!</li>
</ul>
</li>
</ul>
<!-- /wp:list-item -->
<p>&nbsp;</p>
<!-- /wp:list -->
<p>&nbsp;</p>
<!-- wp:heading -->
<h2 class="wp-block-heading">Built with GitHub CoPiliot</h2>
<!-- /wp:heading -->
<p><!-- wp:paragraph -->The best part is that the new Pebble development workflow is incredibly modern. I was able to build this using the <strong>CloudPebble IDE</strong>, which now integrates directly with <strong>VS Code in the browser</strong>.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->This meant I could use the emerging tools like <strong>GitHub Copilot</strong> to help generate the code and work through the trickiest parts—like making direct HTTPS requests to the weather API, which (after a lot of testing!) we proved is possible from the phone app.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->After getting the data, the final step was tweaking the C code to make sure the layout wasn't clipped and all the information fit perfectly on the 144x168 screen. It's now compatible with watches in the Pebble family, from the original Pebble Time (color) to the new <strong>Pebble 2 Duo</strong> and the upcoming <strong>Pebble Time 2</strong>.</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:image {"id":170079097,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img class="wp-image-170079097" src="/assets/uploads/2025/10/Screenshot-2025-10-30-at-12.49.33-1024x727.png" alt="Pebble Watch Face" />
<figcaption class="wp-element-caption">Pebble Watch Face</figcaption>
</figure>
<!-- /wp:image -->
<p>&nbsp;</p>
<!-- wp:heading -->
<h2 class="wp-block-heading">Available Now</h2>
<!-- /wp:heading -->
<p><!-- wp:paragraph -->This project took around 6 hours, with the main issue being that Co-Pilot did not know how to get HTTP requests - it took me down a lot of rabbit holes, and in the end, it was down to using a simpler call on the data - XMLHttpRequest. Once this worked it all fell into place and it was simply a case of asking Copilot to add in the data fields, do the geocoding and then take a step back and explain how the code actually works.</p>
<!-- /wp:paragraph -->
<p><!-- wp:paragraph -->If you're like me and just want a simple, data-rich weather face, please give it a try...</p>
<!-- /wp:paragraph -->
<p>&nbsp;</p>
<!-- wp:list -->
<ul>
<li style="list-style-type: none;">
<ul><!-- wp:list-item -->
<li><strong>Download '<a href="https://apps.rebble.io/en_US/application/69034d22d004720008412cf1">Just Weather</a>' from the Rebble Appstore</strong></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Check out <a href="https://github.com/digitalurban/just-weather-pebble-watchface">the source code on GitHub</a> for the latest updates - now includes its own settings page (its become a proper watch face app)...</strong></li>
</ul>
</li>
</ul>
<!-- /wp:list-item -->
<p>&nbsp;</p>
<!-- /wp:list -->
<p>&nbsp;</p>
<p></p>
