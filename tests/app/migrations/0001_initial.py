# Generated by Django 2.2.4 on 2019-09-02 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255, verbose_name='header')),
                ('order', models.PositiveIntegerField(default=0, editable=False, verbose_name='order')),
            ],
            options={
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
                'ordering': ['order'],
            },
        ),
    ]
