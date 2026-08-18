---
title: "Enhancing Live Weather Monitoring with MQTT and Chart.js"
date: 2024-06-27 15:10:06
slug: "enhancing-live-weather-monitoring-with-mqtt-and-chart-js"
permalink: "/blog/2024/06/27/enhancing-live-weather-monitoring-with-mqtt-and-chart-js/"
author: "Andy"
categories: ["data", "Data Visualisation", "Weather", "Weather (Live)", "Weather Display"]
tags: ["Data", "mqtt", "Weather"]
excerpt: "Introduction Viewing real-time data from a personal weather station such as a Davis Vantage Pro, a Tempest, or an EcoWhitt device can be complex. However, the majority of systems that process weather…"
hero: "/assets/uploads/2024/06/Screenshot-2024-06-27-at-15.48.35.png"
---

<h2></h2>
<h3>Introduction</h3>
Viewing real-time data from a personal weather station such as a Davis Vantage Pro, a Tempest, or an EcoWhitt device can be complex. However, the majority of systems that process weather data, such as Weather Display, Weewx, or CumlusMx, all have the ability to output MQTT data. This data can be used to display a real-time graph of the data, keeping you engaged with the latest weather updates, and supplemented with any other data which is MQTT-based.

<p>With this in mind, we've developed a live weather monitoring dashboard as an illustrative example. This dashboard uses MQTT for real-time data updates and Chart.js for dynamic visualization. We've also included a visual indicator for connection status and a brief pulse effect to notify when new data arrives, enhancing the user experience.</p>

<p><img class=" wp-image-7820 aligncenter" src="/assets/uploads/2024/06/Screenshot-2024-06-27-at-15.48.35-300x185.png" alt="MQTT Weather Dashboard" width="600" height="370" /></p>

<p>You can view it live at: <a href="https://finchamweather.co.uk/weathergraph.htm">https://finchamweather.co.uk/weathergraph.htm</a></p>

<p>The data populates as the page loads - we could of course back load it via a database link, but the aim was to simply use MQTT and have a graphing system that streams in data, its a work in progress but here is how we got it working:<br />
<h3>Setting Up the Environment</h3><br />
Before we dive into the code, ensure you have the following libraries included in your HTML:<br />
<ul><br />
 	<li>Paho MQTT: for MQTT protocol handling - our MQTT feed is open to use as a test, replace this with your own MQTT details in the main code.</li><br />
 	<li>Chart.js: for creating dynamic charts</li><br />
 	<li>Chart.js adapter for date-fns: for handling time scales in charts</li><br />
</ul><br />
<h3>Initial HTML Setup</h3><br />
We'll start by setting up the basic HTML structure. This includes elements for displaying the connection status, forecast, weather statistics, and the weather chart.<br />
<pre><code>&lt;!DOCTYPE html&gt;<br />
&lt;html lang="en"&gt;<br />
&lt;head&gt;<br />
    &lt;meta charset="UTF-8"&gt;<br />
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;<br />
    &lt;meta name="apple-mobile-web-app-capable" content="yes"&gt;<br />
    &lt;meta name="apple-mobile-web-app-status-bar-style" content="black"&gt;<br />
    &lt;title&gt;Live Weather Graph&lt;/title&gt;<br />
    &lt;script src="https://cdnjs.cloudflare.com/ajax/libs/paho-mqtt/1.0.1/mqttws31.js"&gt;&lt;/script&gt;<br />
    &lt;script src="https://cdn.jsdelivr.net/npm/chart.js"&gt;&lt;/script&gt;<br />
    &lt;script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"&gt;&lt;/script&gt;<br />
    &lt;style&gt;<br />
        body {<br />
            font-family: Arial, sans-serif;<br />
            margin: 20px;<br />
        }<br />
        #mqttStatus {<br />
            margin-bottom: 20px;<br />
            text-align: left;<br />
            font-size: 1.2em;<br />
        }<br />
        .dot {<br />
            height: 20px;<br />
            width: 20px;<br />
            border-radius: 50%;<br />
            display: inline-block;<br />
        }<br />
        .green {<br />
            background-color: green;<br />
        }<br />
        .red {<br />
            background-color: red;<br />
        }<br />
        .orange {<br />
            background-color: orange;<br />
        }<br />
        .pulse-once {<br />
            animation: pulse-once 1s;<br />
        }<br />
        @keyframes pulse-once {<br />
            0% { transform: scale(1); }<br />
            50% { transform: scale(1.2); }<br />
            100% { transform: scale(1); }<br />
        }<br />
        #forecast {<br />
            margin-bottom: 20px;<br />
            text-align: left;<br />
            font-size: 1.2em;<br />
            font-weight: bold;<br />
        }<br />
        #stats {<br />
            display: flex;<br />
            justify-content: center;<br />
            gap: 20px;<br />
            margin-bottom: 20px;<br />
            font-size: 1.2em;<br />
            font-weight: bold;<br />
        }<br />
        #stats div {<br />
            padding: 10px 20px;<br />
            border: 1px solid #ccc;<br />
            border-radius: 8px;<br />
            box-shadow: 2px 2px 12px #aaa;<br />
            background-color: #f9f9f9;<br />
        }<br />
        canvas {<br />
            border: 1px solid #ccc;<br />
            box-shadow: 2px 2px 12px #aaa;<br />
        }<br />
    &lt;/style&gt;<br />
