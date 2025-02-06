from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///movies.db'
db= SQLAlchemy(app)
class Movie(db.Model):
   id= db.column(db.Integer, primary_key= True)
   title= db.column(db.String(80))
   release_year= db.column(db.Integer)
   director= db.column(db.String(80))
   runtime = db.column(db.Integer)
   def repr(self):
        return f'<Movie %r>' % self.title
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