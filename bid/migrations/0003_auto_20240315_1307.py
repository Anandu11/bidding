# Generated by Django 3.1.5 on 2024-03-15 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0002_bid_comment_listings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