&lt;/head&gt;<br />
&lt;body&gt;<br />
    &lt;div id="mqttStatus"&gt;&lt;span id="connectionDot" class="dot red"&gt;&lt;/span&gt; mqtt: disconnected&lt;/div&gt;<br />
    &lt;div id="forecast"&gt;Forecast: Loading...&lt;/div&gt;<br />
    &lt;div id="stats"&gt;<br />
        &lt;div id="maxWindSpeed"&gt;Max Wind Speed: 0 mph&lt;/div&gt;<br />
        &lt;div id="maxTemp"&gt;Max Temperature: 0 °C&lt;/div&gt;<br />
        &lt;div id="minTemp"&gt;Min Temperature: 0 °C&lt;/div&gt;<br />
        &lt;div id="maxPressure"&gt;Max Pressure: 0 mbar&lt;/div&gt;<br />
        &lt;div id="minPressure"&gt;Min Pressure: 0 mbar&lt;/div&gt;<br />
    &lt;/div&gt;<br />
    &lt;canvas id="weatherChart" width="800" height="400"&gt;&lt;/canvas&gt;<br />
&lt;/body&gt;<br />
&lt;/html&gt;<br />
</code></pre><br />
<h3>Connecting to MQTT</h3><br />
Next, we set up the MQTT connection. The MQTT client will connect to the broker, subscribe to the necessary topics, and handle messages when they arrive.<br />
<pre><code>// MQTT connection settings<br />
var mqtt;<br />
var reconnectTimeout = 2000;<br />
var host = "mqtt.cetools.org";<br />
var port = location.protocol === 'https:' ? 8081 : 8080;<br />
var options = {<br />
    timeout: 3,<br />
    onSuccess: onConnect,<br />
    onFailure: onFailure,<br />
    useSSL: location.protocol === 'https:',<br />
};<br />
var clientID = "clientID" + parseInt(Math.random() * 100);</p>

<p>function updateConnectionStatus(status) {<br />
    const dot = document.getElementById("connectionDot");<br />
    if (status === "connected") {<br />
        dot.className = "dot green";<br />
        document.getElementById("mqttStatus").innerHTML = `&lt;span class="dot green" id="connectionDot"&gt;&lt;/span&gt; mqtt: connected`;<br />
    } else if (status === "disconnected") {<br />
        dot.className = "dot red";<br />
        document.getElementById("mqttStatus").innerHTML = `&lt;span class="dot red" id="connectionDot"&gt;&lt;/span&gt; mqtt: disconnected`;<br />
    } else if (status === "reconnecting") {<br />
        dot.className = "dot orange";<br />
        document.getElementById("mqttStatus").innerHTML = `&lt;span class="dot orange" id="connectionDot"&gt;&lt;/span&gt; mqtt: reconnecting`;<br />
    }<br />
}</p>

