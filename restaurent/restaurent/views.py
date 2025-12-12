from django.shortcuts import render
from restaurent.forms import QRCodeForm
import qrcode
import os
from django.conf import settings


 

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Generate QR code
            qrcode_img = qrcode.make(url)
            file_name=restaurant_name.replace(" ","_").lower()+'_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qrcode_img.save(file_path)

            # create image  url
            qr_image_url = os.path.join(settings.MEDIA_URL, file_name)
            context ={
                'res_name':restaurant_name,
                'qr_image_url':qr_image_url
            }

            return render(request, 'qr_code_result.html',context)
              
    else:
        form = QRCodeForm()
        context = {'form': form}
        return render(request,'generate_qr_code.html',context)