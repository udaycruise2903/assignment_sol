from django.shortcuts import render, get_object_or_404, redirect
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, api_view
# from rest_framework.views import APIView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, SubCategory, App, Task, Screenshot, TotalPoints, Profile
from .forms import ScreenshotForm, ProfileUpdateForm
from allauth.account.views import LogoutView


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


@permission_classes([IsAuthenticated])
def home(request):
    """
    List of all apps and user's total points.
    """
    apps = App.objects.all()
    try:
        total_points = TotalPoints.objects.get(profile=request.user.profile)
    except TotalPoints.DoesNotExist:
        total_points = None
    return render(request, 'home.html', {'apps': apps, 'total_points': total_points, 'username': request.user.username})


@permission_classes([IsAuthenticated])
def app_detail(request, app_id):
    """
    Upload screenshot for a particular app
    """
    app = get_object_or_404(App, id=app_id)
    task, created = Task.objects.get_or_create(
        user=request.user, app=app, points=0)
    screenshot_form = ScreenshotForm(
        request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if screenshot_form.is_valid():
            screenshot = screenshot_form.save(commit=False)
            screenshot.task = task
            screenshot.save()
            messages.success(request, 'Screenshot uploaded successfully.')
            return redirect('app_detail', app_id=app_id)
    return render(request, 'app_detail.html', {'app': app, 'task': task, 'screenshot_form': screenshot_form})


@permission_classes([IsAuthenticated])
def completed_tasks(request):
    """
    List of tasks completed by a user
    """
    completed_tasks = Task.objects.filter(
        user=request.user, status=Task.COMPLETED)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})


@permission_classes([IsAuthenticated])
def profile(request):
    """
    Updates user's profile
    """
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
        total_points = TotalPoints.objects.get(profile=request.user.profile)
    return render(request, 'profile.html', {'total_points': total_points, 'form': form})


@permission_classes([IsAuthenticated])
def update_profile(request):
    """
    Update a user's profile
    """
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'update_profile.html', {'form': form})


@permission_classes([IsAdminUser])
def add_app(request):
    """
    only admins can add apps
    """
    if request.method == 'POST':
        # code to add a new app
        return redirect('home')
    return render(request, 'add_app.html')


@permission_classes([IsAuthenticated])
class AppListView(ListView):
    """
    List of apps
    """
    model = App
    template_name = 'home.html'


@permission_classes([IsAuthenticated])
def total_points(request):
    """
    Total points earned by a user.
    """
    total_points, created = TotalPoints.objects.get_or_create(
        profile=request.user.profile)
    return render(request, 'total_points.html', {'total_points': total_points})
