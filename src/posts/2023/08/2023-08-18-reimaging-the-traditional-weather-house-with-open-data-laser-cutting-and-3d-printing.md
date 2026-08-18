---
title: "Reimaging the Traditional Weather House with Open Data, Laser Cutting and 3D Printing"
date: 2023-08-18 13:36:46
slug: "reimaging-the-traditional-weather-house-with-open-data-laser-cutting-and-3d-printing"
permalink: "/blog/2023/08/18/reimaging-the-traditional-weather-house-with-open-data-laser-cutting-and-3d-printing/"
author: "Andy"
categories: ["Making", "Weather"]
tags: ["Black Forest", "Open Weather Map", "Pi Pico", "Weather", "Weather House"]
excerpt: "Traditional German weather houses are small, decorative structures that are popular in Germany and other parts of Europe. They are often made from wood and used to predict the weather. A Traditional…"
hero: "/assets/uploads/2023/08/Screenshot-2023-08-18-at-14.30.17-300x267.png"
---

<p><!-- wp:paragraph --></p>
<p>Traditional German weather houses are small, decorative structures that are popular in Germany and other parts of Europe. They are often made from wood and used to predict the weather.<!-- /wp:paragraph -->

<!-- wp:image {"align":"right","id":7182,"width":246,"height":159,"sizeSlug":"large","linkDestination":"none"} --></p>
<figure class="wp-block-image alignright size-large is-resized">
<figure><img class="wp-image-7297 size-medium" style="width: 246px; height: 159px;" src="/assets/uploads/2023/08/Screenshot-2023-08-18-at-14.30.17-300x267.png" alt="Weather House" width="300" height="267" /> A <a href="https://www.amazon.co.uk/TFA-Dostmann-48-1503-08-Weather-House-Germany/dp/B07PHYZ5TS/ref=d_pd_sbs_sccl_4_1/262-7292782-5370661?pd_rd_w=u62wm&amp;content-id=amzn1.sym.c633ef94-5925-4800-8916-1372f3be4382&amp;pf_rd_p=c633ef94-5925-4800-8916-1372f3be4382&amp;pf_rd_r=2JMCC8RK4PJTBANJDR5M&amp;pd_rd_wg=QST5L&amp;pd_rd_r=e3c70644-02b0-416d-b212-1f06c94d20a8&amp;pd_rd_i=B07PHYZ5TS&amp;th=1">Traditional Weather House</a></figure>
</figure>
<p><!-- /wp:image -->

<!-- wp:paragraph -->The way the weather house works is quite simple. Inside the house, there is a strip of catgut or hair. The gut relaxes or shrinks based on the humidity in the surrounding air, relaxing when the air is wet and tensing when the air is dry. Attached to the strip is a small figure of a man and a woman. When the humidity in the air changes, the strip will expand or contract, causing the figures to move.</p>
<p><!-- /wp:paragraph -->

<!-- wp:paragraph -->If the weather is going to be dry and sunny, the man will come out of the house. If it is going to be wet and rainy, the woman will come out of the house. If the humidity is just right, both the man and the woman will be visible.</p>
<p><!-- /wp:paragraph -->

<!-- wp:paragraph -->Traditional German weather houses are, an interesting, if slightly imprecise way to predict the weather. They are also a useful inspiration to develop a slightly more modern version using the Open Weather Map API, a 360-degree non-continuous servo, some neopixels and a Raspberry Pi Pico W.</p>
<p><!-- /wp:paragraph --> </p>
<!-- wp:image {"id":7279,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img class="wp-image-7279" src="/assets/uploads/2023/08/Weatherhousewide@0.5x-1024x419.jpg" alt="Weather House Laser Cut" />
<figcaption class="wp-element-caption">The Weather House Reimagined</figcaption>
</figure>
<p><!-- /wp:image -->

<!-- wp:paragraph -->In essence the house is a series of weather symbols which rotate according to the feed from the Open Weather Map API. This can be set to any location in the world and it updates every 15 minutes. It is also adaptable to change to your own source of weather data, perhaps your own personal weather station.</p>
<p><!-- /wp:paragraph --> </p>
<!-- wp:image {"id":7282,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img class="wp-image-7282" src="/assets/uploads/2023/08/WeatherHouseInternals-1024x614.jpg" alt="Weather House Components" />
<figcaption class="wp-element-caption">Weather House Components</figcaption>
</figure>
<p><!-- /wp:image -->

<!-- wp:paragraph -->There are also two sets of neopixels - one to light up the symbol, this works well at night and looks like an outside light on the house, allowing the weather conditions to be seen. The other is an 8 pixel neopixel strip which changes colour and animates according to the conditions. If it's raining then the lights change to blue and simulate raindrops, for sunny spells they light and dim with tinges of yellow to simulate the sun poking out of the clouds, etc. All of these are editable in the code to change according to your own preference.</p>
<p><!-- /wp:paragraph --> </p>
<!-- wp:image {"id":7284,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img class="wp-image-7284" src="/assets/uploads/2023/08/WeatherHouseNeoPixels-1024x618.jpg" alt="Weather House Neopixels" />
<figcaption class="wp-element-caption">Weather House Neopixels</figcaption>
</figure>
<p><!-- /wp:image -->

<!-- wp:paragraph -->At the heart of the weather house is a Raspberry Pi Pico W, held in a 3D printed enclosure which also encases the LEDs and the Servo.</p>
<p><!-- /wp:paragraph --> </p>
<!-- wp:image {"id":7280,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img class="wp-image-7280" src="/assets/uploads/2023/08/WeatherhouseTopDown-1024x495.jpg" alt="" />
<figcaption class="wp-element-caption">Weather House Laser Cut Outs</figcaption>
</figure>
<p><!-- /wp:image -->

<!-- wp:paragraph -->It slots into the case which, in our example, is laser cut from white perspex for the house and 3mm plywood for the roof.</p>
<p><!-- /wp:paragraph --> </p>
<!-- wp:image {"id":7281,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img class="wp-image-7281" src="/assets/uploads/2023/08/WeatherHouseLaserCut-1024x497.jpg" alt="Weather House Laser Cut Outs" />
<figcaption class="wp-element-caption">Weather House Laser Cut Outs</figcaption>
</figure>
<p>Once assembled the 3D printed enclosure along with the dial, fits into the main house. The servo is set to its starting point with the 'Sun' icon showing through the window.</p>
<p><!-- /wp:image -->

<!-- wp:paragraph --></p>
<figure><img class=" wp-image-7302" src="/assets/uploads/2023/08/Weather-House-Angled-300x166.jpg" alt="Weather House Inside View " width="774" height="428" /><figcaption>Weather House Inside View</figcaption></figure>
<p>We power ours from a 20,000mAh power bank which keeps it running for about a week. Each time the data updates the outside lamp turns on and off, so you have a visual clue that new data has uploaded.</p>
<p><!-- /wp:paragraph --> </p>
<!-- wp:image {"id":7291,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img class="wp-image-7291" src="/assets/uploads/2023/08/Weather-House-45-Degrees-1024x508.jpg" alt="Weather House Looking Down" />
<figcaption class="wp-element-caption">The Final Built Weather House</figcaption>
</figure>
<p><!-- /wp:image --></p>
<p>The Micropython code, build components, 3D print and laser cut files are available on <a href="https://github.com/digitalurban/Weather-House">our accompanying GitHub page</a>, note the project is still a work in progress..</p>
<p></p>
