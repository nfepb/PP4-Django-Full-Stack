# Generated by Django 3.2.16 on 2022-11-21 19:21

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_rename_category_movie_movie_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='directors',
            new_name='director',
        ),
        migrations.AddField(
            model_name='genre',
            name='genre_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlistitem',
            name='movie_status',
            field=models.IntegerField(choices=[(0, 'Not yet watched'), (1, 'Watched')], default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_genre',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.PROTECT, related_name='movie_genre', to='forum.genre'),
            preserve_default=False,
        ),
    ]
