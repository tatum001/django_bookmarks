#-*- coding:utf-8 -*-
# Create your views here.
from django.http import HttpResponse

def main_page(request):
    template = get_template('main_page.html')
    variables = Context({
                         'head_title': '장고 북마크',
                         'page_title': '장고 북마크에 오신 것을 환영합니다',
                         'page_body': '북마크를 저장하고 공유하세요',                     
    })
    output = template.render(variables)
    return HttpResponse(output)
    