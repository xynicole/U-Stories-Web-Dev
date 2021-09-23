import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index.html')
def root():
    return flask.render_template('index.html')

@app.route('/homepage.html')
def homepage():
    return flask.render_template('homepage.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)