from django.shortcuts import render


# View for index (home) page.
def index(request):
    return render(request, 'homepage/home.html')  # from templates
