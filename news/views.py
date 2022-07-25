from django.shortcuts import render, redirect
from .form import NewsForm
from .models import News_post
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def news_main(request):
    context = {'news_main': News_post.objects.all()}
    return render(request, "news.html", context)


def news_detail(request, id):
    context = {'news_detail': News_post.objects.filter(pk=id)}
    return render(request, "news_detail.html", context)

@staff_member_required(login_url = '/login/')
def news_list(request):
    context = {'news_list': News_post.objects.all()}
    return render(request, "news_list.html", context)

@staff_member_required(login_url = '/login/')
def news_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = NewsForm()
        else:
            news = News_post.objects.get(pk=id)
            form = NewsForm(instance=news)
        return render(request, "news_form.html", {'form': form})
    else:
        if id == 0:
            form = NewsForm(request.POST)
        else:
            news = News_post.objects.get(pk=id)
            form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
        return redirect('/news/list')

@staff_member_required(login_url = '/login/')
def news_delete(request, id):
    news = News_post.objects.get(pk=id)
    news.delete()
    return redirect('/news/list')