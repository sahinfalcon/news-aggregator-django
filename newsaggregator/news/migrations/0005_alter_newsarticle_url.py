# Generated by Django 5.0.3 on 2024-03-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_newsarticle_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
