from django.shortcuts import render, redirect

# Datos de ejemplo (sin base de datos)
CATEGORIAS = {
    'Ciencias': [
        {'pregunta': '¿Cuál es el planeta más grande del sistema solar?',
         'opciones': ['Tierra', 'Júpiter', 'Marte', 'Saturno'],
         'correcta': 'Júpiter'},
        {'pregunta': '¿Qué gas respiran los humanos?',
         'opciones': ['Hidrógeno', 'Dióxido de carbono', 'Oxígeno', 'Nitrógeno'],
         'correcta': 'Oxígeno'},
    ],
    'Historia': [
        {'pregunta': '¿En qué año llegó Cristóbal Colón a América?',
         'opciones': ['1492', '1500', '1519', '1485'],
         'correcta': '1492'},
        {'pregunta': '¿Quién fue el primer presidente de México?',
         'opciones': ['Porfirio Díaz', 'Guadalupe Victoria', 'Benito Juárez', 'Antonio López de Santa Anna'],
         'correcta': 'Guadalupe Victoria'},
    ],
}

def index(request):
    return render(request, 'apptriv/index.html')

def categorias(request):
    return render(request, 'apptriv/categorias.html', {'categorias': CATEGORIAS.keys()})

def jugar(request, categoria):
    preguntas = CATEGORIAS.get(categoria, [])
    if request.method == 'POST':
        correctas = 0
        for i, pregunta in enumerate(preguntas):
            respuesta = request.POST.get(f'p{i}')
            if respuesta == pregunta['correcta']:
                correctas += 1
        return redirect('resultado')

    return render(request, 'apptriv/jugar.html', {'categoria': categoria, 'preguntas': preguntas})

def resultado(request):
    return render(request, 'apptriv/resultado.html')
