---
title: "MQTT Scroller for the Pimoroni Stellar Unicorn: THE: Time, Headlines and Environmental Information"
date: 2023-08-03 08:49:16
slug: "mqtt-scroller-for-the-pimoroni-stellar-unicon-the-time-headlines-and-envivronmental-information"
permalink: "/blog/2023/08/03/mqtt-scroller-for-the-pimoroni-stellar-unicon-the-time-headlines-and-envivronmental-information/"
author: "Andy"
categories: ["Making"]
tags: ["CASA", "LED Matrix", "MQTT Scroller", "Pimoroni Stellar", "Pimoroni Unicorn", "UCL"]
excerpt: "Pimoroni make a range of LED matrix displays with Pi Pico W's built in - previously we have used the large scale Pimoroni Galatic Unicorn and added a series of scripts on GitHub to allow it to scroll…"
hero: "/assets/uploads/2023/08/PhotoRoom_20230801_135724-1024x1024.jpg"
---

<!-- wp:paragraph -->
<p>Pimoroni make a range of LED matrix displays with Pi Pico W's built in - previously we have used the large scale <a href="https://shop.pimoroni.com/products/space-unicorns?variant=40842033561683" target="_blank" rel="noreferrer noopener" data-type="URL" data-id="https://shop.pimoroni.com/products/space-unicorns?variant=40842033561683">Pimoroni Galatic Unicorn</a> and added <a href="https://github.com/ucl-casa-ce/Galactic-Unicorn-MQTT-Scroller" target="_blank" rel="noreferrer noopener" data-type="URL" data-id="https://github.com/ucl-casa-ce/Galactic-Unicorn-MQTT-Scroller">a series of scripts on GitHub</a> to allow it to scroll MQTT messages. Pimoroni have just released two new versions, the <a href="https://shop.pimoroni.com/products/space-unicorns?variant=40842626596947" target="_blank" rel="noreferrer noopener" data-type="URL" data-id="https://shop.pimoroni.com/products/space-unicorns?variant=40842626596947">Cosmic Unicorn</a> at 32 x 32 pixels and the <a href="https://shop.pimoroni.com/products/space-unicorns?variant=40842632953939" target="_blank" rel="noreferrer noopener" data-type="URL" data-id="https://shop.pimoroni.com/products/space-unicorns?variant=40842632953939">Stellar Unicorn</a> at 16 x 16 pixels, both of these are also pefect for scrolling information and as such we have updated our scripts and provided laser cut templates, firstly for the Stellar.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7226,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2023/08/PhotoRoom_20230801_135724-1024x1024.jpg" alt="" class="wp-image-7226"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The code is set up around our THE: Time, Headlines and Envivronmental Information stream, this links in feeds from our own MQTT server, providing details on the time, news, weather and earthquake information. You can choose to leave this in place (good for a first test) or add your own MQTT feed. The code uses different coloured backgrounds for different text in feeds - ie News, Weather, Time, you can edit these accordingly to match your own feed. Our feed updates every couple of minutes, for a constant stream of information.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To set it all, all you need do it copy all the files to your Stellar Unicon using Thonny - edit config.py to add your Wifi and MQTT broker credentials.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Headover to our <a rel="noreferrer noopener" href="https://github.com/ucl-casa-ce/Stellar-Unicorn-MQTT-Scroller" data-type="URL" data-id="https://github.com/ucl-casa-ce/Stellar-Unicorn-MQTT-Scroller" target="_blank">GitHub Repository to download the files</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7231,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2023/08/StellarParts-1024x970.jpg" alt="" class="wp-image-7231"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">The Case</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Three files are provided to laser cut:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li>The laser cut front as pictured with Etching (THE: Time, Headlines, Environmental)</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>The laser cut front, minus text</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Front cut for the clear acrylic</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The work has been created as part of work at the <a href="https://connected-environments.org/" data-type="URL" data-id="https://connected-environments.org/" target="_blank" rel="noreferrer noopener">Connected Environments Group</a> at the Centre for Advanced Spatial Analysis, University College London, the <a rel="noreferrer noopener" href="https://github.com/ucl-casa-ce/Stellar-Unicorn-MQTT-Scroller/discussions" data-type="URL" data-id="https://github.com/ucl-casa-ce/Stellar-Unicorn-MQTT-Scroller/discussions" target="_blank">GitHub page has its own discussion forum</a> if you would like to ask any questions or request changes to the code.</p>
<!-- /wp:paragraph -->
