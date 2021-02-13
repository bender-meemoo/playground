from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play")
def play():
    return render_template("index.html")

@app.route("/play/<int:numBoxes>")
def boxes(numBoxes):
    return render_template("index2.html", numBoxes=numBoxes,)

@app.route("/play/<int:numBoxes>/<color>")
def boxesColor(numBoxes, color):
    return render_template("index2.html", numBoxes=numBoxes, color=color)

if __name__ == "__main__":
    app.run(debug=True)