from django.shortcuts import render
from django.shortcuts import render
from .predictors import predict_weather

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')


def weather_predict(request):
    result = None
    if request.method == "POST":
        lon = float(request.POST.get('longitude'))
        lat = float(request.POST.get('latitude'))
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        day = int(request.POST.get('day'))
        
        result = predict_weather(lon, lat, year, month, day)
        
    return render(request, 'weather_form.html', {'result': result})
