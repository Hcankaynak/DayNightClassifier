from flask import Flask , request
import classify


app = Flask(__name__)

@app.route("/api", methods = ['GET','POST'])
def api():
    # get the file 
    f = request.files['image']
    # testing type of image (day or night)
    print(classify.classifyImage(f))
    # return the type of the file.
    return {
        'type': classify.classifyImage(f)
    }

if __name__ == "__main__":
    app.run()
