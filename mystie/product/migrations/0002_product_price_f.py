# Generated by Django 4.0.6 on 2022-07-17 09:48

from django.db import migrations, models
import django.forms.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_f',
            field=models.CharField(default='<django.db.models.fields.PositiveIntegerField>$', max_length=200, verbose_name=django.forms.widgets.HiddenInput),
        ),
    ]
