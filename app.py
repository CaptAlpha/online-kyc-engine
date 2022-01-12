from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import numpy as np
from PIL import Image
import base64
import re
from io import StringIO, BytesIO


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    filepath = "NOT FOUND"
    filepath2 = "NOT FOUND"
    if request.method == 'POST':
        img = request.files['pic']
        pan = request.files['pan']

        name = request.form['user']
        email = request.form['email']
        phone = request.form['phone']
        pan = request.form['pan']
        


        
        if not os.path.isdir('static/user'):
            os.mkdir('static/user')

        if os.path.isfile("static/user/user.jpg"):
            os.remove("static/user/user.jpg") 
        
        if os.path.isfile("static/user/pan_user.jpg"):
            os.remove("static/user/pan_user.jpg") 

        filepath = os.path.join('static/assets', img.filename)
        filepath2 = os.path.join('static/assets', pan.filename)
        newName = "static/assets/cover.jpg"
        newName2 = "static/assets/watermark.jpg"

        
        
        print(pan)

        file.save(filepath)
        file2.save(filepath2)
        fp = os.rename(filepath, newName)
        fp2 = os.rename(filepath2, newName2)
        
        
            
        return redirect(url_for('verify'))
    
    return render_template('index.html')



@app.route("/verify", methods=['GET', 'POST'])
def verify():

    return render_template('verify.html')


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