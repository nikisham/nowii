# Generated by Django 3.0.7 on 2022-04-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20220428_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='kurier',
            field=models.PositiveSmallIntegerField(choices=[('О', 'Ольга'), ('А', 'Арсений'), ('В', 'Виталий')], verbose_name='month'),
        ),
    ]
