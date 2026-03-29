from django.shortcuts import render

posts = [
    {
        "author":"Manoj Pun",
        "title":"Blog Post 1",
        "content":"First post content",
        "date_posted":"March 29, 2026"
    },
    {
        "author":"David Pun",
        "title":"Blog Post 2",
        "content":"Second post content",
        "date_posted":"March 29, 2026"
    },
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html",context,)

def about(request):
    return render(request, "blog/about.html",{"title":"About"})