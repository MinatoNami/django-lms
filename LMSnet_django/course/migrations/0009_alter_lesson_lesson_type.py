# Generated by Django 5.0.1 on 2024-01-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_rename_comment_comment_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(choices=[('article', 'Article'), ('quiz', 'Quiz')], default='article', max_length=20),
        ),
    ]