<p>function pulseDot() {<br />
    const dot = document.getElementById("connectionDot");<br />
    dot.classList.add("pulse-once");<br />
    setTimeout(() =&gt; {<br />
        dot.classList.remove("pulse-once");<br />
    }, 1000); // Duration of the pulse-once animation<br />
}</p>

<p>function onFailure(message) {<br />
    console.log("Connection Attempt to Host " + host + " Failed: ", message.errorMessage);<br />
    updateConnectionStatus("disconnected");<br />
    setTimeout(MQTTconnect, reconnectTimeout);<br />
}</p>

<p>function onConnect() {<br />
    console.log("Connected ");<br />
    updateConnectionStatus("connected");<br />
    mqtt.subscribe("personal/ucfnaps/downhamweather/loop");<br />
    mqtt.subscribe("personal/ucfnaps/eink/met");<br />
}</p>

<p>function MQTTconnect() {<br />
    console.log("Connecting to " + host + " on port " + port);<br />
    updateConnectionStatus("reconnecting");<br />
    mqtt = new Paho.MQTT.Client(host, port, clientID);<br />
    mqtt.onMessageArrived = onMessageArrived;<br />
    mqtt.onConnectionLost = function(responseObject) {<br />
        if (responseObject.errorCode !== 0) {<br />
            console.log("Connection Lost: " + responseObject.errorMessage);<br />
            updateConnectionStatus("disconnected");<br />
            setTimeout(MQTTconnect, reconnectTimeout);  // Attempt to reconnect<br />
        }<br />
    };<br />
    mqtt.connect(options);<br />
}</p>

<p>window.onload = function() {<br />
    MQTTconnect();<br />
}<br />
</code></pre><br />
<h3>Handling Incoming Messages</h3><br />
When messages arrive, we process the data and update the chart. We also update the connection dot to pulse briefly, indicating new data has been received.<br />
<pre><code>let lastUpdate = Date.now();  // Initialize to current time<br />
let firstUpdate = true;  // Flag to ensure first update happens immediately</p>

<p>let maxWindSpeed = 0;<br />
let maxTemp = -Infinity;<br />
let minTemp = Infinity;<br />
let maxPressure = -Infinity;<br />
let minPressure = Infinity;</p>

<p>function updateWindSpeed(windSpeed, timestamp) {<br />
    weatherChart.data .labels.push(timestamp);<br />
    weatherChart.data.datasets[0].data.push(windSpeed);</p>

<p>// Update max wind speed<br />
    if (windSpeed &gt; maxWindSpeed) {<br />
        maxWindSpeed = windSpeed;<br />
        document.getElementById('maxWindSpeed').innerText = `Max Wind Speed: ${maxWindSpeed} mph`;<br />
    }</p>

<p>// Limit the number of data points to keep the chart responsive<br />
    if (weatherChart.data.labels.length &gt; 1440) { // Assuming 1 data point per minute, keep 24 hours of data<br />
        weatherChart.data.labels.shift();<br />
        weatherChart.data.datasets[0].data.shift();<br />
    }</p>

<p>weatherChart.update();<br />
}</p>

