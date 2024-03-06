from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'registro exitoso!')
                else:
                    return HttpResponse('Cuenta bloqueada!')
            else:
                return HttpResponse('Algo salió mal!')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def index(request):
    return render(request, 'account/index.html')

@login_required
def panel_socio(request):
    return render(request, 'account/panel_socio.html',
                           {'section': 'panel_socio'})

@login_required
def logout(request):
    return render(request, 'account/logged_out.html')





