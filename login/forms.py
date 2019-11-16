from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'campo-generico', 'placeholder':'Usuario'}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'campo-generico', 'placeholder':'Contraseña'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'campo-generico', 'placeholder':'Confirmar contraseña'}), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'campo-generico', 'placeholder':'Nombre'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'campo-generico', 'placeholder':'Apellidos'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'campo-generico', 'placeholder':'Correo Electrónico'}), required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            User._default_manager.get(username=username)
            raise forms.ValidationError( 
                'El usuario ya existe.',
                code='username_exists',
            )
        except User.DoesNotExist:
            return username


    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            User._default_manager.get(email=email)
            raise forms.ValidationError( 
                'El correo electrónico ya está en uso.',
                code='email_exists',
            )
        except User.DoesNotExist:
            return email


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'La contraseña no coincide.',
                code='password_mismatch',
            )
        return password2


class CorreoForm(forms.Form):
    email = forms.EmailField(
        label="Ingresa el correo electrónico de tu cuenta", 
        widget= forms.EmailInput(attrs={'class':'campo-generico'}),
        required=True, error_messages={'invalid': 'Ingresa un correo electrónico válido.'}
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            User._default_manager.get(email=email)
            return email
            
        except User.DoesNotExist:
            raise forms.ValidationError( 
                'El correo electrónico no está registrado.',
                code='email_exists',
            )


class CambiarPassForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'disabled_email campo-generico','readonly':True}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autofocus':True, 'class':'campo-generico'}), label='Nueva contraseña', required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'campo-generico'}), label='Confirmar contraseña', required=True)

    class Meta:
        fields = (
            'email',
            'password1',
            'password2'
        )

    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'La contraseña no coincide.',
                code='password_mismatch'
            )
        return password2