<p>function updateOtherMetrics(temperature, solarRadiation, rainAmount, pressure, timestamp) {<br />
    weatherChart.data.datasets[1].data.push({x: timestamp, y: temperature});<br />
    weatherChart.data.datasets[2].data.push({x: timestamp, y: solarRadiation});<br />
    weatherChart.data.datasets[3].data.push({x: timestamp, y: rainAmount &gt; 0 ? rainAmount : null});<br />
    weatherChart.data.datasets[4].data.push({x: timestamp, y: pressure});</p>

<p>// Update max and min temperature<br />
    if (temperature &gt; maxTemp) {<br />
        maxTemp = temperature;<br />
        document.getElementById('maxTemp').innerText = `Max Temperature: ${maxTemp} °C`;<br />
    }<br />
    if (temperature &lt; minTemp) { minTemp = temperature; document.getElementById('minTemp').innerText = `Min Temperature: ${minTemp} °C`; } // Update max and min pressure if (pressure &gt; maxPressure) {<br />
        maxPressure = pressure;<br />
        document.getElementById('maxPressure').innerText = `Max Pressure: ${maxPressure} mbar`;<br />
    }<br />
    if (pressure &lt; minPressure) { minPressure = pressure; document.getElementById('minPressure').innerText = `Min Pressure: ${minPressure} mbar`; } // Limit the number of data points to keep the chart responsive if (weatherChart.data.labels.length &gt; 1440) { // Assuming 1 data point per minute, keep 24 hours of data<br />
        weatherChart.data.datasets[1].data.shift();<br />
        weatherChart.data.datasets[2].data.shift();<br />
        weatherChart.data.datasets[3].data.shift();<br />
        weatherChart.data.datasets[4].data.shift();<br />
    }</p>

<p>weatherChart.update();<br />
}</p>

<p>function updateForecast(forecast) {<br />
    document.getElementById('forecast').innerText = `Forecast: ${forecast}`;<br />
}</p>

