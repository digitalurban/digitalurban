---
title: "Turn Any Device into a Literary Clock with our MQTT Feed"
date: 2024-07-15 13:40:48
slug: "turning-any-device-into-a-literary-clock-with-mqtt"
permalink: "/blog/2024/07/15/turning-any-device-into-a-literary-clock-with-mqtt/"
author: "Andy"
categories: ["Making"]
tags: ["clock", "literacy clock", "mqtt", "time quote clock"]
excerpt: "The Concept of the Literary Clock A literary clock is a unique fusion of literature and timekeeping. Every minute of the day is represented by a corresponding quote from a literary work, providing…"
hero: "/assets/uploads/2024/07/Kindle.webp"
---

<!-- wp:paragraph -->
<p><strong>The Concept of the Literary Clock</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A literary clock is a unique fusion of literature and timekeeping. Every minute of the day is represented by a corresponding quote from a literary work, providing not just the time, but a nugget of wisdom, humor, or beauty from the world of books. This idea transforms the mundane act of checking the time into a delightful literary experience. The initial concept, as outlined by the original <a href="https://www.literaryclock.com/posts/Lt0_Blueprint">Literary Clock Project</a>, involves creating a clock that displays quotes from various literary works for every minute of the day. This concept not only appeals to book lovers but also serves as an artistic and educational piece, bringing literature into everyday life in a novel way. For example, as we type this the time is twenty one minutes to five and the quote from the database, including the book name is:</p>
<!-- /wp:paragraph -->

<!-- wp:pullquote -->
<figure class="wp-block-pullquote"><blockquote><p>&nbsp;</p><cite>"I was told that in his vest pocket he kept a chronometer instead of a watch. If someone asked him what time it was, he would say, ""<strong>A minute and twenty-one seconds to five</strong>.""" Book: The Collected Stories</cite></blockquote></figure>
<!-- /wp:pullquote -->

<!-- wp:paragraph -->
<p><strong>Crowdsourcing the Literary Database</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>An essential aspect of this project was the crowdsourcing of the literary database. The <a href="https://www.literaryclock.com/posts/Lt1_Crowdsourcing">Literary Clock Project</a> engaged a global community of literature enthusiasts to contribute quotes for every minute of the day. This collaborative effort created a diverse and rich collection of quotes, encompassing a wide range of genres, periods, and authors. Contributors from around the world submitted their favourite passages, transforming this project into a communal celebration of literature. The concept was taken a step further by tjaap who cleaned up the database and ported it onto a Kindle, <a href="https://www.instructables.com/Literary-Clock-Made-From-E-reader/">complete with a full instructable</a> on how to build you own.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7850,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/assets/uploads/2024/07/Kindle.webp" alt="" class="wp-image-7850"/><figcaption class="wp-element-caption">The Kindle Literary Clock by tjapp</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>Porting to MQTT</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol designed for small sensors and mobile devices optimized for high-latency or unreliable networks. It’s perfect for the Internet of Things (IoT) applications where bandwidth and battery power are at a premium. It is also good for transmitting short text messages to display across multiple devices at the same time, as long as a device is connected to an MQTT broker, it will automatically display messages as they arrive.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As such, as have created a Python script to read the database and publish the time quotes every minute to our MQTT broker on the following address:<strong> /personal/ucfnap/timequote</strong> (its a little but like tuning a radio, but in the case of MQTT, subscribing to topics).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>How It Works:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>1. <strong>Data Collection</strong>: We are using the extensive CSV file containing literary quotes provided by the Kindle Literarty Clock project, where each quote is tagged with a specific minute of the day. To make it work with our script we tidied things up a little.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>2. <strong>Publishing</strong>: This CSV is processed and published via the MQTT feed. Each minute, a new message is sent out containing the current time and the corresponding quote.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>3. <strong>Subscription</strong>: Any device can subscribe to this MQTT feed to receive the quotes in real-time. This could be an e-ink screen, a smart display, or even a mobile application - ie at 10.47 a device would receive the following message:</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><!-- wp:paragraph -->
<p><strong>10.07 am</strong>: In a meeting with Rod, Momo and Guy. We are rehearsing the final for the third time, with Rod and Guy taking the parts of the clients, when Rod's secretary, Lorraine, bursts in. Book: I Don't Know How She Does It</p>
<!-- /wp:paragraph --></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p><strong>Applications</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>E-Ink Screens</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Perhaps one of the most elegant implementations of this concept is using e-ink screens. E-ink displays are known for their paper-like readability and low power consumption, making them perfect for a literary clock. For an example of this, you can check out our detailed guide on setting up an e-ink screen with MQTT via our previous project THE: Time Headlines and Environmental Information <a href="https://www.digitalurban.org/blog/2020/04/10/the/">here</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7856,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="/assets/uploads/2024/07/timequoteclock-1024x560.png" alt="Literacy Clock using MQTY" class="wp-image-7856"/><figcaption class="wp-element-caption">Literary Clock using MQTT</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>Smart Displays and Mobile Apps</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Beyond e-ink screens, this feed can be integrated into various smart displays and mobile applications. For example, we have intergrated it into our Home Assistant Dashboard, updating the time with a quote every minute. You could also add it to a HUB75 LED Matrix - below is our example of using an LED Matrix as a general data feed, but by simply changing the MQTT feed, it transforms into a Literary Clock.</p>
<!-- /wp:paragraph -->

<!-- wp:embed {"url":"https://youtu.be/kG3OStmfXLk?si=Yyi-UZIeQ3KHTFnd","type":"video","providerNameSlug":"youtube","responsive":true,"className":"wp-embed-aspect-16-9 wp-has-aspect-ratio"} -->
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
https://youtu.be/kG3OStmfXLk?si=Yyi-UZIeQ3KHTFnd
</div></figure>
<!-- /wp:embed -->

<!-- wp:paragraph -->
<p>&nbsp;</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Setting Up Your Literary Clock</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Setting up your device is easy -</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>1. <strong>Choose Your Device</strong>: Select a device that can run an MQTT client. This could be an e-ink screen, a Raspberry Pi with a display, or a smartphone.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>2. <strong>Install an MQTT Libary</strong>: There are numerous MQTT libraries available, we mainly use Paho.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><p>3. <strong>Subscribe to the Feed</strong>: Point your client to the feed /personal/ucfnap/timequote&nbsp;</p>
<p>Configure your client to display the received messages. Our open MQTT Broker is mqtt.cetools.org on Port 1883</p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Of course you may not want to bother with Raspberry Pi's or other about with MQTT, or hack a Kindle - in which case, for those looking for a ready-made commercial version, check out the <a href="https://www.authorclock.com/">Author Clock</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":7851,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="/assets/uploads/2024/07/author-clock.png" alt="" class="wp-image-7851"/><figcaption class="wp-element-caption">The Rather Lovely Author Clock</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><p>The Author Clock is a beautifully designed literary clock that comes pre-loaded with thousands of quotes from a wide array of literary works. It’s an excellent choice for those who want to enjoy the literary clock experience without the need for a DIY setup.</p> <p>With our MQTT messages, any device can now be simply converted into a Literary Clock.</p></p>
<!-- /wp:paragraph -->
