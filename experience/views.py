from django.shortcuts import render
from .models import Experience

# Create your views here.
def experience_list(request):
    experience = Experience.objects.all()
    return render(request, 'experience/list.html', {'experience': experience})
