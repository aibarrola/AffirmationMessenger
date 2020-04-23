from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home")


@app.route("/gallery")
def gallery():
    return render_template('gallery.html', title="Gallery")

@app.route("/createEnvelope")
def register():
    return render_template('createEnvelope.html', title="Create Envelope")


if __name__ == "__main__":
    app.run(debug=True)

