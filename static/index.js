'use strict';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const snap = document.getElementById('snap');
const errorMsgElement = document.getElementById('span#errorMsg');

const constraints = {
    audio: false,
    video:{
        width: 640, height: 480
    }
};

async function init(){
    try{
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        handleSuccess(stream);
    }catch(e){
        //errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
    }
}

function handleSuccess(stream){
    window.stream = stream;
    video.srcObject = stream;
}

init();

//Draw the video and save the 
var context = canvas.getContext('2d');
snap.addEventListener('click', function(){
    context.drawImage(video, 0, 0, 640, 480);
    //
    




   

    

});

