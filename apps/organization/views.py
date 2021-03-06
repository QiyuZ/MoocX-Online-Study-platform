from django.shortcuts import render

# Create your views here.
# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
#from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import CourseOrg, CityDict, Teacher
from organization.forms import UserAskForm
from operation.models import UserFavorite
from courses.models import Course
#from utils.mixin_utils import LoginRequiredMixin
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        #课程机构
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        #城市
        all_citys = CityDict.objects.all()

        #机构搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords))

        #取出筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        #类别筛选
        category = request.GET.get('ct', "")
        if category:
            all_orgs = all_orgs.filter(category=category)\

        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")


        org_nums = all_orgs.count()


        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 5, request=request)

        orgs = p.page(page)
        return render(request, "org-list.html", {
            "all_orgs":orgs,
            "all_citys":all_citys,
            "org_nums": org_nums,
            "city_id": city_id,
            "category": category,
            "hot_orgs": hot_orgs,
            "sort": sort
        })

    class AddUserAskView(View):
        """
        用户添加咨询
        """

        def post(self, request):
            userask_form = UserAskForm(request.POST)
            if userask_form.is_valid():
                user_ask = userask_form.save(commit=True)
                return HttpResponse('{"status":"success"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"something wrong"}', content_type='application/json')