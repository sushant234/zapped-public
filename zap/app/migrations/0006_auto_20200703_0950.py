# Generated by Django 3.0.6 on 2020-07-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('meta', models.TextField()),
                ('anim_txt1', models.CharField(max_length=100)),
                ('anim_txt2', models.CharField(max_length=100)),
                ('anim_txt3', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='img_alt',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='website',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='img_alt',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
