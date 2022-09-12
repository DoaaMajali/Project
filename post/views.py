from django.shortcuts import redirect, render 
from finalproject.models import finalproject
from finalproject.views import is_logged_in
from post.forms import  CreatePost
from post.models import Post
# Create your views here.

def home_page(request):
    if not is_logged_in(request):
        return redirect ('/finalproject/login')

    return render(request,'home.html', context={'create_post_form': CreatePost} )


def create_post(request):
    if not is_logged_in(request):
        return redirect('/finalproject/login')
    form = CreatePost(request.POST)
    if not form.is_valid():
        messages.error(request, form.errors)
        return redirect('/post/home')
        
    title = form.cleaned_data['title']
    content = form.cleaned_data['content']
    author = finalproject.objects.get(username=request.session['username'])
    
    new_post = Post(title=title, content=content, author=author)
    new_post.save()
    messages.success(request, 'Created successfully')
    return redirect('/post/home')   