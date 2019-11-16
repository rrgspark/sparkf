from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags
from .forms import RegisterForm, CorreoForm, CambiarPassForm
from .models import Usuario



def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return render(request,'main.html')
    else:
        messages.info(request,'Usuario o Contraseña inválidos')
        return render(request,'login.html',{'username':username})


def logout(request):
    auth.logout(request)
    return redirect('login')


def registrar(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request,'registrar.html', {'form':form})


def recuperar_pass(request):
    enviado = False
    if request.method=='POST':
        form = CorreoForm(request.POST)
        if form.is_valid():
            user = User.objects.get(email=request.POST['email'])
            url = request.build_absolute_uri().replace('recuperar_pass','cambiar_pass')
            html = f'''
            <!DOCTYPE html>
            <html>
            <body>
                <br>
                Buen día, {user.first_name}<br><br>
                Has solicitado un cambio de contraseña, para continuar con el proceso sigue el siguiente enlace:<br><br>
                <div style="font-size:20px;text-align:center;">
                    <a href="{url}/{user.pk}">Click Aquí</a>
                </div>
                <br>
                Atentamente<br>
                <b>Equipo Spark Foundation</b>
            </body>
            </html>
            '''
            texto = strip_tags(html)
            send_mail(
                'Cambiar contraseña',
                texto,
                settings.EMAIL_HOST_USER,
                [request.POST['email']],
                fail_silently = False,
                html_message = html
            )
            enviado = True
    else:
        form = CorreoForm()
    return render(request,'recuperar_pass.html',{'form':form, 'enviado':enviado})


def cambiar_pass(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = CambiarPassForm(request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            return redirect('login')
    else:
        form = CambiarPassForm(initial={'email':user.email})
    return render(request,'cambiar_pass.html',{'form':form, 'user_id':user_id})