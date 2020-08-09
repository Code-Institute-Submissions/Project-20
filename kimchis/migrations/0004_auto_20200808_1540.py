# Generated by Django 2.2.6 on 2020-08-08 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kimchis', '0003_auto_20200808_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='kimchi',
            name='tag',
            field=models.ManyToManyField(to='kimchis.Tag'),
        ),
    ]