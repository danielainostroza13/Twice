# Generated by Django 2.1.3 on 2019-11-16 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nombrePersona', models.CharField(max_length=30)),
                ('apellidoPersona', models.CharField(max_length=30)),
                ('fechaNacimiento', models.DateField()),
                ('numeroFono', models.CharField(blank=True, max_length=10, null=True)),
                ('regionPersona', models.CharField(max_length=50)),
                ('tipoPersona', models.CharField(default='Usuario', max_length=50)),
            ],
        ),
    ]