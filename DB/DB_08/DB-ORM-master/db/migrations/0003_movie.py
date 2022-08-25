# Generated by Django 4.0.6 on 2022-08-25 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('opening_date', models.DateField()),
                ('running_time', models.IntegerField()),
                ('screening', models.BooleanField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.director')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.genre')),
            ],
        ),
    ]