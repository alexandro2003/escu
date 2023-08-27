from django.shortcuts import render, redirect
from .models import Usuario, Inscripcion, Carrera





def registro_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        correoelectronico = request.POST.get('correoelectronico')
        contraseña = request.POST.get('contraseña')
        
        nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, dni=dni, correoelectronico=correoelectronico, contraseña=contraseña)
        nuevo_usuario.save()
        return redirect('iniciar_sesion')  # Redirige a la página de inicio después del registro
    
    return render(request, 'registrarse.html')

def iniciar_sesion_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')

        try:
            User = Usuario.objects.get(nombre=nombre)
            if User.contraseña == contraseña:
                return redirect('codigocarrera')
            else:
                error_message = "Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo."
                return render(request, 'iniciarsesion.html', {'error_message': error_message})
        except Usuario.DoesNotExist:
            error_message = "Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo."
            return render(request, 'iniciarsesion.html', {'error_message': error_message})

    return render(request, 'iniciarsesion.html')

def inicio_view(request):
    return render(request, 'inicio.html')

def avatar_view(request):
    return render(request, 'avatar.html')

def home_view(request):
    return render(request, 'home.html')

def cerrarsesion_view(request):
    return render(request, 'cerrarsesion.html')

def codigocarrera_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        codigo = request.POST.get('codigo')
        
        nuevo_usuario = Carrera(usuario=usuario, codigo=codigo)
        nuevo_usuario.save()
        
        return redirect('home')  # Redirige a la página de inicio después del registro
    
    return render(request, 'codigocarrera.html')

def editarperfil_view(request):
    return render(request, 'editarperfil.html')

def olvidocontraseña_view(request):
    return render(request, 'olvidocontraseña.html')


def perfil_view(request):
    return render(request, 'perfil.html')

def inscripcionexamenes_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        localidad = request.POST.get('localidad')
        direccion = request.POST.get('direccion')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        nueva_inscripcion = Inscripcion(nombre=nombre, apellido=apellido, dni=dni,
                                        localidad=localidad, direccion=direccion,
                                        email=email, telefono=telefono)
        nueva_inscripcion.save()

        return redirect('home')  # Redirige a la página de inicio después de la inscripción

    return render(request, 'inscripcionexamenes.html')

def inscripcionexamenes2_view(request):
    return render(request, 'inscripcionexamenes2.html')

def inscripcionmaterias_view(request):
    return render(request, 'inscripcionmaterias.html')

def inscripcionmaterias2_view(request):
    return render(request, 'inscripcionmaterias2.html')



