# Generated by Django 3.0.7 on 2022-04-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20220427_1329'),
        ('orders', '0004_order_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'Купон', 'verbose_name_plural': 'Купоны'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='entrance',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='fio',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='flat',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='floor',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='home',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='kurier',
            field=models.ManyToManyField(to='shop.Kurier'),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='street',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
