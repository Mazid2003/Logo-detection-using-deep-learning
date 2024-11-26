from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
from PIL import Image
import io
from .model import model, class_names
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this


def index(request):
    return render(request, 'index.html')
@csrf_exempt
def predict(request):
    print(request.method)
    if request.method == 'POST' and request.FILES['file']:
        image_file = request.FILES['file']
        image = Image.open(image_file)
        image = image.resize((256, 256))
        image = np.array(image)
        image = np.expand_dims(image, axis=0)
        image = image / 255.0
        print(request.method)
        prediction = model.predict(image)
        predicted_class_index = np.argmax(prediction, axis=1)[0]
        predicted_class_name = class_names[predicted_class_index]
        confidence = prediction[0][predicted_class_index]

        return JsonResponse({'prediction': predicted_class_name, 'confidence': str(confidence)})
    return JsonResponse({'error': 'Invalid request'}, status=400)
