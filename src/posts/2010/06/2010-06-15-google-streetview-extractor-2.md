---
title: "Google Street View Extractor"
date: 2010-06-15 08:58:00
slug: "google-streetview-extractor-2"
permalink: "/blog/2010/06/15/google-streetview-extractor-2/"
author: "Andy"
categories: ["extract street view", "google streetview", "Panoramas"]
tags: []
excerpt: "Jamie Thompson has put together a handy little webservice that mashes up postcode geodata with the Street View Images API. In short, it allows you to get access to the unwarped Street View panorama…"
---

<p><a href="http://jamiethompson.co.uk/">Jamie Thompson</a> has put together a handy little webservice that mashes up <a href="http://jamiethompson.co.uk/projects/2010/04/30/an-open-free-uk-postcode-geocoding-web-service/">postcode geodata</a> with the Street View Images API. In short, it allows you to get access to the unwarped Street View panorama and the underlying tiles.<br />
We have put together a short movie to show the service in action:<br />
<center><object width="640" height="385" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="allowFullScreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="src" value="http://www.youtube.com/v/_-lQV7rPuUw&amp;hl=en_US&amp;fs=1&amp;" /><param name="allowfullscreen" value="true" /><embed width="640" height="385" type="application/x-shockwave-flash" src="http://www.youtube.com/v/_-lQV7rPuUw&amp;hl=en_US&amp;fs=1&amp;" allowFullScreen="true" allowscriptaccess="always" allowfullscreen="true" /></object></center>As Jamie states, its handy in that it let’s you directly request a street view thumbnail with nothing more than a postcode.<br />
The format of the request looks like this:<br />
http://geo.jamiethompson.co.uk/streetview/_x.jpg<br />
You can <a href="http://geo.jamiethompson.co.uk/streetview_tiles.php?postcode=E1+6JN&amp;view=2&amp;zoom=2">try it out here</a> - just type in your own postcode.<br />
Thanks go to Dr Chris Speed for picking this up, you can <a href="http://twitter.com/chrisspeed">follow Chris on twitter</a>.</p>
