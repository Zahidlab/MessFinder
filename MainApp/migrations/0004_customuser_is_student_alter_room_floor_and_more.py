# Generated by Django 4.0.2 on 2022-03-17 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_remove_mess_picture_remove_room_picture_messimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.IntegerField(choices=[(2, 'CSE'), (3, 'EEE'), (4, 'ECE'), (1, 'Agriculture'), (5, 'DVM'), (6, 'Physics')]),
        ),
    ]