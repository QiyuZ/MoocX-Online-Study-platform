from datetime import datetime
from django.db import models
from users.models import UserProfile
from courses.models import Course

# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="name")
    mobile = models.CharField(max_length=11, verbose_name="mobile")
    course_name = models.CharField(max_length=50, verbose_name="course")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "userAsk"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    # 课程评论
    user = models.ForeignKey(UserProfile, verbose_name="nick_name")
    course = models.ForeignKey(Course, verbose_name="course")
    comments = models.CharField(max_length=200, verbose_name="comments")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "courseComments"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="nick_name")
    fav_id = models.IntegerField(default=0, verbose_name="id")
    fav_type = models.IntegerField(choices=((1, "course"), (2, "org"),(3, "teacher")), default=1, verbose_name="type")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "userFavorite"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name="id")
    message = models.CharField(max_length=500, verbose_name="message")
    has_read = models.BooleanField(default=False, verbose_name="hasRead")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "UserMessage"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="nick_name")
    course = models.ForeignKey(Course, verbose_name="course")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "userCourse"
        verbose_name_plural = verbose_name
