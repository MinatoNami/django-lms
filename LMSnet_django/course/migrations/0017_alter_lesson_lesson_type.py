# Generated by Django 5.0.1 on 2024-02-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_course_created_by_alter_lesson_lesson_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(choices=[('quiz', 'Quiz'), ('video', 'Video'), ('article', 'Article')], default='article', max_length=20),
        ),
    ]
