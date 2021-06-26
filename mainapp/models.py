from django.db import models
from django.conf import settings

# 1. Task
# 3. Comment
# 5. Category
# 6. Chat

from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название задачи", blank=True, null=True)
    content = models.TextField(max_length=3500, verbose_name="Условие задачи")
    image = models.ImageField(blank=True, null=True)
    resource = models.CharField(max_length=500, blank=True, verbose_name="Источник/название олимпиады")
    year = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Год")
    grade = models.PositiveSmallIntegerField(verbose_name="Класс", blank=True, null=True)
    difficulty_level = models.PositiveSmallIntegerField(verbose_name="Уровень сложности", blank=True, null=True)
    answer = models.CharField(max_length=500, blank=True, null=True, verbose_name="Ответ")
    chat = models.OneToOneField('Chat', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(
        'Category',
        verbose_name="Раздел",
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse('task', kwargs={'category_slug': self.category.slug, 'task_id': self.id})

    def get_name(self):
        name = ""
        if self.resource:
            name += self.resource + " "
        if self.grade:
            name += str(self.grade) + "кл. "
        if self.year:
            name += str(self.year) + "г."
        return name

    class Meta:
        ordering = ['difficulty_level', 'grade', 'year']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название раздела")
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def get_num_task_by_cat(self):
        return len(Task.objects.filter(category_id=self.id))

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.CASCADE)
    text = models.TextField(max_length=1500)
    timestamp_create = models.DateTimeField(auto_now_add=True)
    timestamp_update = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(null=True)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self',
        verbose_name="Родительский комментарий",
        blank=True,
        null=True,
        related_name='comment_children',
        on_delete=models.CASCADE

    )

    def __str__(self):
        return "Message text"

    class Meta:
        ordering = ['likes', 'timestamp_create']


class Chat(models.Model):


    def __str__(self):
        return "Chat"
