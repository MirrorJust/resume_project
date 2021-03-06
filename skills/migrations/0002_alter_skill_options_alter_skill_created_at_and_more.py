# Generated by Django 4.0.4 on 2022-06-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['created_at'], 'verbose_name': 'Навык', 'verbose_name_plural': 'Навыки'},
        ),
        migrations.AlterField(
            model_name='skill',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Добавлн'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Навык поулчен?'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name_skill',
            field=models.CharField(max_length=50, verbose_name='Название навыка'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
    ]
