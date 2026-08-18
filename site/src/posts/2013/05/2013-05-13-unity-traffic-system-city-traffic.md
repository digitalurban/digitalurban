---
title: "Unity Traffic System - City Traffic"
date: 2013-05-13 12:05:01
slug: "unity-traffic-system-city-traffic"
permalink: "/blog/2013/05/13/unity-traffic-system-city-traffic/"
author: "Andy"
categories: ["Game Engine", "Unity"]
tags: ["ABM", "traffic", "Unity"]
excerpt: "Creating a sandbox style traffic system in Unity is a challenge. As our previous posts have shown agents can use NavMesh and calculate shortest paths but the hit is high on processing which in turn…"
hero: "/assets/uploads/2013/05/Screen-Shot-2013-05-13-at-12.53.56-1.png"
---

Creating a sandbox style traffic system in Unity is a challenge. As our previous posts have shown agents can use NavMesh and calculate shortest paths but the hit is high on processing which in turn limits the number of agents in a scene. <a href="http://sandervandervegte.nl/">Sander van der Vegte</a> is a multidisciplinary game developer who for the past 12 years has fortunate enough to make a living creating games, part of his current development process is a city traffic game and thus finding ways for natural behaviour while maintaining a low processing requirment.
<figure><a href="/assets/uploads/2013/05/Screen-Shot-2013-05-13-at-12.53.56-1.png"><img class=" wp-image-3359" title="Unity City Traffic" alt="Screen Shot 2013-05-13 at 12.53.56" src="/assets/uploads/2013/05/Screen-Shot-2013-05-13-at-12.53.56-1.png" width="666" height="329" /></a><figcaption>Unity City Traffic</figcaption></figure>
The clip below is a recording of an autonomous traffic system. Cars drive around while aware of crossings and other vehicles. When something is blocking their path, they will stop. If it takes too long, they will back up and look for another path, the basic ruleset allows for humorous situations:
<center><iframe src="http://player.vimeo.com/video/41237419?byline=0&amp;portrait=0" width="640" height="416" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe> <p><a href="http://vimeo.com/41237419">Traffic system</a> from <a href="http://vimeo.com/user8707001">Sander van der Vegte</a> on <a href="http://vimeo.com">Vimeo</a>.</p></center>
Within the development the user is able to click on a car to take it over while falling off the edge triggers the random camera again.
It is well worth heading over to <a href="http://sandervandervegte.nl/">http://sandervandervegte.nl/</a> to view his other projects and to keep up to date on City Traffic.
