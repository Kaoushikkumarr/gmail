from django.shortcuts import render

# Create your views here.
def home(request):
    # posts = Post.objects.order_by('-pub_date')
    return render(request, 'home.html')
