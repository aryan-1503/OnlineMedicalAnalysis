from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route('/lungs.html')
def lungs():
    return render_template('lungs.html')

@app.route('/heart.html')
def heart():
    return render_template('heart.html')
@app.route('/thyroid.html')
def thyroid():
    return render_template('thyroid.html')




if __name__ == '__main__':
    app.run(debug=True)