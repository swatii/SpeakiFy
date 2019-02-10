import rec2

from flask import Flask, render_template, redirect, url_for, request 
app = Flask(__name__)


@app.route("/")
def index():
     return render_template("index.html")

  
@app.route('/msg',methods = ['POST', 'GET']) 
def val(): 
   if request.method == 'POST': 
      p = str(rec2.rec())
      if p!= "":
        msg = p.lower()
        print msg
      else:
        msg = p
      #msg = "hi i am swati"
   #msg = ["hi", "Swats"]

   letters = []
   for c in msg:
      if c == ' ':
        d = "static/images/space.png"
      else:
        d = "static/images/" + c + ".jpg"
      letters.append(d)


   return render_template("sign.html", rows = letters)


if __name__ == "__main__":
    app.run(debug=True)


