from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is the main page"

@app.route("/api")
def api(fd):
    print(fd)
    return {

        'name': 'John',
        'surname': 'Due'
    }

if __name__ == "__main__":
    app.run()