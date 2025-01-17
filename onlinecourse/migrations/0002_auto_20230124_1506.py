# Generated by Django 3.1.3 on 2023-01-24 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(default='choice', max_length=60)),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(to='onlinecourse.Choice')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.enrollment')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='question', max_length=200)),
                ('grade_point', models.IntegerField(default=0)),
                ('for_course', models.ManyToManyField(to='onlinecourse.Course')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='for_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
        ),
    ]
