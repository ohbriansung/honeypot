# pythonspot.com
from flask import Flask, render_template, flash, request

from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import logging

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required()])
    hidden = TextField('Hidden:', validators=[])
    print(hidden)
    # password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        hidden = form.data['hidden']
        print (name, " ", email, " ", hidden)

        if hidden =="":
            if form.validate():
                # Save the comment here.
                flash('Thanks for registration ' + name)
            else:
                flash('Error: All the form fields are required. ')
        else:
            flash('Error: You might be a bot')
            LOG_FILENAME = 'http.log'
            logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
            logging.info("--------------------\n")

    return render_template('hello.html', form=form)


if __name__ == "__main__":
    app.run(port=8000, debug=True)

