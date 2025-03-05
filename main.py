from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["get","post"])
def displayGrid():

    if request.method == "POST":
        #get the data from the form and check right or wrong against solution.
        # print(request.form.getlist())

        gridData = [
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
        ]
        #check if it is right or wrong
    else:
        gridData = [
            ["1","","","","","","","",""],
            ["","","","3","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","7","","",""],
            ["","","","","","","","",""],
            ["","","","4","","","","",""],
            ["","","","","","","","",""],
            ["","","","","","","","",""],
        ]
        
        
    return render_template("solution.html", gridData = gridData)






app.run(debug = True)