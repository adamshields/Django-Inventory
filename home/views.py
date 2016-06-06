from django.shortcuts import render, render_to_response, RequestContext


# Create your views here.
def home(request):
    print(request.user)
    if request.user.is_authenticated():
        title = 'Welcome'
        myUser = request.user

        # context = {'title': 'Welcome', 'abc': request.user}
    else:
        title = 'Hello New User!'
        myUser = ''
        form = None

    context = {'title': title,
                'myUser': myUser,
                   }

    return render(request, 'home.html', context)