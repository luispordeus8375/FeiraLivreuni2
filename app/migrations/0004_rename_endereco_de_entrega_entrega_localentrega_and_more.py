# Generated by Django 4.2.3 on 2024-04-18 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_data_de_entrega_entrega_data_de_entrega_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrega',
            old_name='endereco_de_entrega',
            new_name='localentrega',
        ),
        migrations.RenameField(
            model_name='entrega',
            old_name='nome_do_cliente',
            new_name='nomecliente',
        ),
        migrations.RenameField(
            model_name='entrega',
            old_name='data_de_entrega',
            new_name='prazoentrega',
        ),
        migrations.RenameField(
            model_name='frutas',
            old_name='quantidade_disponivel',
            new_name='estoquedisponivel',
        ),
        migrations.RenameField(
            model_name='frutas',
            old_name='nome_do_produto',
            new_name='nomeproduto',
        ),
        migrations.RenameField(
            model_name='frutas',
            old_name='preco_unitario',
            new_name='precounidade',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='entrega',
            new_name='entregaitem',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='quantidade',
            new_name='estoqueitem',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='nome_do_produto',
            new_name='nomeitem',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='preco_unitario',
            new_name='precounidadeitem',
        ),
        migrations.RenameField(
            model_name='pagamento',
            old_name='metodo_de_pagamento',
            new_name='formapagamento',
        ),
        migrations.RenameField(
            model_name='pagamento',
            old_name='valor_total',
            new_name='total',
        ),
        migrations.RenameField(
            model_name='verduras',
            old_name='quantidade_disponivel',
            new_name='estoquedisponivel',
        ),
        migrations.RenameField(
            model_name='verduras',
            old_name='nome_do_produto',
            new_name='nomeproduto',
        ),
        migrations.RenameField(
            model_name='verduras',
            old_name='preco_unitario',
            new_name='precounidade',
        ),
    ]
