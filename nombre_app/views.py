from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'nombre_app/index.html')

def formulario(request):
    return render(request, 'nombre_app/formulario.html')

def resultados(request):

    fname = request.POST['fname']
    lname = request.POST['lname']
    age = request.POST['age']
    email = request.POST['email']
    dieta = request.POST['dieta']
    vivienda = request.POST['vivienda']

    animales = []
    if 'animal1' in request.POST:  # OJO con los checkboxes
        animales.append(request.POST['animal1'])
    if 'animal2' in request.POST:  # OJO con los checkboxes
        animales.append(request.POST['animal2'])


    context = {}
    context['fname'] = fname
    context['lname'] = lname
    context['age'] = age
    context['email'] = email
    context['dieta'] = dieta
    context['vivienda'] = vivienda
    context['animales'] = animales



    return render(request, 'nombre_app/resultados.html',context)
