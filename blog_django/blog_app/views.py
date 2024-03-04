from django.shortcuts import render, get_object_or_404, redirect
from blog_app.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog_app.forms import PostForm


def posts_list(request):
    posts = Post.objects.all().order_by('id')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    print(posts, type(posts))
    return render(request, 'post_list.html', context={'posts': posts,
                                                      'page': page})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect('post_list')
        else:
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, "create_post.html", {'form': form})