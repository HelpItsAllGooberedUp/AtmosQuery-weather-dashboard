from flask import Flask, render_template, request, redirect, jsonify
import requests, os
from condition_icons import CODE_TO_ICON
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():


    if request.method =="GET":
        return render_template("welcome.html")
    
    

    if request.method == "POST":
        city = request.form.get("location")
        default = request.remote_addr or "New York City"

        response = requests.get(f"http://api.weatherapi.com/v1/current.json",
                     params={"key": API_KEY, "q": city or default}) 
        
        data = response.json()
        weather_code = (data.get("current", {}).get("condition", {}).get("code", 0))

        iconpath = CODE_TO_ICON.get(weather_code, "images/icons/wi-na.svg")
    
        return render_template("index.html", data=data, iconpath=iconpath)
