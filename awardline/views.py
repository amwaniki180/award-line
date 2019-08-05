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
