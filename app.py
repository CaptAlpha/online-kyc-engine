from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import numpy as np
from PIL import Image
import base64
import os
import re
from io import StringIO, BytesIO
import face_recognition
import time
import ocrspace
import requests

app = Flask(__name__)
api = ocrspace.API()

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    filepath = "NOT FOUND"
    filepath2 = "NOT FOUND"
    if request.method == 'POST':
        img = request.files['pic']
        card = request.files['card']

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

        filepath = os.path.join('static/user', img.filename)
        filepath2 = os.path.join('static/user', card.filename)
        newName = "static/user/user.jpg"
        newName2 = "static/user/pan_user.jpg"

        print(pan)

        img.save(filepath)
        card.save(filepath2)
        fp = os.rename(filepath, newName)
        fp2 = os.rename(filepath2, newName2)        
            
        return redirect(url_for('verify'))
    
    return render_template('index.html')



@app.route("/verify", methods=['GET', 'POST'])
def verify():
    if request.method=='POST':
        time.sleep(0.5)
        original=face_recognition.load_image_file('static/user/user.jpg')
        captured=face_recognition.load_image_file('static/image.png')
        knownFace=[]
        knownEncoding=face_recognition.face_encodings(original)[0]
        knownFace.append(knownEncoding)
        unknownEncodings=face_recognition.face_encodings(captured)
        result=face_recognition.compare_faces(knownFace,unknownEncodings[0])
        global success
        if result==[True]:
            success="Verified"
        elif result==[False]:
            success="Verification failed"
        print(success)
        return redirect(url_for('status'))

    return render_template('verify.html')


@app.route('/hook', methods=['POST','GET'])
def hook():
    image_b64 = request.values['imageBase64']
    image_data = re.sub('^data:image/.+;base64,', '', image_b64)
    image_data = base64.b64decode(str(image_data))
    image_PIL = Image.open(BytesIO(image_data))
    image_save = image_PIL.save('static/image.png')
    return ''

@app.route("/status",methods=['POST','GET'])
def status():
    if request.method=='POST':
        time.sleep(0.5)
        #pan verification code
        file='static/image.png'
        lines = api.ocr_file(open(file, 'rb'))
        x = lines.split()
        global pan_status
        global pan_num
        for line in x:
            regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
            # Compile the ReGex
            p = re.compile(regex)
        
            # If the PAN Card number
            # is empty return false
            if(line == None):
                return False
        
            # Return if the PAN Card number
            # matched the ReGex
            if(re.search(p, line) and len(line) == 10):
                pan_status=True
                pan_num=line
                break
            else:
                pan_status=False

        return redirect(url_for('pan_status'))
    return render_template('status.html',success=success);

@app.route('/pan_status',methods=['POST','GET'])
def pan_status():
    return render_template('pan_status.html',pan_status=pan_status,pan_num=pan_num)

if __name__ == '__main__':
    app.run(debug=True)