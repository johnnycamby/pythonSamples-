from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.template.context_processors import csrf
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from article.forms import ArticleForm, CommentForm
from article.models import Article, Comment
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from haystack.query import SearchQuerySet
from django.template import RequestContext
from django.contrib import messages



# Create your views here.
from pystudy import settings


def articles(request):
    return render(request, 'article/articles.html',{'articles': Article.objects.all()})
    #return render_to_response('article/articles.html',{'articles': Article.objects.all()} )

def article(request, article_id=1):
    return render(request,'article/article.html', {'article': Article.objects.get(id = article_id)})
'''
def edit(request, article_id):
    if article_id:
        art = Article.objects.get(id=article_id)
        count = art.likes
        count += 1
        art.likes = count
        art.save()
    redirect('get_article')
    #return render(request,'article/edit.html', {'edit': Article.objects.get(id = article_id)})
'''

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your Article was added!")
            return redirect('all_articles')
    else:
        form = ArticleForm()
    return render(request, 'article/create_article.html',{'form': form})

def delete(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    article_id = c.article.id
    c.delete()
    messages.add_message(request, settings.DELETE_MESSAGE, "Your Comment was deleted!")
    #return HttpResponseRedirect('get_article')
    return redirect('get_article', article_id)


def comment(request, article_id):
    art = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.comment_date = timezone.now()
            comm.article = art
            comm.save()
            messages.success(request, "Your Comment was added")
            return redirect('all_articles')
    else:
        form = CommentForm()
        args = {}
        args.update(csrf(request))
        args['article'] = art
        args['form'] = form
    return render(request, 'comment/comment.html', args)
'''
def search(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''

    articles = Article.objects.filter(title__contains=search_text)
    return render(request,'search/ajax_search.html', {'articles': articles})
'''
def search(request):
    articles = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text',''))
    return render(request,'search/ajax_search.html', {'articles': articles})



