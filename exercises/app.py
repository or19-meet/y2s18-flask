from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	players=["Dele", "Griezmann", "Kane"]
	return render_template(
		"index.html",
		players=players,
		like_some_sport=True)

    

if __name__ == '__main__':
   app.run(debug = True, port=8080)