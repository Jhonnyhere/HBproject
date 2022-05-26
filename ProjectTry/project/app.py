from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from models import db,detail
app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://actecal:actecal12345@actecalserver/student1"
app.config['SECRET_KEY'] = "NOTHING"


@app.route("/")
def home():
    return render_template('home.html')
    
@app.route("/latest")
def latest():
    return render_template('latest.html')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')
    
@app.route("/contact")
def contact():
    return render_template('contact.html')
    
@app.route("/cart")
def cart():
    return render_template('cart.html')

@app.route("/student")
def student():
    return render_template("details.html")

@app.route("/student", methods=["GET","POST"]) 
def student_post():
    name = request.form('name')
    father_name = request.form('father_name')
    address = request.form('address')
    standard = request.form('standard')
    roll_no = request.form('roll_no')
    phone = request.form('phone')    
    
    details = detail(name=name,father_name=father_name,address=address,standard=standard,roll_no=roll_no,phone=phone)       
    db.session.add(details)
    db.session.commit()
    return render_template("details.html" , details =details)
 
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=2000)