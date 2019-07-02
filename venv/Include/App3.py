from flask import Flask, render_template, url_for, flash, redirect
from bs4 import BeautifulSoup
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e15f92a144579f3ba3a66512f7be144a'

posts = [
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 12, 2019'
    },
    {
        'author': 'Adam Dean',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 13, 2019'
    }]


@app.route("/")
def home():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect((url_for('home')))
        else:
            flash('Login unsuccessful. Please check username and password!', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
