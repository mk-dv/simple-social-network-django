import os
import PIL

from django.contrib.auth import get_user_model
# from tempfile import NamedTemporaryFile
# from django.core.files.base import UploadedFile
from django.core.files.temp import NamedTemporaryFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from account.models import Profile


# Вместо получения профиля/указания литералов несколько раз можно
# использовать поля класса или даже синглтон(хотя он здесь явно избыточен)
# но я не уверен как это отразится на чистоте тестов.
class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()

        test_user = User.objects.create_user(
            username='test_username',
            first_name='test_firstname',
            email='test_email@example.com',
            password='test_password'
        )
        # test_user.set_password('testpass')
        # test_user.save()
        # TODO(mk-dv): Заполнить профиль.

        # Создание изображения
        image = PIL.Image.new('RGB',(100,100),color=(73,22,30))
        # image_file = NamedTemporaryFile(suffix='.jpg')
        # image.save(image_file)
        import io
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='JPEG')
        profile = Profile.objects.create(
            user = test_user,
            photo = SimpleUploadedFile(name='test_img.jpg',
                                       content=img_bytes.read(),
                                   content_type='image/jpeg')
        )
        print()

    def test_date_of_birth_label(self):
        profile = Profile.objects.get(pk=1)
        # Получение метаданных поля для получения необходимых значений. Мы не
        # можем получить поле verbose_name напрямую через
        # `profile.date_of_birth.verbose_name,потому что author.first_name
        # является
        # строкой.Вместо этого,нам надо использовать атрибут _meta объекта
        # автора для получения того экземпляра поля,который будет
        # использоваться для получения дополнительной информации.
        field_label = profile._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label,'date of birth')

    def test_str_method(self):
        profile = Profile.objects.get(pk=1)
        str_profile = str(profile)
        self.assertEquals('Profile for user test_username', str_profile)
    # def test_user_exist(self):
    #     User = get_user_model()
    #     test_user = User.objects.get(pk=1)
    #     self.assertEqual(test_user.username, 'test_username')



    # def test_Profile_with_image(self):
    #     profile = Profile.objects.get(pk=1)
    #     self.assertIsNotNone(profile.photo)
    #     # тут еще проверить что файл на диске
    #     os.remove(Profile.photo.file)
