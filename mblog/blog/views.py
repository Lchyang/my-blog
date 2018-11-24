import markdown

from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list}
    )

def about(request):
    return render(request, 'blog/about.html')

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 支持markdown语法
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ]
                                  )
    return render(request, 'blog/post.html', context={'post':post})