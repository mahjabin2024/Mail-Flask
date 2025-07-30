from flask import Flask, render_template,request,redirect,flash
from flask_mail import Mail,Message

app=Flask(__name__)
app.secret_key="my_secret_key"

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False
app.config['MAIL_USERNAME']='tasbihmahjabin2010@gmail.com'
app.config['MAIL_PASSWORD']='pehe zssp lvmn laov'

mail=Mail(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/send',methods=['POST'])
def send_email() :
    try:
        name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        message=request.form['message']

        msg=Message(subject=subject,sender=app.config['MAIL_USERNAME'], recipients=[email])
        msg.body=f"Hello {name}, \n\n {message}"
        mail.send(msg)
        flash("Email sent succesfully!", "success")
    except Exception as e:
        print(e)
        flash("Failed sending the email")

    return redirect('/')
if __name__=='__main__':
    app.run(debug=True)