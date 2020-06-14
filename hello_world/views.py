from django.shortcuts import get_object_or_404, render
from hello_world.models import Post
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def actors1(request):
    return render(request, 'actors1.html', {})

def actors2(request):
    return render(request, 'actors2.html', {})

def comments(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'comments.html', context)

def create (request):
    if request.method == "POST":
        obj = Post(title=request.POST.get("title"),
                    text=request.POST.get("text"))
        obj.save()
        return render(request, "success.html")
    return render(request, "create.html")

def detail(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return render(request, "create.html")
    print("POST_ID:", post_id)
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, 'detail.html', context);
