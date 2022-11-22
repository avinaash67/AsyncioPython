""" Main file """
from flask import Flask
from flask import jsonify

app = Flask(__name__)  # instance of flask class

@app.route("/")
def hello_world():
    """ Produces a hello-world html response at endpoint '/' """
    return "<p>Hello world</p>"  # return html 

@app.route("/health")
def health():
    """ Used to check the health of the python application.
    User can check the health of the application using the restAPI-endpoint '/health'
    """
    return jsonify(  #jsonify - converts string to json format
        status = 'UP'
    )

if __name__ == "__main__":
    # Run Flask application
    app.run(host= '0.0.0.0', port=5000)
