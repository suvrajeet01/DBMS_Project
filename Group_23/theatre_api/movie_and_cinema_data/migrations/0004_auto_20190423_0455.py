# Generated by Django 2.1.4 on 2019-04-22 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_and_cinema_data', '0003_movie_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_price_and_time',
            name='language',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket_price_and_time',
            name='screen_type',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
