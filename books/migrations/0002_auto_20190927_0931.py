# Generated by Django 2.1.3 on 2019-09-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='goodreads_book_id',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='image_location',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='image_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='original_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
