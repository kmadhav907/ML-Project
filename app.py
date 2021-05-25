from flask import Flask, render_template, request
import pickle
from SVM import *
import numpy as np

parent_dir = "E:/web/maithli/MLminiproj/TrainingDigits/"


app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    result = ""
    if request.method=="POST":
        print("DATA IS RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)
        file=request.files["file"]
        if file.filename=="":
            return redirect(request.url)
        if file:
           label = file.filename;
           print(label)
           result = test_your_image(parent_dir+label)
           print(result)
          
            

    return render_template("home.html", result= result)

if __name__=="__main__":
    app.run(debug=True, threaded=True)
