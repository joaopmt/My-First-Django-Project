from django.shortcuts import render


# View for index (home) page.
def index(request):
    return render(request, 'personal/home.html')


# View for contact page.
def contact(requests):
    # Return the html page to render and a dict with some strings to be used in it
    return render(requests, 'personal/basic.html', {'content': ['To contact me, please email me',
                                                                'joaopedrocmartins39@hotmail.com']})
