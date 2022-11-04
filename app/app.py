from flask import Flask

app = Flask(__name__)
@app.route("/")
def holaMundo():
  return "<h1> Hola Mundo, desde mi Web, esta es mi primer aplicación!</h1>"

if __name__ == "__main__":
  app.run(host="0.0.0.0")

