'''
Модель пользователя dj содержит min набор полей. Для сохранения доп данных
создадим модель профиля со ссылкой OneToOne
'''
from django.db import models
from django.conf import settings


# Мне кажется довольно логичным, отделять необязательную информацию профиля от,
# собственно, пользователя(и даже не кажется, что стандартная модель User dj -
# СОДЕРЖ какие-либо лишние данные.
class Profile(models.Model):
    # Чтобы код не зависел от конкретного пользователя - используем
    # [get_user_model(), возвращающую]: бредни вроде
    # модель указанную в settins.AUTH_USER_MODEL

    # Связываем новые данные с конкретными пользователями
    # Связаные с пользователем данные будут удалены при удалении User
    # (а наоборот?)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    # Требует Pillow, иначе запускающийся SystemCheck выдаст ошибку
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
