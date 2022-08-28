from flask import Flask,render_template,request
from pyshorteners import Shortener
import validators
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'url.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

class urls(db.Model):
    __tablename__ = 'url shortner'
    id = db.Column(db.Integer,primary_key=True)
    long_url = db.Column(db.Text)
    short_url = db.Column(db.Text)

    def __init__(self,long_url,short_url):
        self.long_url=long_url
        self.short_url=short_url

    def __repr__(self):
        return 'Long url is {} and the shortened url is {}'.format(self.long_url,self.short_url)

@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        long_url = request.form['in_1']
        if validators.url(long_url)==True:
            url_1 = Shortener()
            url_shorten= url_1.tinyurl.short(long_url)
            table = urls(long_url,url_shorten)
            db.session.add(table)
            db.session.commit()
            return render_template('result.html',url_shorten=url_shorten)
        else:
            result = 'ENTER A VALID URL'
            return render_template('error.html',result=result)
    return render_template('home.html')

@app.route('/history')
def history():
    history = urls.query.all()
    return render_template('history.html',history=history)


if __name__ =='__main__':
    app.run(debug=True)