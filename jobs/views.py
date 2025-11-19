from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Job, UserProfile
from .forms import JobForm, UserProfileForm, UserRegistrationForm

def home(request):
    jobs = Job.objects.filter(is_active=True)
    search_query = request.GET.get('search', '')
    location_query = request.GET.get('location', '')
    job_type_query = request.GET.get('job_type', '')

    if search_query:
        jobs = jobs.filter(title__icontains=search_query) | jobs.filter(company__icontains=search_query)
    if location_query:
        jobs = jobs.filter(location__icontains=location_query)
    if job_type_query:
        jobs = jobs.filter(job_type=job_type_query)

    context = {
        'jobs': jobs,
        'search_query': search_query,
        'location_query': location_query,
        'job_type_query': job_type_query,
    }
    return render(request, 'jobs/home.html', context)

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def post_job(request):
    try:
        profile = request.user.userprofile
        if profile.user_type != 'recruiter':
            messages.error(request, 'Only recruiters can post jobs.')
            return redirect('home')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Please complete your profile first.')
        return redirect('home')

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('my_jobs')
    else:
        form = JobForm()

    return render(request, 'jobs/post_job.html', {'form': form})

@login_required
def my_jobs(request):
    try:
        profile = request.user.userprofile
        if profile.user_type != 'recruiter':
            messages.error(request, 'Only recruiters can view this page.')
            return redirect('home')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Please complete your profile first.')
        return redirect('home')

    jobs = Job.objects.filter(recruiter=request.user)
    return render(request, 'jobs/my_jobs.html', {'jobs': jobs})

@login_required
def edit_job(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('my_jobs')
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/edit_job.html', {'form': form, 'job': job})

@login_required
def delete_job(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully!')
        return redirect('my_jobs')
    return render(request, 'jobs/delete_job.html', {'job': job})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'jobs/register.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('home')
    return render(request, 'jobs/logout.html')
