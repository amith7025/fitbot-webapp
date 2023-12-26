from django.shortcuts import render
from translate import translate
import random

L = []

def home(request):
    if request.method == 'POST':
        prompt_value = request.POST.get('prompt', '')
        ans = translate(prompt_value)
        L.append({'prompt': prompt_value, 'translation': ans})
        return render(request, 'index.html', {'data': L})
    else:
        return render(request, 'index.html')
