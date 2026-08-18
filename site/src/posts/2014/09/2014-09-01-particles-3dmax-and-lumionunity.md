---
title: "Particles -  3dsMax and Lumion/Unity"
date: 2014-09-01 10:43:24
slug: "particles-3dmax-and-lumionunity"
permalink: "/blog/2014/09/01/particles-3dmax-and-lumionunity/"
author: "Andy"
categories: ["3D Max", "3D Modelling"]
tags: ["3dsmax", "lumion", "lumion3d", "particles", "Unity"]
excerpt: "Particle Flow is a versatile, powerful particle system for Autodesk's 3ds Max . It employs an event-driven model, using a special dialog called Particle View, allowing you to combine individual…"
hero: "/assets/uploads/2014/09/Screen3DMaxParticles1-1.jpg"
---

<p class="blurb" style="color: #000000;">Particle Flow is a versatile, powerful particle system for Autodesk's <span class="charspan-msgph">3ds Max</span>. It employs an event-driven model, using a special dialog called <span class="char_link">Particle View, allowing</span> you to combine individual <span class="char_link">operators</span> that describe particle properties such as shape, speed, direction, and rotation over a period of time into groups called <span class="char_link">events</span>. Each operator provides a set of parameters, many of which you can animate to change particle behaviour during the event. As the event transpires, Particle Flow continually evaluates each operator in the list and updates the particle system accordingly.</p>
<figure><img class=" wp-image-3685" src="/assets/uploads/2014/09/Screen3DMaxParticles1-1-1024x560.jpg" alt="pFlow 3ds Max" width="590" height="322" /><figcaption>pFlow 3ds Max</figcaption></figure>
<p style="color: #000000;">To achieve more substantial changes in particle properties and behaviour, you can create a <span class="char_link">flow</span>. The flow sends particles from event to event using <span class="char_link">tests</span>, which let you <span class="char_link">wire</span> events together in series. A test can check, for example, whether a particle has passed a certain age, how fast it's moving, or whether it has collided with a deflector. Particles that pass the test move on to the next event, while those that don't meet the test criteria remain in the current event, possibly to undergo other tests. The simple example pictured above details a pFlow dialogue determining the birth of particles linked to a target geometry. The particles can subsequently be baked (using<a href="http://www.oferz.com/maxscripts.php"> pFlow Baker</a>) into an animation timeline for simple output via .fbx, allowing import into external systems such as Unity or Lumion.</p>
<p style="color: #000000;"></p><center><iframe width="640" height="360" src="//www.youtube.com/embed/Ex4SyeQMpFU" frameborder="0" allowfullscreen></iframe></center>
<p style="color: #000000;">The clip above illustrates the pFlow system imported into Lumion with the addition of a scene created in CityEngine.</p>
