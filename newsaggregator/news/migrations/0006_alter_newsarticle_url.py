# Generated by Django 5.0.3 on 2024-03-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_newsarticle_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='url',
            field=models.URLField(),
        ),
    ]
