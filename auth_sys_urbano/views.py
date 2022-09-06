from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.


def login_view(request):
    
    # print(request.method)
    # verificando que el Metodo POST se haya utilizado
    if request.method == 'POST':
        # optenemos el valor del Dicciionario 'POST', 
        # mediante la 'llave' correspondiente
        username = request.POST.get('username')
        # print(username)
        password = request.POST.get('password')
        # print(password)

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            # print('usuario autenticado')
            return redirect('Home')
        else:
            # print('usuario NO autenticado')
            messages.error(request, 'Usuario o contraseña inválidos !')

    context = {
        "title": "Access Control | 41ZRE",
    }
    return render(request, 'auth/login.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Sessión cerrada exitosamente')
    return redirect('login')

def register(request):
    context = {
        "title": "Registro de usuarios",
    }
    return render(request, 'auth/register.html', context)    

