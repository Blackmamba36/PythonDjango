from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts = [

    {
        'autor': 'Simon',
        'titulo': 'Post de Simon',
        'contenido':'lorep ipsum',
        'fecha_publicacion' : '28 de Enero 2022'

    },

    {
        'autor': 'Allison',
        'titulo': 'Post de Allison',
        'contenido':'lorep ipsum',
        'fecha_publicacion' : '28 de Enero 2022'

    }


]



def home(request):
    # Se define para que nos pueda crear los objetos antes definidos 
    contexto = {
        'posts': posts
    }
    return render(request, 'blog/index.html', contexto) # Render descarga toda la plantilla que tengamos directamente a nuestro buscador


def about(request):
    return HttpResponse('<h1>About Awakelab</h1>')
    
