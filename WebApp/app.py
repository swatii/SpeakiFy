"#hello world#" 
from flask import Flask, request, render_template  # Here, we load the Flask python package
import webbrowser

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))  # This is how you create a path in Flask
def hello():  

    if request.method == 'GET':
        return render_template("sw1.html")
    animal = request.form['animal']
    if not animal:
        return 'Error: No animal provided'
    if animal == 'dog':
        image_url = "https://d17fnq9dkz9hgj.cloudfront.net/uploads/2018/04/Frenchie_05.jpg"
    elif animal == 'cat':
        image_url = "https://data.whicdn.com/images/298844185/large.jpg?t=1507433077"
    else:
        image_url = 'https://img.purch.com/h/1000/aHR0cDovL3d3dy5saXZlc2NpZW5jZS5jb20vaW1hZ2VzL2kvMDAwLzAwOS82Nzkvb3JpZ2luYWwvMDkwNTExLXBsYXR5cHVzLTAyLmpwZw=='


    return '''
        <h1>Hello {animal_name}!</h1>
        <image style="width: 100%" src="{image_src}" />
    '''.format(animal_name=animal, image_src=image_url)




@app.route('/validate',methods = ['POST', 'GET']) 
def val(): 
      return render_template("show.html")


# new code below
@app.route('/')
def index():
    return 'Welcome to the server root with changes'
