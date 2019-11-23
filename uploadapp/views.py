from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from uploadprjt import settings
from django.views.decorators.csrf import csrf_exempt
import base64
from django.core.files.base import ContentFile

# Create your views here.
# Create your views here.
def hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html', {'form' : form})


def success(request):
    img = Hotel.objects.all().last()
    return render(request,'gallery.html',{"img":img, 'media_url':settings.MEDIA_URL})


def uploadview(request):
    return render(request, 'upload.html')
def uploadimg(request):
    print('sgfshgdgdfhsgdfhgsdfhg')
    imagemodel=Imagemodel()
    if request.method=="POST":
        print('asdfghjkl')
        image=request.POST.get('imgBase64')
        print(image)
        data1={
        'hello':'123'
        }
        print('5465467987987987')
        return JsonResponse(data1)
    else:
        return redirect(uploadview)
