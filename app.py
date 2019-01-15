from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("project-home.html")


@app.route('/About us')
def info():
	return render_template("project_info.html")

@app.route('/sign_up', methods ['GET', 'POST'])
def sign_up():
	if request.method == 'GET':
		return render_template('sign_up.html')
	else:
		try:
			username = request.form['name']	
			password = request.form['password']
		except:
			return render_template("signup.html", error="try again")
	create_post(username,password)
	return redirect(url_for('home_page'))
	




	return render_template("sign_up.html")
	
@app.route('/Create_post')
def post():
	return render_template("create_post.html")
	

if __name__ == '__main__':
    app.run(debug=True)

