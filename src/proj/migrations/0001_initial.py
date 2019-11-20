# Generated by Django 2.2.4 on 2019-11-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
