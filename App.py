from flask import Flask

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>HACKED</title>

<style>
body {
    margin: 0;
    background: black;
    overflow: hidden;
    font-family: monospace;
    color: #00ff00;
}

canvas {
    position: fixed;
    top: 0;
    left: 0;
}

.container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}
.glitch {
    font-size: 60px;
    color: red;
    position: relative;
    animation: glitch 1s infinite;
}

@keyframes glitch {
    0% { text-shadow: 2px 2px red; }
    20% { text-shadow: -2px -2px lime; }
    40% { text-shadow: 2px -2px red; }
    60% { text-shadow: -2px 2px lime; }
    80% { text-shadow: 2px 2px red; }
    100% { text-shadow: -2px -2px lime; }
}

.typing {
    font-size: 20px;
    border-right: 2px solid #00ff00;
    white-space: nowrap;
    overflow: hidden;
    width: 0;
    animation: typing 4s steps(40, end) forwards, blink 1s infinite;
}

@keyframes typing {
    from { width: 0 }
    to { width: 350px }
}

@keyframes blink {
    50% { border-color: transparent }
}
</style>
</head>

<body>

<canvas id="matrix"></canvas>

<div class="container">
    <div class="glitch">HACKED</div>
    <div class="typing">keneviz was fucked</div>
</div>

<script>
const canvas = document.getElementById("matrix");
const ctx = canvas.getContext("2d");

canvas.height = window.innerHeight;
canvas.width = window.innerWidth;

let letters = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ";
letters = letters.split("");

let fontSize = 14;
let columns = canvas.width / fontSize;

let drops = [];
for (let x = 0; x < columns; x++)
    drops[x] = 1;

function draw() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0F0";
    ctx.font = fontSize + "px monospace";

    for (let i = 0; i < drops.length; i++) {
        let text = letters[Math.floor(Math.random() * letters.length)];
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);

        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975)
            drops[i] = 0;

        drops[i]++;
    }
}

setInterval(draw, 33);
</script>

</body>
</html>"""

@app.route("/")
def index():
    return HTML

if __name__ == "__main__":
    app.run(debug=True)
