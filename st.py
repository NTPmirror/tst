from flask import Flask, render_template_string

app = Flask(__name__)

# HTML и CSS прямо в переменной
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DietPi Test Server</title>
    <style>
        body {
            background: radial-gradient(circle, #1a1a1a 0%, #000000 100%);
            color: #ffffff;
            font-family: 'Courier New', monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        .card {
            border: 2px solid #00ff41;
            padding: 40px;
            background: rgba(0, 255, 65, 0.05);
            box-shadow: 0 0 20px rgba(0, 255, 65, 0.2);
            text-align: center;
            border-radius: 5px;
        }
        h1 {
            color: #00ff41;
            text-transform: uppercase;
            letter-spacing: 5px;
            margin: 0 0 20px 0;
            font-size: 2em;
        }
        .status-box {
            background: #00ff41;
            color: #000;
            padding: 10px 20px;
            font-weight: bold;
            display: inline-block;
            margin-top: 20px;
        }
        .info {
            color: #888;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>System Online</h1>
        <p>Ваш сервер на DietPi успешно транслирует эту страницу.</p>
        <p class="info">Порт: 8081 | Протокол: HTTP/2 (via Cloudflare)</p>
        <div class="status-box">CONNECTION: SECURE</div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Слушаем только локально, чтобы cloudflared забирал трафик
    app.run(host='127.0.0.1', port=8081)
