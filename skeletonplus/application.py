from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/docs')
@app.route('/demo')
def demo():
    return render_template('demo.html')
