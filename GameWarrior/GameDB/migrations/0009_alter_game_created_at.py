# Generated by Django 4.2.2 on 2023-06-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameDB', '0008_alter_game_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created_at',
            field=models.DateField(verbose_name='Publication Date'),
        ),
    ]