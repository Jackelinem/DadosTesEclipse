# Generated by Django 2.0.5 on 2018-05-23 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnioLectivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anioLectivo', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('contrasenia', models.CharField(max_length=50)),
                ('confirmpass', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstudianteCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cupos', models.IntegerField()),
                ('codigo_alec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.AnioLectivo')),
                ('codigo_cur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Curso')),
                ('codigo_est', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Evalucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('codigo_est_cur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.EstudianteCurso')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=255)),
                ('codigo_eval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Evalucion')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('contrasenia', models.CharField(max_length=50)),
                ('confirmpass', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.CharField(max_length=255)),
                ('validacion', models.CharField(max_length=50)),
                ('codigo_pre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='TipoPregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pregunta',
            name='codigo_tip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.TipoPregunta'),
        ),
        migrations.AddField(
            model_name='historial',
            name='codigo_pre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Pregunta'),
        ),
        migrations.AddField(
            model_name='estudiantecurso',
            name='codigo_profe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Profesor'),
        ),
    ]