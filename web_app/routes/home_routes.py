# Final_Project_OPIM244/routes/home_routes.py

from flask import Blueprint, render_template, redirect, flash

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    return render_template("home.html")

@home_routes.route("/nameresult")
def nameresult():
    print("VISITED THE NAME RESULT PAGE")
    #return "About Me (TODO)"
    return render_template("nameresult.html")

@home_routes.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    #return "About Me (TODO)"
    return render_template("about.html")