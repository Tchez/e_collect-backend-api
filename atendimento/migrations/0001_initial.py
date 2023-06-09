# Generated by Django 3.2.19 on 2023-05-29 17:48

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=True, verbose_name='Ativo')),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Atendente',
                'verbose_name_plural': 'Atendentes',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='CriarAgendamentos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=True, verbose_name='Ativo')),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('evento', models.CharField(blank=True, max_length=100, null=True)),
                ('data_inicial', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date.today), django.core.validators.MaxValueValidator(datetime.date(2024, 5, 28))], verbose_name='Data inicial')),
                ('hora_inicial', models.TimeField(verbose_name='Hora inicial')),
                ('data_final', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date.today), django.core.validators.MaxValueValidator(datetime.date(2024, 5, 28))], verbose_name='Data final')),
                ('hora_final', models.TimeField(verbose_name='Hora final')),
                ('numero_atendentes', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)], verbose_name='Número de Atendentes Simultâneos')),
                ('tempo_atendimento', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(360), django.core.validators.MinValueValidator(1)], verbose_name='Tempo de Atendimento em MINUTOS')),
                ('atende_feriado', models.BooleanField(default=False, verbose_name='Atende feriado Nacional')),
                ('atende_24_horas', models.BooleanField(default=False, verbose_name='Atende 24 horas')),
                ('atende_final_semana', models.BooleanField(default=False, verbose_name='Atende final de semana')),
            ],
            options={
                'verbose_name': 'Criar Agendamentos',
                'verbose_name_plural': 'Criar Agendamentos',
                'ordering': ['-data_inicial'],
            },
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=True, verbose_name='Ativo')),
                ('deleted', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('evento', models.CharField(blank=True, max_length=100, null=True)),
                ('hora_inicial', models.TimeField(verbose_name='Hora de Início')),
                ('hora_final', models.TimeField(verbose_name='Hora Final')),
                ('data', models.DateField(verbose_name='Data')),
                ('situacao', models.IntegerField(choices=[(0, 'Livre'), (1, 'Agendado'), (2, 'Cancelado'), (3, 'Confirmado'), (4, 'Concluido'), (5, 'Nao Confirmado')], default=0)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuario.usuario', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Atendimento',
                'verbose_name_plural': 'Atendimentos',
                'ordering': ['data', 'hora_inicial', 'hora_final'],
            },
        ),
    ]
