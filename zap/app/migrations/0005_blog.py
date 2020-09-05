# Generated by Django 3.0.6 on 2020-06-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_addescbox_dsdescbox_mldescbox_wddescbox'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgs', models.ImageField(default='Null', upload_to='pics')),
                ('heading', models.CharField(max_length=500)),
                ('summary', models.CharField(max_length=1000)),
                ('desc', models.TextField()),
                ('author', models.CharField(default='ZAPPAD', max_length=100)),
            ],
        ),
    ]
