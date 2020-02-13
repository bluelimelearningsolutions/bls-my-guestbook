from flask import Flask ,render_template,request,redirect,url_for
#import mysql.connector
#import pymysql
from flask_sqlalchemy import SQLAlchemy

#from flask_mysql import MySQL
#from flask.ext.mysql import MySQL
#from flaskext.mysql import MySQL

#First we imported the Flask class from the flask library. 
# Render Templates lets you render templates
'''
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guestbook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
'''


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://sql2322449:bY6!jX6@sql2.freemysqlhosting.net/sql2322449'
#app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://sql2322449:bY6!jX6@sql2.freemysqlhosting.net/sql2322449'
#app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+mysqldb://sql2322449:bY6!jX6@sql2.freemysqlhosting.net/sql2322449'
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:Monday09@localhost/guestbook'
app.config['DATABASE_URI']='postgres://dqdasjgibihrfu:e91bfe3483b8988ac715abb3d4445a2e842abf1bcdc44221fc23879368fd10d7@ec2-3-231-46-238.compute-1.amazonaws.com:5432/d69c0jelktl1fm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Monday09'
app.config['MYSQL_DB'] = 'guest_book'

mysql = MySQL(app)
'''
class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	comment = db.Column(db.String(1000))



#An instance of this class will be our WSGI application.

'''
Next we create an instance of this class on line 4
first argument is the name of the application’s module or package.
If you are using a single module (as in this example),
you should use __name__ because depending on if it’s started as application
or imported as module the name will be different
('__main__' versus the actual import name).
This is needed so that Flask knows where to look for templates,
static files, and so on. 

'''



# Create route  # We then use the route() decorator to tell 
#Flask what URL should trigger our function.

@app.route('/')
def index():
	result = Comments.query.all()

	return render_template('index.html', result=result)

    #return render_template('index.html')

 
 #The view function is given a name which is also used to 
 #generate URLs for that particular function, and returns the message
 #we want to display in the user’s browser.
 
#if __name__=='__main__':
	#app.run(debug=True) # debug mode will help address errors

# If code is called from cmd we want app to run.	

# Creating more endpoints
@app.route('/about')
def about():
    return '<h1>This is a simple guestbook application</h1>'


@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']

	signature = Comments(name=name, comment=comment)
	db.session.add(signature)
	db.session.commit()

	return redirect(url_for('index'))

	#return render_template('index.html', name=name, comment=comment)


if __name__ == '__main__':
    app.run(debug=True)
