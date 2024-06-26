from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from course.models import Course, Batch, Resource #,Purchase
from .forms import UserUpdateForm
from userauths.models import Dashboard_User
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.utils import timezone
from datetime import *
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from subscription.models import PurchaseCourse
from course.serializers import *
from .serializers import *
from rest_framework import generics


@login_required(login_url="/userauths/login/")
@transaction.atomic
def user_ui(request, username):
    if request.method == "GET":
        auser = User.objects.get(username=username)
        # if request.user.is_authenticated:
        if auser.is_staff == True:
            return redirect("/admin")
        else:
            user = User.objects.get(username=auser.username)
            if not Dashboard_User.objects.filter(user_id=user.id).exists():
                dashboard_user, created = Dashboard_User.objects.get_or_create(user=auser)
                dashboard_user.save()
            dash_user = Dashboard_User.objects.get(user_id=user.id)
            todays_date = timezone.now().date()
            enrolled_courses = dash_user.enrolled_courses.filter(status="active")
            todays_date = timezone.now().date()
            years = list(range(1990, 2031))
            enrolled_courses = dash_user.enrolled_courses.filter(status="active")
            todays_date = timezone.now().date()
            years = list(range(1990, 2031))
            batches = Batch.objects.filter(course__in=enrolled_courses)
            print(f"batches: {batches}")
            batches = Batch.objects.filter(course__in=enrolled_courses)
            batch_notes ={}
            for batch in batches:
                notes = Resource.objects.filter(batch=batch, notes__isnull=False)
                batch_notes[batch] = notes
            return render(
                request,
                "dashboard.html",
                {
                    'years': years,
                    "user": user,
                    "dash_user": dash_user,
                    "enrolled_courses": enrolled_courses,
                    "batches": batches,
                    "batch_notes": batch_notes,
                },
            )        
    if request.method == "POST":
        user_profile = Dashboard_User.objects.get(user=request.user)        
    if request.method == "POST":
      #get from frontend
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        college_name = request.POST.get("college_name")
        graduation_year = request.POST.get("graduation_year")
        mobile_number = request.POST.get("mobile_number")
        bio = request.POST.get("bio")
        education =request.POST.get("education")
        github = request.POST.get("github")
        linkedin = request.POST.get("linkedin")
        if not education:
            education = "No Education Provided"
        # Update user details
        user_profile.fname = first_name
        user_profile.mname = middle_name
        user_profile.lname = last_name
        user_profile.mobilenumber = mobile_number
        user_profile.collegename = college_name
        user_profile.graduation_year = graduation_year
        user_profile.education = education
        user_profile.github = github
        user_profile.linkedin = linkedin
        user_profile.bio = bio
        # Save changes
        profile_photo = request.FILES.get('profile_photo')
        print("profile is :", profile_photo)
        if profile_photo:
            fs = FileSystemStorage()
            file_path = fs.save(f'user_photos/{request.user.username}/{profile_photo.name}', ContentFile(profile_photo.read()))
            print("File saved to:", file_path)
            user_profile.photo = file_path
        user_profile.save()
        return redirect("core:index")
    return render(request, "dashboard.html", {"user": request.user})


def user_ui_json(request, username):
    user = User.objects.get(username=username)
    dash_user = Dashboard_User.objects.get(user_id=user.id)
    enrolled_courses = dash_user.enrolled_courses.filter(status="active")
    batches = Batch.objects.filter(course__in=enrolled_courses)
    batch_notes = []
    for batch in batches:
        notes = Resource.objects.filter(batch=batch, notes__isnull=False)
        resource_serializer = ResourceSerializer(notes, many=True)
        batch_notes.append(resource_serializer.data)
    batches_data = []
    if batches:
        for batch in batches:
            batch_serializer = BatchSerializer(batch)
            batches_data.append(batch_serializer.data)
    enrolled_courses_data = [] 
    if enrolled_courses:
        for course in enrolled_courses:
            course_serializer = CourseSerializer(course)
            enrolled_courses_data.append(course_serializer.data)
    user_serializer = UserSerializer(user)
    dashuser_serializer = Dash_userSerializer(dash_user)

    jsondata = {
            'User': user_serializer.data,
            'DashUserDetails': dashuser_serializer.data,
            'CoursesEnrolled': enrolled_courses_data,
            'Batches': batches_data,
            'Resources':batch_notes,
        }  
    return Response(jsondata)
    
    
def admin_ui(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            auser = request.user
            if auser.is_staff == True:
                return redirect("core:index")
            else:
                return redirect("/admin")
        else:
            return redirect("core:index")


@login_required(login_url="/userauths/login/")
def enroll_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    batches = Batch.objects.filter(course_id=course_id)
    if request.method == "POST":
        batch_id = request.POST.get("batch_id")
        if batch_id:
            batch = get_object_or_404(Batch, pk=batch_id)
            dashboard_user, created = Dashboard_User.objects.get_or_create(user=request.user)
            dashboard_user.enrolled_batches.add(batch)
    return redirect("dashboard:user_ui")  # Redirect to the dashboard


@login_required(login_url="/userauths/login/")
def enroll_plan(request, date, course_id):
    dashboard_user, created = Dashboard_User.objects.get_or_create(user=request.user)
    course = get_object_or_404(Course, pk=course_id)
    batch = get_object_or_404(Batch, course_id=course_id)   
    start_date = timezone.now()
    end_date = timezone.datetime.strptime(date, "%Y-%m-%d")
    additional_access_date = (end_date + timedelta(days=30)).strftime("%Y-%m-%d")
    months = ((end_date.year - start_date.year ) * 12) + (end_date.month - start_date.month)
    print("MONTHSSSS", months)
    return redirect("core:index")


# RestAPI views Here
class dash_user_api(generics.ListCreateAPIView):
    queryset = Dashboard_User.objects.all()
    serializer_class = Dash_userSerializer

class dash_user_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dashboard_User.objects.all()
    serializer_class = Dash_userSerializer
    lookup_field = 'user__username'