# Generated by Django 5.0.4 on 2024-08-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image1', models.ImageField(upload_to='images')),
                ('image2', models.ImageField(null=True, upload_to='images')),
                ('image3', models.ImageField(null=True, upload_to='images')),
                ('image4', models.ImageField(null=True, upload_to='images')),
                ('image5', models.ImageField(null=True, upload_to='images')),
                ('image6', models.ImageField(null=True, upload_to='images')),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
