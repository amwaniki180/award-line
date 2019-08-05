from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,ReviewForm,CommentForm
from .models import Project,Profile,Comments,Review
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
# Create your views here.
def index(request):

    current_user = request.user
    projects = Project.objects.order_by('-date')
    profile = Profile.objects.order_by('-last_update')
    return render(request,'index.html',{"projects":projects,"profile":profile})

@login_required(login_url='/accounts/login/')
def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)

    except DoesNotExist:
        raise Http404()

    comments = Review.get_comment(project_id)
    latest_review_list=Review.objects.all().filter(project_id = project.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.user = request.user
            review.save()

    else:
        form = ReviewForm()

       

    return render(request, 'project.html', {"project": project,'form':form,'comments':comments,'latest_review_list':latest_review_list})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    #profile = Profile.objects.get(user_id=current_user.id)
    projects = Project.objects.all().filter(poster_id=user.id)
    return render(request, 'profile.html',{"user":user, "current_user":request.user,"projects":projects})

