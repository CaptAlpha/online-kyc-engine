from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    
    return render_template('index.html')

@app.route("/image", methods=['GET', 'POST'])
def image():
    if request.method == 'GET':
        #retrieve image from request
        image = request.files['image']
        #save image to disk
        image.save('./static/image.jpg')
        #return image
        return jsonify({"image": "image.jpg"})
    else:
        return jsonify({"error": "Method not allowed"})
    