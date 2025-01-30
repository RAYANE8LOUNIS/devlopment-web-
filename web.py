from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
   image_filenames = ['london.jpg', 'rayane.jpg']
   return render_template('index.html', images=image_filenames)

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/contact")
def contact():
   return render_template("contactpage.html")

@app.route("/grid")
def gride():
   return render_template("code.html")



if __name__ == '__main__':
    app.run(debug=True)