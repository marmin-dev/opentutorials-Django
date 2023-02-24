from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
post_id = 0
post = []


def PageTemplate(post):
    return f'''
    <html>
    <body>
    <link rel="stylesheet" href="style.css">
    <h1 class="header"><a href ="/">Post Api</a></h1>
    <form action"/create/" method="post">
    <p><input type ="text" name="title" placeholder="Title"></p>
    <p><textarea placeholder="content" name="body"></textarea></p>
    </form>
    </body>
    </html>
    '''


def index(request):
    post = ""
    return HttpResponse(PageTemplate(post))
