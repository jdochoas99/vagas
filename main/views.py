from django.shortcuts import render
from django.http import HttpResponse
from staticfiles.CNN.predict import finalpredict
# Create your views here.
def index(request):
    data = {}
    finalpredict()
    ##os.system('python staticfiles/CNN/predict.py')
    return render(request, 'main/teste.html', data)