<p>function onMessageArrived(message) {<br />
    console.log("Message Arrived: " + message.destinationName + " : " + message.payloadString);<br />
    if (message.destinationName === "personal/ucfnaps/downhamweather/loop") {<br />
        const data = JSON.parse(message.payloadString);<br />
        const windSpeed = data['windSpeed_mph'];  // Adjust this key according to your data structure<br />
        const temperature = data['outTemp_C'];  // Adjust this key according to your data structure<br />
        const solarRadiation = data['radiation_Wpm2'];  // Adjust this key according to your data structure<br />
        const rainAmount = data['dayRain_mm'];  // Adjust this key according to your data structure<br />
        const pressure = data['pressure_mbar'];  // Adjust this key according to your data structure</p>

<p>const nowTimestamp = new Date();</p>

<p>// Update wind speed every time<br />
        updateWindSpeed(windSpeed, nowTimestamp);</p>

<p>if (firstUpdate || Date.now() - lastUpdate &gt;= 60000) {<br />
            // Update other metrics every minute<br />
            updateOtherMetrics(temperature, solarRadiation, rainAmount, pressure, nowTimestamp);<br />
            lastUpdate = Date.now();<br />
            firstUpdate = false;  // Ensure subsequent updates follow the interval<br />
        }</p>

<p>// Pulse the dot when new data arrives<br />
        pulseDot();<br />
    } else if (message.destinationName === "personal/ucfnaps/eink/met") {<br />
        const forecast = message.payloadString;<br />
        updateForecast(forecast);<br />
    }<br />
}<br />
</code></pre><br />
<h3>Chart.js Setup</h3><br />
Now, let's configure Chart.js to visualize the weather data. We will use multiple datasets to display wind speed, temperature, solar radiation, rain amount, and pressure.<br />
<pre><code>// Chart.js setup<br />
const ctx = document.getElementById('weatherChart').getContext('2d');<br />
const weatherChart = new Chart(ctx, {<br />
    type: 'line',<br />
    data: {<br />
        labels: [],  // Time labels<br />
        datasets: [{<br />
            label: 'Wind Speed (mph)',<br />
            data: [],<br />
            borderColor: 'rgba(75, 192, 192, 1)',<br />
            borderWidth: 3,<br />
            fill: false,<br />
            yAxisID: 'y-axis-1',<br />
            tension: 0.1<br />
        },<br />
        {<br />
            label: 'Temperature (°C)',<br />
            data: [],<br />
            borderColor: 'rgba(255, 99, 132, 1)',<br />
            borderWidth: 3,<br />
            fill: false,<br />
            yAxisID: 'y-axis-2',<br />
            tension: 0.1<br />
        },<br />
        {<br />
            label: 'Solar Radiation (W/m²)',<br />
            data: [],<br />
            borderColor: 'rgba(255, 206, 86, 1)',<br />
            borderWidth: 3,<br />
            fill: false,<br />
            yAxisID: 'y-axis-3',<br />
            tension: 0.1<br />
        },<br />
        {<br />
            label: 'Rain Amount (mm)',<br />
            data: [],<br />
            borderColor: 'rgba(54, 162, 235, 1)',<br />
            borderWidth: 3,<br />
            fill: false,<br />
            yAxisID: 'y-axis-4',<br />
            tension: 0.1<br />
        },<br />
        {<br />
            label: 'Pressure (mbar)',<br />
            data: [],<br />
            borderColor: 'rgba(153, 102, 255, 1)',<br />
            borderWidth: 3,<br />
            fill: false,<br />
            yAxisID: 'y-axis-5',<br />
            tension: 0.1<br />
        }]<br />
    },<br />
    options: {<br />
        responsive: true,<br />
        plugins: {<br />
            legend: {<br />
                position: 'top',<br />
            },<br />
            title: {<br />
                display: true,<br />
                text: 'Live Weather Data'<br />
            },<br />
            decimation: {<br />
                enabled: true,<br />
                algorithm: 'lttb',<br />
                samples: 100,  // Adjust this value as needed for performance<br />
            },<br />
        },<br />
        scales: {<br />
            x: {<br />
                type: 'time',<br />
                time: {<br />
                    unit: 'minute'<br />
                },<br />
                title: {<br />
                    display: true,<br />
                    text: 'Time'<br />
                }<br />
            },<br />
            'y-axis-1': {<br />
                type: 'linear',<br />
                position: 'left',<br />
                beginAtZero: true,<br />
                title: {<br />
                    display: true,<br />
                    text: 'Wind Speed (mph)'<br />
                }<br />
            },<br />
            'y-axis-2': {<br />
                type: 'linear',<br />
                position: 'right',<br />
                beginAtZero: true,<br />
                title: {<br />
                    display: true,<br />
                    text: 'Temperature (°C)'<br />
                },<br />
                grid: {<br />
                    drawOnChartArea: false<br />
                }<br />
            },<br />
            'y-axis-3': {<br />
                type: 'linear',<br />
                position: 'right',<br />
                beginAtZero: true,<br />
                title: {<br />
                    display: true,<br />
                    text: 'Solar Radiation (W/m²)'<br />
                },<br />
                grid: {<br />
                    drawOnChartArea: false<br />
                }<br />
            },<br />
            'y-axis-4': {<br />
                type: 'linear',<br />
                position: 'right',<br />
                beginAtZero: true,<br />
                title: {<br />
                    display: true,<br />
                    text: 'Rain Amount (mm)'<br />
                },<br />
                grid: {<br />
                    drawOnChartArea: false<br />
                }<br />
            },<br />
            'y-axis-5': {<br />
                type: 'linear',<br />
                position: 'right',<br />
                beginAtZero: true,<br />
                title: {<br />
                    display: true,<br />
                    text: 'Pressure (mbar)'<br />
                },<br />
                grid: {<br />
                    drawOnChartArea: false<br />
                }<br />
            }<br />
        },<br />
        interaction: {<br />
            intersect: false,<br />
            mode: 'nearest',<br />
        },<br />
        elements: {<br />
            line: {<br />
                cubicInterpolationMode: 'monotone',<br />
            },<br />
        },<br />
    }<br />
});<br />
</code></pre><br />
<h3>Conclusion</h3><br />
By integrating MQTT and Chart.js, it is possible to create a dynamic and real-time weather monitoring dashboard. The connection status indicator provides immediate feedback on the connection state, and the pulsing effect when new data arrives enhances user experience by visually notifying them of updates.</p>

<p>This setup can be further extended by adding more datasets, customizing the chart's appearance, or integrating additional sensors. The data of course couple be from any feed, but real-time weather monitoring provides a good example of how IoT and web technologies can be combined to create realtime dashboards.</p>
