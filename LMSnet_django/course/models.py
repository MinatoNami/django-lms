from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Course(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        return 'http://bulma.io/images/placeholders/1280x960.png'
    
class Lesson(models.Model):
    DRAFT='draft'
    PUBLISHED='published'

    CHOICES_STATUS = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )

    ARTICLE='article'
    QUIZ='quiz'

    CHOICES_LESSON_TYPE = {
        (ARTICLE, 'Article'),
        (QUIZ, 'Quiz'),
    }

    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=PUBLISHED)
    lesson_type = models.CharField(max_length=20, choices=CHOICES_LESSON_TYPE, default=ARTICLE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name