# Generated by Django 2.0.1 on 2018-01-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20180115_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcq_quiz',
            name='mq_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='true_false',
            name='tq_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='txt_question',
            name='txtq_no',
            field=models.IntegerField(default=0),
        ),
    ]
