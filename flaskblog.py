from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '08de058bf602514fd4fa46852e4e1a06'


posts = [

{
	'author': 'Vinay KS',
	'title':'Blog Post 1',
	'content':'project',
	'date_posted': '20 Apr 2021 '
},

{
	'author': 'Vinay Kumar',
	'title':'Blog Post 2',
	'content':'project 1',
	'date_posted': '21 Apr 2021 '
}

]

@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))

	return render_template('register.html', title = 'Register', form = form)


@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash(f'You have been logged in!','success')
			return redirect(url_for('home'))
		else:
			flash(f'Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title = 'Login', form = form)


if __name__ == '__main__':
	app.run(debug = True)