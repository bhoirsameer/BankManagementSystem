# Generated by Django 4.2 on 2023-05-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acctholders', '0004_alter_acctholders_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='acctholders',
            name='acc_typ',
            field=models.CharField(max_length=50, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='acctholders',
            name='balance',
            field=models.CharField(max_length=50, null='True'),
            preserve_default='True',
        ),
    ]
