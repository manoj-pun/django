from django.shortcuts import render

posts = [
    {
        "author":"Manoj Pun",
        "title":"Blog Post 1",
        "content":"First Post Content",
        "date_posted":"August 27,2025"
    },
    {
        "author":"David Pun",
        "title":"Blog Post 2",
        "content":"Second Post Content",
        "date_posted":"August 28,2025"
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title":"About"})