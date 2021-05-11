from django.shortcuts import redirect, HttpResponse, render
from app01 import models
import requests
from app01.myclass import Weibo,Hupu,Twitter
from django.utils.safestring import mark_safe
import time
# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user_obj = models.Login.objects.filter(email=email).first()
        if user_obj:
            if password == user_obj.password:
                print('qqq')
                return redirect('/home/')
            else:
                return render(request,'index_reverse.html')
        else:
            return render(request,'index_reverse.html')

    else:
        return render(request, 'index_reverse.html')


def register(requset):

    if requset.method == "POST":
        username = requset.POST.get('username')
        email = requset.POST.get('email')
        password = requset.POST.get('password')
        res = models.Login.objects.create(username=username, email=email,password=password)
        return redirect('/login/')
    return render(requset, 'index.html')


def userlist(request):
    user_queryset = models.User.objects.all()

    return render(request, 'userlist.html', locals())


def edit_user(request):
    if request.method == "POST":
        nid = request.GET.get('nid')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        models.User.objects.filter(id=nid).update(username=username, password=password)
        return redirect('/userlist/')
    nid = request.GET.get('nid')
    res = models.User.objects.filter(id=nid).first()
    return render(request, 'edit_user.html', locals())


def del_user(request):
    nid = request.GET.get('nid')
    models.User.objects.filter(id=nid).delete()
    return redirect('/userlist/')


def add_file(request):
    if request.method == "POST":
        file_obj = request.FILES.get('file')
        with open(file_obj.name, 'wb') as fp:
            for line in file_obj.chunks():
                fp.write(line)
        return HttpResponse('上传成功')
    return render(request, 'form.html')


from django.views import View


class Mylogin(View):
    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):
        return HttpResponse('POST')


def home(request):

    localtime = time.asctime(time.localtime(time.time()))
    print(localtime,type(localtime))
    xingqi = localtime[:3]
    month = localtime[4:7]
    day = localtime[8:10]
    times = localtime[11:19]
    years = localtime[20:]
    return render(request, 'home.html',locals())


def book_list(request):
    book_queryset = models.Book.objects.all()

    return render(request, 'book_list.html', locals())


def book_add(request):
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    if request.method == "POST":
        print('ok')
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')
        book_obj = models.Book.objects.create(title=title, price=price, publish_data=publish_date,
                                              publish_id=publish_id)
        book_obj.authors.add(*authors_list)
        print(title)
        print('ok')
        return redirect('/book/')
    else:
        print('error')
        return render(request, 'book_add.html', locals())


def book_del(request):
    nid = request.GET.get('nid')
    models.Book.objects.filter(pk=nid).delete()
    return redirect('/book/')


def book_edit(request):
    nid = request.GET.get('nid')
    book_quryset = models.Book.objects.filter(pk=nid)
    publish_queryset = models.Publish.objects.all()
    author_queryset = models.Author.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish_id = request.POST.get('publish')
        authors_list = request.POST.getlist('authors')
        book_obj = models.Book.objects.get(pk=nid)
        models.Book.objects.filter(pk=nid).update(title=title, price=price, publish_data=publish_date,
                                                  publish_id=publish_id)
        return redirect('/book/')

    return render(request, 'book_edit.html', locals())


def author(request):
    dic = Weibo().parse(r'I:\PycharmProjects\django0002\templates\xml\江宁.xml')
    for i in dic:
        content = mark_safe(i['content'])
        models.Weibo.objects.create(user='江宁', title=i['title'], url=i['url'], content=content, jpg=i['href'])
    return redirect('/weibo/')


def study(request):
    return render(request, 'limit.html', locals())


def sys_time(request):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    return render(request,'home.html',locals())


def qidian(request):
    import requests
    import os
    from lxml import html
    etree = html.etree

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'

    }
    count = 0
    models.QiDian.objects.filter().delete()
    for page in range(1, 10):
        url = 'https://www.qidian.com/rank/yuepiao?page=' + str(page)
        page_text = requests.get(url, headers=headers).text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//*[@id="rank-view-list"]/div/ul/li')

        for li in li_list:
            dic = {}
            count += 1
            title = li.xpath('./div[2]/h4/a/text()')[0]
            author = li.xpath('./div[2]/p/a/text()')[0]
            type = li.xpath('./div[2]/p/a[2]/text()')[0]
            href = 'https:' + li.xpath('./div[2]/h4/a/@href')[0]
            status = li.xpath('./div[2]/p/span/text()')[0]
            models.QiDian.objects.create(rank=count, title=title, author=author, type=type, href=href, status=status)
    return redirect('/rank/')


def rank(request):
    all = models.QiDian.objects.all()
    return render(request, 'qidian.html', locals())


def joke(request):
    a = Twitter().twitter('')
    return render(request, 'twitter.html', locals())
def weibo_net(request):
    queery = models.Weibo.objects.all()
    for que in queery:
        que.content = mark_safe(que.content)
        que.title = que.title.replace('&ensp','')
        que.title = que.title.replace('[doge]', '')
        que.title = que.title[:30] + '...'

    return render(request,'home.html',locals())

def hupu(request):
    hupu_result = Hupu().hupu('https://bbs.hupu.com/liaoning')
    return render(request,'hupu.html',locals())