from flask import Flask, render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os



app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)




class Telephone(db.Model):
	__tablename__ = 'telephone'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	number = db.Column(db.Integer)

	def __init__(self,name,number):
		self.name = name
		self.number = number
	def __repr__(self):
		return " name - {} and number - {}".format(self.name, self.number)




@app.route("/")
def index():
	return render_template("layout.html")

@app.route("/add",methods=['GET','POST'])
def add():
	name1 = request.form.get("var_1")
	print(name1)
	number1 = request.form.get("var_2")
	if name1 != None and number1 != None:
		if name1 !="" and number1 !="":
			data = Telephone(name1,number1)
			db.session.add(data)
			db.session.commit()
	return render_template("add.html")

@app.route("/display")
def display():
	details = Telephone.query.all()
	return render_template("display.html", details = details)

@app.route("/search",methods =["Get","Post"])
def search():
	s=request.form.get("search")
	priya  = Telephone.query.filter_by(name = s)
	return render_template("search.html",priya = priya)

if __name__ == '__main__':
	app.run(debug=True,port=5009)