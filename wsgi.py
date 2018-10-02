from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/demo")
def hellodemo():
    return "<b>Hello World!</b><br><img src=\"https://media.giphy.com/media/QgixZj4y3TwnS/giphy.gif\">"

if __name__ == "__main__":
    application.run()
