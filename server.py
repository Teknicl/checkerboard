from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def block():
    return render_template('index.html')

@app.route('/<int:x>')
def rows(x):
    return render_template('index.html',row=x)

@app.route('/<int:x>/<int:y>')
def col(x,y):
    return render_template('index.html',row=x,col=y)

@app.route('/<path:path>')
def catch_all():
    return 'Invalid URL'

if __name__=="__main__":
    app.run(debug=True)