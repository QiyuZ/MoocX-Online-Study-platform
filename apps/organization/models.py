from django.db import models
from datetime import datetime
# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name="city")
    add_time = models.DateTimeField(default=datetime.now)
    desc = models.CharField(max_length=200, verbose_name="cityDesc")

    class Meta:
        verbose_name = "city"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name="org")
    clicks = models.IntegerField(default=0, verbose_name="click")
    desc = models.TextField(verbose_name="orgDesc")
    fav_nums = models.IntegerField(default=0, verbose_name="favNum")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="pic", max_length=120)
    address = models.CharField(max_length=150, verbose_name="address")
    city = models.ForeignKey(CityDict, verbose_name="city")

    class Meta:
        verbose_name = "organization"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name="org")
    name = models.CharField(max_length=50, verbose_name="teacherName")
    work_years = models.IntegerField(default=0, verbose_name="workYears")
    work_company = models.CharField(max_length=50, verbose_name="company")
    work_pos = models.CharField(max_length=50, verbose_name="pos")
    points = models.CharField(max_length=150, verbose_name="character")
    clicks = models.IntegerField(default=0, verbose_name="click")
    fav_nums = models.IntegerField(default=0, verbose_name="favNum")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "teacher"
        verbose_name_plural = verbose_name