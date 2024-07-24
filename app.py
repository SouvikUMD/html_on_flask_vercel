# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 13:05:54 2023

@author: prama
"""

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def gfg_form():
    return render_template("index.html")

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       print("first_name: ", first_name)
       # getting input with name = lname in HTML form
       last_name = request.form.get("lname")
       print("last_name: ", last_name)
       return "Your name is "+first_name + last_name