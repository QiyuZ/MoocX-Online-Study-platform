from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="Nick name", default="")
    birthday = models.DateField(verbose_name="Birthday", null=True, blank=True)
    gender = models.CharField(choices=(("male", "male"), ("female", "female")), default="female", max_length=10)
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "userMessage"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="code")
    email = models.EmailField(max_length=50, verbose_name="email")
    send_type = models.CharField(choices=(("register", "register"), ("forget", "forget")), max_length=20)
    send_time = models.DateTimeField(default=datetime.now)
    #上面的now不要括号，加括号是编译的时间，不加是实例化时的时间

    class Meta:
        verbose_name = "emailVerify"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="images", max_length=100)
    url = models.URLField(max_length=200, verbose_name="url")
    index = models.IntegerField(default=100, verbose_name="order")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "bannerPic"
        verbose_name_plural = verbose_name

