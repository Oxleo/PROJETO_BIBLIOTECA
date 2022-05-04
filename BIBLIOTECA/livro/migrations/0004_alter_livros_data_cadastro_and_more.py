# Generated by Django 4.0.4 on 2022-05-04 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0003_alter_livros_co_autor_alter_livros_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_emprestimo',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='nome_emprestado',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='tempo_duracao',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
