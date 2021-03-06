# Generated by Django 2.0.1 on 2018-01-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20180115_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcq_quiz',
            name='mq_no',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='mcq_quiz',
            name='option1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mcq_quiz',
            name='option2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mcq_quiz',
            name='option3',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='mcq_quiz',
            name='option4',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='results',
            name='a1',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='results',
            name='a10',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='results',
            name='a2',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='results',
            name='a3',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='results',
            name='a4',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='results',
            name='a5',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='results',
            name='a6',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='results',
            name='a7',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='results',
            name='a8',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='results',
            name='a9',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='true_false',
            name='tfoption1',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='true_false',
            name='tfoption2',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='true_false',
            name='tq_no',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='txt_question',
            name='txtoption1',
            field=models.CharField(blank='True', max_length=100, null='True'),
        ),
        migrations.AlterField(
            model_name='txt_question',
            name='txtq_no',
            field=models.CharField(max_length=5),
        ),
    ]
