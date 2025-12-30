from flask import Flask, render_template, request, redirect, jsonify
import requests


API_KEY = "2e1083a5c426416f88a231919252912"


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
        if data:
            print(data)
        return render_template("index.html", data=data)
