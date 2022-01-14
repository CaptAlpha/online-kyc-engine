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
    global pan
    if request.method == 'POST':
        img = request.files['photograph']
        card = request.files['pan-card']

        name = request.form['f-name']
        pan = request.form['pan-card-number']
        
        if not os.path.isdir('static/user'):
            os.mkdir('static/user')

        filepath = os.path.join('static/user', img.filename)
        filepath2 = os.path.join('static/user', card.filename)
        newName = "static/user/user.jpg"
        newName2 = "static/user/pan_user.jpg"

        img.save(filepath)
        card.save(filepath2)
        fp = os.rename(filepath, newName)
        fp2 = os.rename(filepath2, newName2)        
            
        return redirect(url_for('verify'))
    
    return render_template('signupkyc.html')



@app.route("/verify", methods=['GET', 'POST'])
def verify():
    if request.method=='POST':
        time.sleep(5)
        original=face_recognition.load_image_file('static/user/user.jpg')
        captured=face_recognition.load_image_file('static/image.png')
        knownFace=[]
        knownEncoding=face_recognition.face_encodings(original)[0]
        knownFace.append(knownEncoding)
        unknownEncodings=face_recognition.face_encodings(captured)
        if len(unknownEncodings)>0:
            result=face_recognition.compare_faces(knownFace,unknownEncodings[0])
        else:
            return redirect(url_for('verify'))
        if result==[True]:
            os.remove("static/image.png")
            return redirect(url_for('status'))
        elif result==[False]:
            return redirect(url_for('verify'))
        

    return render_template('pic_capture.html')


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
        time.sleep(5)
        file='static/image.png'
        lines = api.ocr_file(open(file, 'rb'))
        x = lines.split()
        global pan_status
        for line in x:
            regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
            p = re.compile(regex)
            if(line == None):
                return redirect(url_for('status'))

            if(re.search(p, line) and len(line) == 10 and line==pan):
                os.remove(file)
                return redirect(url_for('pan_status'))
            else:
                pan_status=False

    return render_template('pan_veri.html');

@app.route('/pan_status',methods=['POST','GET'])
def pan_status():
    os.remove('static\\user\\pan_user.jpg')
    os.remove('static\\user\\user.jpg')
    return render_template('user_confirm.html')

if __name__ == '__main__':
    app.run(debug=True)