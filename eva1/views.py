from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Variables globales para almacenar los datos del ESP32
sensor_data = {
    'valor': 0,
    'voltaje': 0.0,
    'voltaje_corregido': 0.0
}

@csrf_exempt

def home_view(request):
    # Si es un POST, actualiza los valores
    if request.method == 'POST':
        sensor_data['valor'] = request.POST.get('valor')
        sensor_data['voltaje'] = request.POST.get('voltaje')
        sensor_data['voltaje_corregido'] = request.POST.get('voltaje_corregido')
        return JsonResponse({'status': 'Datos recibidos correctamente'})
    
    # Si es un GET, renderiza el template con los valores actuales
    return render(request, 'home.html', sensor_data)
