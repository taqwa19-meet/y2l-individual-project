from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("project-home.html")


@app.route('/About us')
def info():
	return render_template("project_info")

	pass

if __name__ == '__main__':
    app.run(debug=True)

