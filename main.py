#import "Flask"
from flask import Flask, render_template

#create "Flask"
app = Flask(__name__)

#home
@app.route('/')
def home():
    return render_template("index.html")

#rsa demonstration
@app.route('/rsa')
def rsaEX():
    return render_template("rsa.html")
#rsa info
@app.route('/rsa/about')
def rsaAbout():
    return render_template("rsaAbout.html")

#run file
if __name__ == "__main__":
    app.run(debug = True)