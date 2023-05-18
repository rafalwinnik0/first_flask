from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/quess/<name>")
def say_quess(name):
    age_response = requests.get(f"https://api.agify.io/?name={name}")
    age_response.raise_for_status()
    age = age_response.json()["age"]
    sex_response = requests.get(f"https://api.genderize.io/?name={name}")
    sex_response.raise_for_status()
    sex = sex_response.json()["gender"]
    return render_template("guess.html", name=name, age=age, sex=sex )

if __name__ == "__main__":
    app.run()
