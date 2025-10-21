from datetime import datetime

import pytz
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(tz)

    html_content = f"""
    <html>
        <head>
            <title>тестовое приложение</title>
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
                    background-color: #111;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                }}
                h1 {{
                    color: #28a745;
                }}
                #time {{
                    font-weight: bold;
                    font-size: 5.2em;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <p>Текущее время: <span id="time"></span></p>
            </div>

            <script>
                let serverTime = new Date("{current_time.isoformat()}");

                function updateTime() {{
                    serverTime.setSeconds(serverTime.getSeconds() + 1);

                    let hours = serverTime.getHours().toString().padStart(2, '0');
                    let minutes = serverTime.getMinutes().toString().padStart(2, '0');
                    let seconds = serverTime.getSeconds().toString().padStart(2, '0');
                    let timeString = `${{hours}}:${{minutes}}:${{seconds}}`;
                    
                    document.getElementById('time').textContent = timeString;
                }}

                setInterval(updateTime, 1000);
                
                updateTime(); 
            </script>
        </body>
    </html>
    """
    return html_content
