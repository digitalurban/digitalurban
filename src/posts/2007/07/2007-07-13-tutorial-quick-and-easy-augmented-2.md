---
title: "Tutorial - Quick and Easy Augmented Reality from SketchUp/3DMax etc"
date: 2007-07-13 09:50:00
slug: "tutorial-quick-and-easy-augmented-2"
permalink: "/blog/2007/07/13/tutorial-quick-and-easy-augmented-2/"
author: "Andy"
categories: ["3D Max", "3D Modelling", "Augmented Reality", "Best Of", "SketchUp"]
tags: []
excerpt: "Creating your own Augmented Reality is, thanks to ARTAG, staggeringly easy. Yet behind the simplicity lays a serious potential for both the hobbyist, local government use and the professional…"
hero: "/assets/uploads/external/2.bp.blogspot.com/_ADwvfqkxChw/RpdPxRqXbbI/AAAAAAAAAcw/mJ2kl-MyNCo/s200/Capture.JPG"
---

<p>Creating your own Augmented Reality is, thanks to ARTAG, staggeringly easy. Yet behind the simplicity lays a serious potential for both the hobbyist, local government use and the professional practice.<br />
The only requirements are a webcam, printer and the ability to export models in either .obj, .wrl or .ase formats. As such if you have a model in SketchUp, 3DMax or any other common 3D package you can now view it on your desk using Augmented Reality.<br />
<span style="font-weight: bold;">Step 1</span><br />
<a href="http://iit-iti.nrc-cnrc.gc.ca/license/info_e/8">Download ARTag</a> and unzip the contents to a folder. We generally use the desktop for easy access. Note the SDK kit is currently required as the demo on the main ARTag site has timed out. The contents are however mostly the same.<br />
<span style="font-weight: bold;">Step 2</span><br />
Open your newly created folder - in our case under its default name of 'artag_rev2k_sdk_windows_1207' and navigate to the 'patterns' directory.<br />
<span style="font-weight: bold;">Step 3</span><br />
<a href="http://2.bp.blogspot.com/_ADwvfqkxChw/RpdPxRqXbbI/AAAAAAAAAcw/mJ2kl-MyNCo/s1600-h/Capture.JPG"><img id="BLOGGER_PHOTO_ID_5086622012111547826" style="margin: 0pt 0pt 10px 10px; float: right; cursor: pointer;" src="/assets/uploads/external/2.bp.blogspot.com/_ADwvfqkxChw/RpdPxRqXbbI/AAAAAAAAAcw/mJ2kl-MyNCo/s200/Capture.JPG" alt="" border="0" /></a>Open both base0.gif and toolbar0_7.gif as pictured to the right. Print our each of these .gifs making sure that your print options are set to 'scale to fit media' with either A4 or A3 paper (or your standard printers paper size).<br />
Lay both these printouts side by side on your desk or workspace.<br />
<span style="font-weight: bold;">Step 4</span><br />
Making sure your webcam is plugged in navigate to the 'compiled_demos' folder and double click on 3d_augmentations_usb.exe. This will launch a window in which the view from your webcam is displayed. If you move your cam towards the two marker sheets you printed out a series of 3D models will appear - as pictured below:<br />
<a href="http://2.bp.blogspot.com/_ADwvfqkxChw/RpdSxRqXbcI/AAAAAAAAAc4/bn1vKstkMR4/s1600-h/demo..jpg"><img id="BLOGGER_PHOTO_ID_5086625310646431170" style="margin: 0px auto 10px; display: block; text-align: center; cursor: pointer;" src="/assets/uploads/external/2.bp.blogspot.com/_ADwvfqkxChw/RpdSxRqXbcI/AAAAAAAAAc4/bn1vKstkMR4/s400/demo..jpg" alt="" border="0" /></a><br />
This is your first example of Augmented Reality, all we need now is to import our own objects.<br />
<span style="font-weight: bold;">Step 5</span><br />
The objects that load on the marker grid are defined by a text file - setup_artag_3d.cfg. Open this file in a text editor such as Notepad.<br />
<a href="http://1.bp.blogspot.com/_ADwvfqkxChw/RpdU5BqXbdI/AAAAAAAAAdA/DQ4ni1ViH_o/s1600-h/Capture1.JPG"><img id="BLOGGER_PHOTO_ID_5086627642813672914" style="margin: 0pt 10px 10px 0pt; float: left; cursor: pointer;" src="/assets/uploads/external/1.bp.blogspot.com/_ADwvfqkxChw/RpdU5BqXbdI/AAAAAAAAAdA/DQ4ni1ViH_o/s320/Capture1.JPG" alt="" border="0" /></a> Pictured left we have highlighted the main line in setup_artag_3d.cfg. This defines the file to display on the main marker sheet, in the case of the first demonstration a fish.<br />
To load your own objects you simply change this line to your files name and extension. For the movie below we made a simple windfarm in 3D Studio Max and exported both the textures (in .jpg format) and the file in .ASE format to the 'compiled_demos' folder. We then edited fish.obj to in our case windfarm.ase and saved the file.<br />
Relaunching 3d_augmentations_usb.exe loads the changed file as illustrated in the Youtube movie below:<br />
<center><object width="425" height="350" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="wmode" value="transparent" /><param name="src" value="http://www.youtube.com/v/lz96zndmr9k" /><embed width="425" height="350" type="application/x-shockwave-flash" src="http://www.youtube.com/v/lz96zndmr9k" wmode="transparent" /></object></center>It is worth experimenting with a variety of objects with the system - a 3D Earth model works particularly well and has obvious applications for the teaching of geography in a classroom environment, especially if you print out the marker sheet in A1 size.<br />
For more detailed info take a look at the <a href="http://www.artag.net/">ARTag site</a>.<br />
Let us know if you hit any problems or require any further tips..<br />
*<br />
Update 17th July 2007<br />
As requested we have uploaded a sample .obj to load into the directory as a test for replacing the supplied 3d models in the demo. Download and unzip to the compiled demos directory the following file <a href="http://www.casa.ucl.ac.uk/andy/Globe.zip">Globe.zip</a> (542K).<br />
The zip contains three files - Globe.obj, Globe.mtl and the texture in .jpg format - is this case a panoramic image.<br />
Replace fish.obj with Globe.obj as per Step 5 and you should see a globe panorama on the main base0 maker sheet.</p>
