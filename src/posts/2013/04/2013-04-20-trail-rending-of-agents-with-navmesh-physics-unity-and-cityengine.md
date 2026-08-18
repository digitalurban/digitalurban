---
title: "Trail Rending of Agents with NavMesh, Physics, Unity and CityEngine"
date: 2013-04-20 09:05:27
slug: "trail-rending-of-agents-with-navmesh-physics-unity-and-cityengine"
permalink: "/blog/2013/04/20/trail-rending-of-agents-with-navmesh-physics-unity-and-cityengine/"
author: "Andy"
categories: ["Posts"]
tags: []
excerpt: "Combining simple agent based models with physics objects and rendering techniques in a game engine has potential for city wide 3D urban modelling. Traditional techniques often use JAVA based…"
hero: "/assets/uploads/2013/04/Screen-Shot-2013-04-20-at-10.04.10-1.png"
---

Combining simple agent based models with physics objects and rendering techniques in a game engine has potential for city wide 3D urban modelling. Traditional techniques often use JAVA based solutions or custom written toolkits with researchers developing their own models. With recent advances in procedural modelling and game engine technology, with the move to real time data feeds and advanced physics engines, there is notable potential.
<figure><a href="/assets/uploads/2013/04/Screen-Shot-2013-04-20-at-10.04.10-1.png"><img class=" wp-image-3330 " alt="Trail Render in Unity" src="/assets/uploads/2013/04/Screen-Shot-2013-04-20-at-10.04.10-1.png" width="646" height="313" /></a><figcaption>Trail Render in Unity</figcaption></figure>
Yesterday's post on '<a href="http://www.digitalurban.org/2013/04/shortest-path-modelling-and-navmesh-in-unity-and-cityengine.html">Shortest Path Modelling and NavMesh in Unity and CityEngine</a>' explored a simple target/navmesh approach. If you add physics to the target and use the 'trail rendering' effects of Unity you can create a dynamic scene with the paths of the agents traced. It is of course exploratory, but the possibilities are intriguing:
<center><iframe src="http://www.youtube.com/embed/mGUrHK3v-ws" height="360" width="640" allowfullscreen="" frameborder="0"></iframe></center>The Trail Renderer is simply used to make trails behind objects in the scene as they move about - with the addition of physics the ball reacts to the mesh and the agents are continuously calculating a shortest path. This is computationally intensive so a question remains on the number of agents Unity can handle in a single simulation, we will be exploring this over the coming weeks.
