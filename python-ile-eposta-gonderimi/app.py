#app.py - flask-mail kullanarak eposta gönderimi

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '81e0d22cd4b15b'
app.config['MAIL_PASSWORD'] = '94355a1553f58b'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail= Mail(app)

@app.route("/")
def index():
    try:
        msg = Message('Test Mesajı', sender =   'ferhatcicek@mailtrap.io', recipients = ['iletisim@ferhatcicek.com'])
        msg.body = "Bu bir test mesajıdır"
        mail.send(msg)
        return "Eposta gönderildi."
    except Exception as e:
        return(str(e))

if __name__ == '__main__':
   app.run(debug = True)
