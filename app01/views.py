from django.shortcuts import redirect, HttpResponse, render
from app01 import models
from app01.myclass import Weibo, Hupu, Twitter,Qidian,Cat,Jlu
from django.utils.safestring import mark_safe
from markdown import markdown
import time


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user_obj = models.Login.objects.filter(email=email).first()
        if user_obj:
            if password == user_obj.password:
                print('qqq')
                return redirect('/home/')
            else:
                return render(request, 'index_reverse.html')
        else:
            return render(request, 'index_reverse.html')

    else:
        return render(request, 'index_reverse.html')


def register(requset):
    if requset.method == "POST":
        username = requset.POST.get('username')
        email = requset.POST.get('email')
        password = requset.POST.get('password')
        res = models.Login.objects.create(username=username, email=email, password=password)
        return redirect('/login/')
    return render(requset, 'index.html')


def home(request):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, type(localtime))
    xingqi = localtime[:3]
    month = localtime[4:7]
    day = localtime[8:10]
    times = localtime[11:19]
    years = localtime[20:]
    queery = models.Jilin.objects.all()
    for que in queery:
        que.title = que.title.replace('&ensp', '')
        que.title = que.title.replace('[doge]', '')
        que.title = que.title[:30] + '...'
    return render(request, 'home.html', locals())


def qidian_refresh(request):
    models.QiDian.objects.all().delete()
    Qidian().qidian()
    print('refresh')
    return redirect('/qidian/')


def qidian(request):

    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, type(localtime))
    xingqi = localtime[:3]
    month = localtime[4:7]
    day = localtime[8:10]
    times = localtime[11:19]
    years = localtime[20:]
    queery = models.Jilin.objects.all()
    for que in queery:
   #     que.content = mark_safe(que.content)
        que.title = que.title.replace('&ensp', '')
        que.title = que.title.replace('[doge]', '')
        que.title = que.title[:30] + '...'
    all = models.QiDian.objects.all()
    return render(request, 'qidian.html', locals())


def twitter(request):
    queery = models.Jilin.objects.all()
    a = Twitter().twitter('')
    return render(request, 'twitter.html', locals())


def weibo_net(request):
    queery = models.Jilin.objects.all()
    for que in queery:
 #       que.content = mark_safe(que.content)
        que.title = que.title.replace('&ensp', '')
        que.title = que.title.replace('[doge]', '')
        que.title = que.title[:30] + '...'

    return render(request, 'home.html', locals())


def hupu(request):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, type(localtime))
    xingqi = localtime[:3]
    month = localtime[4:7]
    day = localtime[8:10]
    times = localtime[11:19]
    years = localtime[20:]
    queery = models.Jilin.objects.all()

    for que in queery:
  #      que.content = mark_safe(que.content)
        que.title = que.title.replace('&ensp', '')
        que.title = que.title.replace('[doge]', '')
        que.title = que.title[:30] + '...'
    hupu_result = Hupu().hupu('https://bbs.hupu.com/liaoning')
    return render(request, 'hupu.html', locals())


def cat(request):
    img = Cat().cat()
    queery = models.Jilin.objects.all()
    return render(request,'cat.html',locals())


def write(request):
    if request.method=="POST":
        contents = request.POST.get('contents')
        print(contents,'sadfasfd')
        return redirect('/home')
    return render(request,'write.html',locals())


def jlu_new(request):
    Jlu().jlu()
    return redirect('/jlu/')
def jlu(request):
    queery = models.Jilin.objects.all()
    return render(request,'jlu.html',locals())