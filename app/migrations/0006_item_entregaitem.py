# Generated by Django 4.2.3 on 2024-04-18 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_item_entregaitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='entregaitem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='app.entrega'),
        ),
    ]
