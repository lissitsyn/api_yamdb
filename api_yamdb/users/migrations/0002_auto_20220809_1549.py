# Generated by Django 2.2.16 on 2022-08-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('verification_code', models.CharField(max_length=4, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Обычный пользователь'), ('moderator', 'Модератор'), ('admin', 'Админ')], default='user', max_length=20),
        ),
    ]
