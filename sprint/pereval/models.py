from django.db import models

# составляем классы для заполнения информации о перевале


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    fam = models.CharField(max_length=50, verbose_name='Фамилия')
    otc = models.CharField(max_length=50, verbose_name='Отчество')
    email = models.CharField(max_length=50, verbose_name='Электронная почта')
    tel = models.CharField(max_length=50, verbose_name='Телефон')


class Pereval(models.Model):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'
    TYPE = [
        (new, 'Новый'),
        (pending, 'Ожидается'),
        (accepted, 'Принят'),
        (rejected, 'Отклонен'),
    ]

    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Название')
    beautyTitle = models.CharField(max_length=50, default=None, verbose_name='Форма рельефа')
    other_titles = models.CharField(max_length=50, null=True, blank=True, verbose_name='Другое название')
    connect = models.TextField(null=True, blank=True, verbose_name='Связь')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    coords = models.OneToOneField('Coords', on_delete=models.CASCADE, verbose_name='Координаты')
    level = models.ForeignKey('Level', on_delete=models.CASCADE, verbose_name='Уровень')
    status = models.CharField(max_length=10, choices=TYPE, default=new, verbose_name='Статус')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')


class Coords(models.Model):
    width = models.FloatField(max_length=50, verbose_name='Широта')
    longitude = models.FloatField(max_length=50, verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')


class Images(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    data = models.URLField(null=True, blank=True, verbose_name='Изображение')
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, verbose_name='Перевал-фото')


class Level(models.Model):
    winter = models.CharField(max_length=2, verbose_name='Зима', null=True, blank=True)
    summer = models.CharField(max_length=2, verbose_name='Лето',  null=True, blank=True)
    autumn = models.CharField(max_length=2, verbose_name='Осень',  null=True, blank=True)
    spring = models.CharField(max_length=2, verbose_name='Весна',   null=True, blank=True)

