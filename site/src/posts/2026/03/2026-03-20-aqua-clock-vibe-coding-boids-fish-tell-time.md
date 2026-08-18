---
title: "Aqua Clock: Multi-Model Vibe Coding, Boids, and the Fish That Tell the Time"
date: 2026-03-20 09:00:00
slug: "aqua-clock-vibe-coding-boids-fish-tell-time"
permalink: "/blog/2026/03/20/aqua-clock-vibe-coding-boids-fish-tell-time/"
author: "Andy"
categories: ["Making"]
tags: ["ai", "vibe coding", "boids", "clock", "ios", "agent based modelling"]
excerpt: "How an experiment in agent-based fish simulation, vibe coded with Claude and Gemini AI Studio, became a clock — and ended up on the Apple App Store."
hero: "/assets/uploads/imported/connected-environments.org/assets/img/blog/202603-aqua-clock/aqua_clock_aquarium_header.png"
original: "https://connected-environments.org/blog/2026-03-20-aqua-clock-vibe-coding-boids-fish-tell-time/"
---

<figure><img src="/assets/uploads/imported/connected-environments.org/assets/img/blog/202603-aqua-clock/aqua_clock_aquarium_header.png" alt="Aqua Clock" /></figure>

<p><strong>An Aquairum, published into the Apple Store, that tells the time was never the plan.</strong> The plan was to explore the use of the latest AI tools to develop agent based models with the aim to use those models to display data feeds. It turned into its own unique app where the fish (the aqents) gather every minute to tell the time - Aqua Clock.</p>

<p>Aqua Clock began as a loose experiment, in between writing a paper on the ‘Phygital City’. It aimed to explore how to build an agent-based simulation entirely through conversational AI — no design document, no formal spec, just an open-ended dialogue and a canvas to draw on? The fish came first as the boids algorithm is a natural first step. The idea of the clock came mid break from the paper and it was so nice, the release into the The App Store came next.</p>

<figure>
  <img src="/assets/uploads/imported/connected-environments.org/assets/img/blog/202603-aqua-clock/aqua_clock_launch_square.png" alt="Aqua Clock launch poster" />
  <figcaption>Aqua Clock: where the fish tell the time — <a href="https://apps.apple.com/gb/app/aqua-clock/id6760460959">Download on the App Store</a></figcaption>
</figure>

## What is Vibe Coding?

<p>Vibe coding is now a common term, but the tools are moving rapidly and to keep on top of developments its good to take a fresh look at the workflows every could of months. Rather than writing code to meet a brief, its a processes of iterating through ideas, accepting suggestions, discarding others, and allowing the final artefact to emerge from the generative process itself. Its like have a computer scientish on hand, where you discuss ideas and they go off and build things.</p>

<p>There is no requirements document, no architecture diagram drawn in advance, no sprint backlog. There is a conversation — often exploratory, sometimes surprising — between a human an AI system with broad technical knowledge. Its a new an emerging world of developing apps and in many ways it frees up creativity.</p>

## Its all about the Boids

<p>The project started with a classic problem in computational simulation: how do you model the collective, emergent behaviour of a group of agents following simple local rules? Craig Reynolds’ <em>boids</em> algorithm, first published in 1987, remains the canonical answer. Three steering rules — <strong>separation</strong> (avoid crowding neighbours), <strong>alignment</strong> (steer toward the average heading of neighbours), and <strong>cohesion</strong> (steer toward the average position of neighbours) — produce uncannily lifelike flocking behaviour from agents with no global awareness of the group.</p>

<figure><img src="/assets/uploads/imported/connected-environments.org/assets/img/blog/202603-aqua-clock/aquaclockboids.png" alt="Boids in the Aquarium" /><figcaption>Boids in the Aquarium</figcaption></figure>

