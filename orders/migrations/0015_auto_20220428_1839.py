# Generated by Django 3.0.7 on 2022-04-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20220428_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='kurier',
            field=models.CharField(blank=True, choices=[('О', 'Ольга'), ('А', 'Арсений'), ('В', 'Виталий')], max_length=100),
        ),
    ]