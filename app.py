from flask import Flask, render_template
from flask import request
from database import *
from flask import flash, redirect, url_for, session as flask_session
app = Flask(__name__)

app.config['SECRET_KEY'] = 'WHATEVER'

@app.route('/')
def home_page():
	return render_template("project-home.html")


@app.route('/About us')
def info():
	return render_template("project_info.html")

@app.route('/sign_up',methods= ['GET','POST'])
def sign_up():
	if request.method == 'POST':
		name = request.form['username'] 
		password = request.form['psw']
		sign_ups(name,password)
		user = query_user_by_name(name)
		if user is not None and user.password == password:
			flask_session['username'] = user.username
		flash('You were successfully signed up')
		return redirect(url_for('home_page'))

	else:
		return render_template('sign_up.html')


@app.route('/create-post', methods=['GET','POST'])
def post():
	if request.method == 'POST':
		add_Post(request.form['post_submit'])
		return redirect(url_for('posts'))
	return render_template("create_post.html")

@app.route('/log_in',methods= ['GET','POST'])
def log_in():
	if request.method == 'POST':
		name = request.form['uname']
		password = request.form['psw']
		posts = query_all_posts()
		posts = posts.reverse()
		user = query_user_by_name(name)
		if user is not None and user.password == password:
			flask_session['username'] = user.username
			return redirect(url_for('logged_in'))
		else :
			error = 'Username & Password do not match , Please try again'
			flash(error)
			return render_template('log_in.html')
	else:       
		return render_template('log_in.html')

@app.route('/logged_in')
def logged_in():
	return render_template('logged_in.html')


@app.route('/posts')
def posts():
	reversed_posts = reversed(query_all_posts())
	return render_template('posts.html',posts = reversed_posts )


if __name__ == '__main__':
	app.run(debug=True)

