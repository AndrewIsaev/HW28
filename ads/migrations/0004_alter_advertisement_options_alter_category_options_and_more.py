# Generated by Django 4.1.6 on 2023-02-12 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('ads', '0003_advertisement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='address',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='author',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='author_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ads.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]