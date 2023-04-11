from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        verbose_name='Группы',
        help_text='Название группы',
        max_length=200
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        db_index=True,
        verbose_name='слаг для URL'
    )
    description = models.TextField(
        max_length=2000,
        verbose_name='Описание группы',
        help_text='Описание группы'
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Введите в окне текст нового поста'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='По дате изменения',
        help_text='Дата изменения'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
        help_text='Выбирете автора из списка'
    )
    group = models.ForeignKey(
        Group,
        help_text='Выбирете группу из списка',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Группа'
    )
    image = models.ImageField(
        help_text='Выберете картинку',
        verbose_name='Картинка',
        upload_to='posts/',
        blank=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        null=True,
        verbose_name='Комментарий',
        on_delete=models.CASCADE,
        help_text='Комментарий',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
        help_text='Автор'
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Введите в окне текст комментария'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Коментарий был создан',
        help_text='Время создания комментария',
    )

    def __str__(self):
        return self.text[:30]
