import base64
import io
import numpy as np
import os
from PIL import Image
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import Flask,request,redirect,url_for
from flask import render_template,jsonify
from werkzeug import secure_filename
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys
from keras.preprocessing.image import img_to_array

app = Flask(__name__)

@app.route('/launch')
def launch():
    return render_template('home.html')

def get_model():
    global model
    model = load_model('gender.h5')
    print("Model loaded !")

print("Loading Keras model")
get_model()

@app.route('/predict',methods=['POST','GET'])
def store_pic():
    if request.method == 'POST':
        os.chdir('path to folder of images')
        dirs = os.listdir('path to folder of images')
        img = Image.open(dirs[0])
        image = img.resize((32,32),Image.NEAREST)
        image = img_to_array(image)
        image = np.expand_dims(image,axis = 0)
        result = model.predict_classes(image).tolist()
        if(result[0]==0):
            os.remove(dirs[0])
            return 'female'
        else:
            os.remove(dirs[0])
            return 'male'
if __name__ =="__main__":
    app.run(debug=True)