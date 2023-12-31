# Generated by Django 4.2.4 on 2023-08-31 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0003_remove_problem_raiting_problem_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(max_length=255, verbose_name='Message_id')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'request',
                'verbose_name_plural': 'request',
            },
        ),
    ]
