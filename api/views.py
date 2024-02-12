from django.shortcuts import render
#from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .serializers import *
import requests
import os
import matplotlib.pyplot as plt
from PIL import Image
import io
# Create your views here.

@api_view(["POST"])
def getResult(request):
    image_url = request.data['url']
    print("**image url: "+image_url)


# Extract the image code from the URL
    image_code = os.path.splitext(os.path.basename(image_url))[0]


# Get the actual image URL
    download_url = image_url

# Send the GET request
    response = requests.get(download_url)

# Check for successful response
    if response.status_code == 200:
    # Prepare the filename with extension
         filename = f"{image_code}{os.path.splitext(image_url)[1]}"
         image = Image.open(io.BytesIO(response.content))
         # Convert the image to JPEG format
         image = image.convert('RGB')

        # Save the converted image to a BytesIO object
         output = io.BytesIO()
         image.save(output, format='JPEG')

         #plt.imshow(image) #debug code
         #plt.show() #debug code
   
         s = list(filename)
         filename = ''.join(s[0:-4])  # Corrected the slicing to remove the file extension
         #print(f"Image downloaded successfully! Saved as: {filename}")
         return Response({"payload" : "yes"})
    else:
        print(f"Error downloading image: {response.status_code}")

     
