from flask import Flask,render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///contact_form.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(200))
    company_name= db.Column(db.String(500))
    number = db.Column(db.Integer)
    message = db.Column(db.String(500))
    date_created = db.Column(db.Integer , default = datetime.utcnow)

    

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():

    if request.method == "POST":
        emp_name = request.form['emp_name']
        company_name = request.form['company_name']
        number = request.form['number']
        message = request.form['message']
        contact = Contact(emp_name = emp_name, company_name = company_name,number = number, message = message)
        db.session.add(contact)
        db.session.commit()

    return render_template('index.html')

@app.route('/download', methods= ['GET', 'POST'])
def download():
    p = "Resume.pdf"
    return send_file(p, as_attachment=True)


if __name__=="__main__":
    app.run(debug= False, host='0.0.0.0')