from flask import Flask , request
import classify


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is the main page"

@app.route("/api", methods = ['GET','POST'])
def api():

    f = request.files['image']
    print(classify.classifyImage(f))
    
    return {
        'name': 'John',
        'surname': 'Due',
        'type': classify.classifyImage(f)
    }

if __name__ == "__main__":
    app.run()

# I believe it will enable to send data with fetch
#flask_cors.CORS(app, expose_headers='Authorization')