<p>The original goal was modest: Claude (we used both Claude and Gemini during the developement) was prompted with an open-ended invitation: <em>let’s build a fish tank with flocking fish</em>. What followed was a series of exchanges in which the AI generated, explained, and iteratively refined a TypeScript/React simulation rendered on an HTML5 Canvas. Ghost shrimp, snails, a crab, bubbles, and drifting plants were added over successive sessions. The result was a convincing living aquarium — aesthetically pleasing, behaviourally rich, and computationally lightweight at under 11 MB. AI systems have ‘token’ limits on use and the development of the app took a series of back and forth flows between Gemini and Claude, which we detail in the next section.</p>

<p>At this point, the project had no clock, just a nice living aquarium where the plants grow over time and the fish school together, as planned.</p>

## The Creative Pivot: Fish as Time Display

<p>The idea emerged, as many good ones do, from a tangential observation mid-session. The tetra fish — small, numerous, 28 in the final implementation — could in principle be choreographed to form recognisable shapes. Seven-segment displays, the kind used in digital clocks and calculators since the 1960s, are composed of straight line segments. Fish swimming in formation along those segments could render digits legibly. Regular readers of my site over at digitalurban.org will know i have a ‘thing’ about clocks, physcial and digital.</p>

<p>This is the core design insight of Aqua Clock: <strong>the fish are not decorative, they are functional.</strong> Every minute, the 28 tetra fish abandon their emergent flocking behaviour and are assigned target positions along the seven-segment outlines of four digits representing HH:MM. They swim to those positions, hold formation, then dissolve back into free flocking. The transition — fish departing their natural behaviour to form the time and then dispersing — is itself a kind of performance, observable in real time.</p>

<p>A double-tap gesture summons the time on demand, holding the formation for seven seconds before releasing the fish. Single-tap drops food pellets the fish chase and consume. Pinch and scroll adjust water brightness. An optional ambient underwater soundscape plays in the background.</p>

<p>None of these features were in a specification. Each one emerged from the conversation.</p>

## A Dual-AI Workflow with GitHub at the Centre

<p>One of the core aspects of this project was its use of two distinct AI systems in alternating roles, with GitHub as the shared substrate between them.</p>

<figure><img src="/assets/uploads/imported/connected-environments.org/assets/img/blog/202603-aqua-clock/aqua_clock_workflow.png" alt="The dual-AI workflow with GitHub at the centre" /><figcaption>The dual-AI workflow with GitHub at the centre</figcaption></figure>

<p><strong>Claude</strong> handled the heavier architectural work — the initial boids implementation, the entity system (<code>VectorFish</code>, <code>GhostShrimp</code>, <code>Snail</code>, <code>Crab</code>, <code>Bubble</code>, <code>Food</code>), the canvas rendering pipeline, and the seven-segment clock logic. Claude’s strength in this context was its ability to hold a large codebase in working context and reason about the interactions between components.</p>

<p><strong>Gemini AI Studio</strong> was brought in at points where a fresh perspective was useful — reviewing code for performance issues, suggesting interaction patterns, and providing an independent read on the user experience. Critically, Gemini operated from the code as it existed in GitHub at each handoff: the repository served as a shared ground truth that neither AI system owned, and that both could read.</p>

<p>GitHub, in this model, is not merely version control — it is <strong>the handoff protocol</strong>. Committing code to the repository creates a durable, readable artefact that can be passed to a different AI system without loss of context. Each commit is, in effect, a message in a conversation between two AI interlocutors mediated by a human developer who understands both.</p>

<p>This is a pattern worth naming: <strong>multi-model vibe coding</strong>, in which different LLMs contribute distinct perspectives to a shared codebase, with version control as the neutral interchange format.</p>

## Under the Hood

<p>The final application is built on a deliberately lightweight stack:</p>

<ul>
<li><strong>React + TypeScript</strong> for component architecture and state management</li>
<li><strong>Vite</strong> as the build tool, chosen for fast hot module replacement during iterative sessions</li>
<li><strong>HTML5 Canvas API</strong> for all rendering — no WebGL, no external graphics library</li>
<li><strong>Capacitor</strong> for iOS packaging — the web application wrapped in a native iOS container, no Swift written by hand</li>
</ul>

