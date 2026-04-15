import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Exercice 1 / 6
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Exercice 2
@app.get("/paris")
def api_paris():
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]

    return jsonify(result)

# Exercice 5
@app.route("/histogramme")
def histogramme():
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&daily=temperature_2m_max&forecast_days=7&timezone=Europe%2FParis"
    response = requests.get(url)
    data = response.json()

    dates = data["daily"]["time"]
    temperatures = data["daily"]["temperature_2m_max"]

    meteo = list(zip(dates, temperatures))

    return render_template("histogramme.html", meteo=meteo)

# Exercice 6
@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
