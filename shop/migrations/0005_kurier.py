# Generated by Django 3.0.7 on 2022-04-27 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20220427_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kurier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=150, verbose_name='Имя')),
                ('cost', models.TextField(max_length=150, verbose_name='Описание')),
                ('img', models.ImageField(blank=True, upload_to='photos/kurier', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Курьер',
                'verbose_name_plural': 'Курьеры',
            },
        ),
    ]
