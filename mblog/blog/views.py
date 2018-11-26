import markdown

from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from .models import Post


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 10

# def index(request):
#     post_list = Post.objects.all().order_by('-create_time')
#
#     return render(request, 'blog/index.html', context={'post_list': post_list}
#     )

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
    # 调用increate_views 阅读量+1
    post.increase_views()

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list,
    }

    return render(request, 'blog/post.html', context=context)