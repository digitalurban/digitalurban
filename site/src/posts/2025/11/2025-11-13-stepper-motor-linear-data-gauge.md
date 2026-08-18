---
title: "Stepper Motor Linear Data Gauge"
date: 2025-11-13 12:01:34
slug: "stepper-motor-linear-data-gauge"
permalink: "/blog/2025/11/13/stepper-motor-linear-data-gauge/"
author: "Andy"
categories: ["Making"]
tags: ["Data", "gauge", "iot", "stepper", "Weather"]
excerpt: "The latest upload to the Open Gauges Github is a Linear Gauge, using a timing belt to provide Linear Stepper Motor Gauge a full 1 metre range for the data visualisation. It uses a stepper motor for…"
hero: "/assets/uploads/2025/11/WindStepperLinearClose.jpeg"
---

The latest upload to the <a href="https://github.com/ucl-casa-ce/Open-Gauges/tree/main">Open Gauges Github</a> is a Linear Gauge, using a timing belt to provide

<figure><img class="wp-image-170079126 size-large" src="/assets/uploads/2025/11/WindStepperLinear-200x1024.png" alt="Linear Stepper Motor Gauge" width="200" height="1024" /><figcaption>Linear Stepper Motor Gauge</figcaption></figure>

a full 1 metre range for the data visualisation. It uses a stepper motor for precise needle movement, and a limit switch for calibration, it can be adapted to any MQTT data feed and any base mount. The example shown uses a 5cm by 10cm peice of wood, cut to 1 metre length and indicates wind speed from 0 to 60 mph.
<p class="p1">The design uses a stepper motor (like the 28BYJ-48) which offers high-precision, 360-degree movement without the jitter or limited range of a standard servo. The limit switch allows the gauge to "home" itself on startup, ensuring the pointer always starts at a known zero position.</p>
<p class="p1">The main code - <span class="s1">WindStepperTimerBeltwithLimitSwitch.ino</span> in the Github has a distance calibration number, adjust for your range.</p>
<p class="p1"><b>Hardware Components</b></p>

<ul class="ul1">
 	<li class="li1">Arduino-compatible Board: Any board like an Arduino Uno, Nano, or a NodeMCU.</li>
 	<li class="li1">Stepper Motor: 28BYJ-48 5V stepper motor.</li>
 	<li class="li1">Stepper Driver: ULN2003 driver board (which often comes with the 28BYJ-48).</li>
 	<li class="li1">Limit Switch: A small microswitch to detect the pointers zero position.</li>
 	<li class="li1">Power Supply: USB.</li>
 	<li class="li1">Timer Belt <a href="https://www.amazon.co.uk/Timing-Pulley-Tensioner-Torsion-Printer/dp/B0C54ZXM88/ref=sxin_15_pa_sp_search_thematic_sspa?content-id=amzn1.sym.0a6bbb1a-ed2d-4392-adfc-40ed1cfcd8e2%3Aamzn1.sym.0a6bbb1a-ed2d-4392-adfc-40ed1cfcd8e2&amp;crid=L07UDXXKCZFX&amp;cv_ct_cx=timing%2Bbelt%2Bgt2&amp;keywords=timing%2Bbelt%2Bgt2&amp;pd_rd_i=B0C54ZXM88&amp;pd_rd_r=12141bbe-35d0-4c0a-8811-d7f399206de4&amp;pd_rd_w=AVwDb&amp;pd_rd_wg=JG5Mx&amp;pf_rd_p=0a6bbb1a-ed2d-4392-adfc-40ed1cfcd8e2&amp;pf_rd_r=H6T6R7VAGD99FGNPH875&amp;qid=1763028887&amp;sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&amp;sprefix=timer%2Bbelt%2Bgt2%2Caps%2C99&amp;sr=1-5-ad3222ed-9545-4dc8-8dd8-6b2cb5278509-spons&amp;aref=vwr3X339Nm&amp;sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&amp;th=1"><span class="s2">GT2 Timer Belt</span></a></li>
</ul>
It is made to be as simple to build/power as possible but also adatable for a number of senarios.

The github provides the mount for the stepper motor, the pointer (which also joins together the timing belt) the limit switch and the end mount for the pulley. These allow the gauge to be adapted to any size required.

At the moment the gauge is sitting on the wall in our lounge and it has become one of our most used guages. The data updates every minute to show the maximum wind gust and due to the nature of the stepper motor, it provides a smooth movement, almost replicating the gust of wind.

&nbsp;
