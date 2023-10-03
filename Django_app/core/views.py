from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Juego, Categoria 

# Create your views here.

def root(request):
    context = {'saludo':'Bienvenido root'}
    return render(request, 'core/home.html', context)

def home(request):
    context = {'saludo':'Wink Bienvenido'}
    return render(request, 'core/home.html', context)

def login(request):
    #Key: value
    context= { 'nombre':'Top Games' }
    # Lógica para la página de inicio de sesión
    return render(request, 'core/login.html', context)

def contacto(request):
    context = {'concato_con':'Página de contacto'}
    return render(request, 'core/contacto.html', context)

def categoria_carreras(request):
    return render(request, 'core/categoria/carreras.html')

def categoria_deporte(request):
    return render(request, 'core/categoria/deporte.html')

def categoria_lucha(request):
    return render(request, 'core/categoria/lucha.html')

def categoria_terror(request):
    return render(request, 'core/categoria/terror.html')

def categoria_accion(request):
    return render(request, 'core/categoria/accion.html')

def categoria_shooter(request):
    return render(request, 'core/categoria/shooter.html')
 

 # JUEGOS
def juego_accion1(request):
    return render(request, 'core/juego/juego_accion1.html')

def juego_index(request):
    juegos = Juego.objects.all() # SELECT * FROM LIBRO
    print(juegos)

    context = {
        'juego_index': 'Juegos',
        'juegos': juegos  
    }

    if request.method=='POST':
            codigo = request.POST.get('codigo')
            nombre = request.POST.get('nombre')
            categoria = request.POST.get('categoria')
            descripcion = request.POST.get('descripcion')
            
            categoria = get_object_or_404 (Categoria, id=categoria )

            print(f"nombre {nombre} categoria {categoria} descripcion {descripcion} codigo {codigo}")


            Juego.objects.create(
                codigo_isbn = codigo,
                nombre = nombre,
                descripcion = descripcion,
                categoria=categoria
            )

            #Juego.objects.create(
                #codigo_isbn = codigo,
                #nombre = nombre,
                #descripcion = descripcion,
                #categoria_id=categoria
            #)
        

    return render(request, 'core/juego/index.html', context)


def juego_create(request):
        categorias = Categoria.objects.all() # SELECT * FROM LIBRO
        context ={'categorias': categorias }
        return render(request, 'core/juego/create.html', context)


#def juego_show(request, id):
    # Lógica para la página de contacto
    #juegos = ['accion1', 'accion2', 'accion3']
    #images = ['accion1.jpg', 'accion2.jpg', 'accion3.jpg']
    #juego = juegos ['id-1']
    #img = images ['id-1']

    #context= { 
       # 'nombre':juego,
        #'img':img
        #}
   # return render(request, 'core/juego/show.html', context)



def juego_show(request, id):
    # Lógica para la página de contacto
    juegos = ['accion1', 'accion2', 'accion3']
    images = ['accion1.jpg', 'accion2.jpg', 'accion3.jpg']
    juego = juegos[int(id) - 1]
    img = images[int(id) - 1]

    context = { 
        'juego': juego,  # Cambiado de 'nombre' a 'juego'
        'img': img
   }
    return render(request, 'core/juego/show.html', context)




def mostrar(request, id):
    # Lógica 
    print(f"ID: {id}")
    juegos =[
        {'nombre': 'Accion', 'image': 'images/fornite.jpg'},
        {'nombre': 'Carreras', 'image': 'images/forza.jpg'},
        {'nombre': 'Deporte', 'image': 'images/deporte.jpg'},
        {'nombre': 'Lucha', 'image': 'images/ssff6.jpg'},
        {'nombre': 'Shooter', 'image': 'images/shooter.jpg'},
        {'nombre': 'Terror', 'image': 'images/resident.jpg'}
        ]
    
    if id >= 0 and id < len(juegos):
        context = { 
            'juego': juegos[id],  # Cambiado de 'nombre' a 'juego'
    }
        return render(request, 'core/mostrar.html', context)
    else:
        return redirect ('home')


