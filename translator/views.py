from django.shortcuts import render
from . import translate

# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea'] #my_textarea is defined in html
        output = translate.translate(original_text)
        return render(request, 'translator.html', {'output_text':output, 'original_text':original_text}) #output_text and original_text is in html
    else: #in case of GET request
        return render(request, template_name='translator.html')
