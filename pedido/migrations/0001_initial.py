# Generated by Django 4.2.3 on 2023-07-26 16:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('total', models.FloatField()),
                ('troco', models.CharField(blank=True, max_length=20)),
                ('pagamento', models.CharField(max_length=20)),
                ('ponto_referencia', models.CharField(blank=True, max_length=2000)),
                ('data', models.DateTimeField(default=datetime.datetime(2023, 7, 26, 13, 53, 23, 788004))),
                ('cep', models.CharField(blank=True, max_length=50)),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(blank=True, max_length=200)),
                ('telefone', models.CharField(max_length=30)),
                ('entregue', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
                ('adicionais', models.TextField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
    ]