<p>Battery efficiency was a deliberate concern. The animation loop uses <code>requestAnimationFrame</code> with frame-rate throttling, and its suspends entirely via the <code>visibilitychange</code> API when the app is backgrounded. The bubble simulation is capped at 150 active bubbles to prevent unbounded growth at high air pump settings.</p>

<p>The fish themselves are roughly 50 lines of simulation logic per entity per frame — position update, velocity update, boids force accumulation, wall steering, food steering, and clock-formation steering when active. The emergent complexity of the aquarium arises from the interaction of these simple rules across 28+ fish, not from any global choreography system.</p>

## Deployment: From Browser to App Store

<p><em>Capacitor</em>, developed by Ionic, bridges web applications to native mobile platforms. The build process was:</p>

<ol>
<li><code>npm run build</code> — Vite compiles the React/TypeScript application to a static web bundle</li>
<li><code>npx cap sync ios</code> — Capacitor copies the bundle into an Xcode project scaffold</li>
<li>Xcode — the compiled app is signed and submitted to Apple’s App Store Connect</li>
</ol>

<p>The entire application logic — including all simulation code — runs in TypeScript inside a WKWebView on iOS. The app is 10.5 MB, requires iOS 15.0 or later, and is compatible with iPhone, iPad and Mac (Apple Silicon).</p>

<p>The absence of native Swift code in the application layer is itself a product of the vibe coding approach: when the AI generates web technology natively, and Capacitor wraps it for distribution, the boundary between “web app” and “native app” dissolves in ways that would have seemed implausible even a year ago. The development of an app to the store is so short that a rise in ‘app abandonment’ is probable, where its so easy to make an publish apps that ‘developers’ (maybe that term now needs a new name) rapidly move onto the next thing.</p>

## What Vibe Coding Reveals

<p><em>Aqua Clock</em> would not exist without vibe coding — not because the underlying techniques are beyond a skilled developer, but because <strong>no specification for it would ever have been written</strong>. The combination of a living aquarium with a fish-formation clock is an idea that emerges from the process of making, not from planning.</p>

<p>This is what vibe coding offers: a mode of creative-technical practice in which the act of building is also the act of discovery. The AI does not replace the developer; it accelerates iteration to a pace at which exploration becomes viable. Ideas that would require days to prototype can be tested in hours.</p>

<p>The dual-AI workflow introduces a further dimension: different models bring different tendencies. Using Claude and Gemini in alternating roles — with GitHub as the neutral handoff — introduces a productive form of creative friction, analogous to showing a half-finished painting to a different critic at each stage.</p>

<p>What remains irreducibly human in this process is <strong>aesthetic judgement</strong>: the decision that fish should form a clock, that the transition between modes should be visible and unhurried, that the aquarium should feel inhabited rather than mechanical. The AI provided the means; the human provided the meaning.</p>

## City Clock - The City where the People Tell the Time

<p>Of course the majority of our work is concerned with cities and the concept extends in a City where the People Tell the Time - as such City Clock is under development (its almost complete) and will be incoming to the Apple Store soon…</p>

<figure><img src="/assets/uploads/imported/connected-environments.org/assets/img/blog/202603-aqua-clock/cityclock.png" alt="City Clock" /><figcaption>City Clock</figcaption></figure>

## Download it

<p><em>Aqua Clock</em> is free on the Apple App Store for iPhone, iPad, and Mac. An Android version is incoming, probably ‘developed’ during a break on a book chapter i need to complete next week…</p>

<p><a href="https://apps.apple.com/gb/app/aqua-clock/id6760460959">Download on the App Store</a></p>

<p><em>First published on <a href="https://connected-environments.org/blog/2026-03-20-aqua-clock-vibe-coding-boids-fish-tell-time/">UCL Connected Environments</a>.</em></p>
