from flask import Flask, render_template, redirect, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



 