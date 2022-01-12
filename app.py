from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import numpy as np
from PIL import Image
import base64
import re
from io import StringIO, BytesIO


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    
    return render_template('index.html')


@app.route('/hook', methods=['POST'])
def hook():
    image_b64 = request.values['imageBase64']
    image_data = re.sub('^data:image/.+;base64,', '', image_b64)
    image_data = base64.b64decode(str(image_data))
    
    image_PIL = Image.open(BytesIO(image_data))
    image_save = image_PIL.save('flask-app\static\image.png')

    return ''

if __name__ == '__main__':
    app.run(debug=True)