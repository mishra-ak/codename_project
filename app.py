from flask import Flask,render_template,url_for,redirect,request
from prediction import find
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/main/<int:response>")
def main(response):
    if  response == 1:
        return render_template("main.html")

@app.route("/main",methods = ['POST'])
def model():
    if request.method == 'POST':
        q = request.form["ip"]
        ques = list(q)
        label = find(ques)
        return render_template("main.html",title=label)

@app.route("/",methods = ['POST'])
def login():
    dic = {}
    if request.method == 'POST':
        ip = request.form["ip"]
        passwd = request.form["passwd"]
        dic[ip] = passwd
        if dic =={'AKSHAY':'RA1611003030337'} or dic == {'ANCHAL': 'RA1611003030336'}  or dic == {'SHUBHAM' : 'RA1611003030357'}:
            r = 1
            return redirect(url_for('main',response = r))
        else:
            return redirect(url_for('home'))    


if __name__ == "__main__":
    app.run(debug=True,port='3000')
    