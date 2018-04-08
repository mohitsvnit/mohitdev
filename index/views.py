from django.shortcuts import render
#from keras.models import load_model
from django.http import HttpResponse
from .forms import UploadFileForm
import base64
# Create your views here.
#import tensorflow as tf


def index(request):
    '''
    if(request.method == "POST"):
        response = request.POST.get("file")
        image_64_decode = base64.decodestring(response)

    response = "{\"status\":5,\"message\":"+response+"}"
    '''
    return HttpResponse("3665")

def predictDisease(request):
    return HttpResponse("62")

# if request.method == 'POST':
# 	form = UploadFileForm(request.POST, request.FILES)
# 	if form.is_valid():
# 		file = request.FILES['file']
# else:
# 	form = UploadFileForm()

# model = load_model('models/mymodel-3.h5')
# X = []
# X.append(img)
# y_pred_proba = model.predict(np.array(X))
# y_pred = (y_pred_proba >0.5)*1
# print(y_pred)
