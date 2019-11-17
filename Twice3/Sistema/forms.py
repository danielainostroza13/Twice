from django import forms

class RegistrarPersonaForm(forms.Form):
    UsuPersona=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombrePersona=forms.CharField(widget=forms.TextInput(),label="Nombre")
    mailPersona=forms.EmailField(label="Email: ")
    fechaNacimiento=forms.DateField(widget=forms.SelectDateWidget(years=range(1910,2001)),label="Fecha de Nacimiento")

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
