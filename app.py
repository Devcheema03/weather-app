from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "c98e3b6d38fcf477519c284c9568ec2f"

@app.route('/', methods=["GET", "POST"])
def home():

    weather = None

    if request.method == "POST":

        city = request.form["city"]

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        if data["cod"] == 200:

            weather = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)

    