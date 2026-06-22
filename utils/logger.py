from datetime import datetime

def log(message):
    with open("logs/app.log", "a") as file:
        file.write(
            f"{datetime.now()} - {message}\n"
        )