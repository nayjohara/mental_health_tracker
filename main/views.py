from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245674',
        'name': 'Najya Johara Robby',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
