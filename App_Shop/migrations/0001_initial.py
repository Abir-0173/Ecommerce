# Generated by Django 4.2.14 on 2024-10-11 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(upload_to='Product')),
                ('name', models.CharField(max_length=264)),
                ('preview_text', models.TextField(max_length=200, verbose_name='Previews Text')),
                ('detail_text', models.TextField(max_length=1000, verbose_name='Descriptin')),
                ('old_price', models.FloatField(default=0.0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='App_Shop.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
