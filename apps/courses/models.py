from django.db import models
from datetime import datetime
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    desc = models.CharField(max_length=100, verbose_name="describe")
    detail = models.TextField(verbose_name="detail")
    degree = models.CharField(choices=(("easy", "easy"), ("medium", "medium"), ("hard","hard")), max_length=5)
    duration = models.IntegerField(default=0, verbose_name="duration_mins")
    student = models.IntegerField(default=0, verbose_name="students")
    fav_nums = models.IntegerField(default=0, verbose_name="fav_students")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name="Pic", max_length=100)
    clicks = models.IntegerField(default=0, verbose_name="clicks")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="course")
    name = models.CharField(max_length=100, verbose_name="chapterName")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="addTime")

    class Meta:
        verbose_name = "lesson"
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="chapter")
    name = models.CharField(max_length=100, verbose_name="videoName")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "video"
        verbose_name_plural = verbose_name


class Resource(models.Model):
    course = models.ForeignKey(Course, verbose_name="name")
    name = models.CharField(max_length=100, verbose_name="rescourceName")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="addTime")
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name="resourceFile", max_length=100)

    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = verbose_name
