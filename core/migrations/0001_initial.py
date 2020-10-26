# Generated by Django 2.2 on 2020-10-26 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=25)),
                ('apellido', models.CharField(default='', max_length=25)),
                ('dni', models.IntegerField()),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('club', models.CharField(default='Introduzca nombre del club', max_length=35, primary_key=True, serialize=False)),
                ('division', models.CharField(default='Introduzca division del club', max_length=1)),
                ('cantJugadores', models.IntegerField()),
                ('amonestados', models.IntegerField()),
                ('expulsados', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('idError', models.CharField(default='', max_length=8, primary_key=True, serialize=False)),
                ('numLinePerdidos', models.IntegerField()),
                ('numScrumPerdidos', models.IntegerField()),
                ('numPenalesEnContra', models.IntegerField()),
                ('numPelotasCaidas', models.IntegerField()),
                ('numConversionesErrados', models.IntegerField()),
                ('numTaclesErrados', models.IntegerField()),
                ('numPaseFoword', models.IntegerField()),
                ('numDropErrados', models.IntegerField()),
                ('numMaulErrados', models.IntegerField()),
                ('numRuckErrados', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=25)),
                ('apellido', models.CharField(default='', max_length=25)),
                ('dni', models.IntegerField()),
                ('tel', models.IntegerField()),
                ('posicion', models.CharField(default='', max_length=50)),
                ('asistenciaComp', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('amonestado', models.BooleanField(default=False)),
                ('expulsado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('idPartido', models.CharField(default='', max_length=8, primary_key=True, serialize=False)),
                ('numLine', models.IntegerField()),
                ('numScrum', models.IntegerField()),
                ('numPenales', models.IntegerField()),
                ('tri', models.IntegerField()),
                ('numConversiones', models.IntegerField()),
                ('numDrop', models.IntegerField()),
                ('numTacles', models.IntegerField()),
                ('numMaul', models.IntegerField()),
                ('numRuck', models.IntegerField()),
                ('cantPases', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Equipo')),
                ('error', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Error')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Partido')),
            ],
        ),
    ]
