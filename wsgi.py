from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/demo")
def hello():
    return "<b>Hello World!</b>"

if __name__ == "__main__":
    application.run()
