# Generated by Django 3.0.7 on 2022-04-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20220428_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='kurier',
            field=models.CharField(choices=[('', ''), ('О', 'Ольга'), ('А', 'Арсений'), ('В', 'Виталий')], default=None, max_length=1, null=True),
        ),
    ]
