#-*- coding:utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

def main_page(request):
    template = get_template('main_page.html')
    variables = Context({
                         'head_title': '장고 북마크',
                         'page_title': '장고 북마크에 오신 것을 환영합니다',
                         'page_body': '북마크를 저장하고 공유하세요',                     
    })
    output = template.render(variables)
    return HttpResponse(output)
    
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('사용자를 찾을 수 없습니다')
    
    bookmarks = user.bookmark_set.all()
    
    template = get_template('user_page.html')
    variables = Context({
                         'username': username,
                         'bookmarks': bookmarks
    })
    output = template.render(variables)
    return HttpResponse(output)
