import xadmin
from .models import Course, Lesson, Video, Resource
from organization.models import CourseOrg


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time'] # foreignkey use __(两个下划线)


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'duration', 'student']
    search_fields = ['name', 'desc', 'detail', 'degree', 'student']
    list_filter = ['name', 'desc', 'detail', 'degree', 'duration', 'student']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class ResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(Resource, ResourceAdmin) 