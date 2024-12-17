from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blogging.models import Post

# Create your views here.

"""
Commented out to create a class-based view
# rewrite our view:

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)
"""


class PostListView(ListView):
    # model = Post
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )  # apply both 'filter' and 'order_by' methods to 'Post.objects' query set
    template_name = "blogging/list.html"


"""
Commented out to make a class-based view

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
"""


class PostDetailView(DetailView):
    # model = Post
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"
