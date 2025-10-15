from datetime import datetime

import pytz
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""
    <html>
        <head>
            <title>Тестовое приложение</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f0f2f5;
                    color: #333;
                    margin: 0;
                }}
                .container {{
                    text-align: center;
                    padding: 40px;
                    border-radius: 10px;
                    background-color: #fff;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                }}
                h1 {{
                    color: #0056b3;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <p>Текущее время: {current_time}</p>
            </div>
        </body>
    </html>
    """
    return html_content


if __name__ == "__main__":
    app.run(debug=True)
