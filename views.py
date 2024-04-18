from django.shortcuts import render
from .models import Image

def image_list(request):
    images = Image.objects.all()
    return render(request, 'golden_image/image_list.html', {'images': images})
