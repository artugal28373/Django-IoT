#from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializers import *
import requests
import os
from PIL import Image
import io
import numpy as np
from sklearn.svm import SVC
import cv2
import joblib

'''
'''
#import matplotlib.pyplot as plt

'''
'''

# Create your views here.

@api_view(["POST"])
def getResult(request):
    image_url = request.data['url']
    #print("**image url: "+image_url)


# Extract the image code from the URL
    image_code = os.path.splitext(os.path.basename(image_url))[0]


# Get the actual image URL
    #download_url = image_url

# Send the GET request
    response = requests.get(image_url)

# Check for successful response
    if response.status_code == 200:
    # Prepare the filename with extension
         #filename = f"{image_code}{os.path.splitext(image_url)[1]}"
         image = Image.open(io.BytesIO(response.content))
         #plt.imshow(image)
         #plt.show()
         numpy_array = np.array(image)
         img = cv2.cvtColor(numpy_array, cv2.COLOR_RGB2BGR)
         # Convert the image to JPEG format
         #img = image.convert('L')

        # Save the converted image to a BytesIO object
         ''''''
         model = joblib.load('model.pkl')
         image_size = (128, 128)  # Adjust as needed
         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         img = cv2.resize(img, image_size)
         prediction = model.predict([img.flatten()])[0]
         val = "fire" if prediction == 1 else "nonfire"
         ''''''
         #plt.imshow(image) #debug code
         #plt.show() #debug code
   
         #s = list(filename)
         #filename = ''.join(s[0:-4])  # Corrected the slicing to remove the file extension
         #print(f"Image downloaded successfully! Saved as: {filename}")
         return Response({"payload" : val})
    else:
        print(f"Error downloading image: {response.status_code}")

    
    
    
