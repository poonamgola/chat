from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Thread
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

def search_profiles(request):
    query = request.GET.get('q')  # Get the search query from the GET request
    results = []
    if query:
        # Filter users based on the search query
        results = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        results = User.objects.filter(
        )

    return render(request, 'user-account-dashboard/messages.html', {'results': results, 'query': query})



@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    all_users = User.objects.exclude(id=request.user.id)
    context = {
        'Threads': threads,
        'Users': all_users,
    }
    return render(request, 'user-account-dashboard/chat.html', context)



def SignIn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('confirm_password')
        
        if password!=password1:
            return HttpResponse("Your password doesn't match...Please try again!!!")
        else:
            my_user=User.objects.create_user(username,email,password)
            my_user.save()
            return redirect('Login')
    return render(request,"sign-up.html")
    

def Login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password') 

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')   
        else:
            return HttpResponse("username is not valid!!!!!")     
    return render(request,"sign-in.html") 


def Logout(request):
    logout(request)
    return redirect('Login') 

@login_required(login_url='Login')
def userProfile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user,
    }
    return render(request, 'user-account-dashboard/account-detail.html', context)

@login_required(login_url='Login')
def accountNotification(request):
    return render(request, 'user-account-dashboard/account-notification.html')

@login_required(login_url='Login')
def accountProjects(request):
    
    # if request.method == 'POST':
    #     category_id = request.POST.get('category')
    #     title = request.POST.get('title')
    #     sector = request.POST.get('sector')
    #     sub_sector = request.POST.get('sub_sector')
    #     description = request.POST.get('description')
    #     pdf_file=request.FILES.get('pdf')
       
    #     user = request.user
    #     try:
    #         category = CommunityCategory.objects.get(id=category_id)
    #         data = CommunityPost(
    #             user=user,
    #             category=category,
    #             title=title,
    #             sector=sector,
    #             sub_sector=sub_sector,
    #             description=description,
    #             pdf=pdf_file,
    #         )
    #         data.save()
    #         messages.success(request, 'Successfully added new Project!')
    #     except CommunityCategory.DoesNotExist:
    #         messages.error(request, 'Please select the Role field to proceed!')

    #     return redirect('account_projects')

    # communities = CommunityCategory.objects.all()
    # projects = CommunityPost.objects.filter(user=request.user)

    # context = {
    #     'communities': communities,
    #     'projects': projects,
    # }
    return render(request, 'user-account-dashboard/account-projects.html')

@login_required(login_url='Login')
def accountProject_update(request, id=None):
    # post = get_object_or_404(CommunityPost, id=id)
    
    # if request.method == 'POST':
    #     post.category_id = request.POST.get('category')
    #     post.sector = request.POST.get('sector')
    #     post.sub_sector = request.POST.get('sub_sector')
    #     post.title = request.POST.get('title')
    #     post.description = request.POST.get('description')
    #     post.pdf=request.FILES.get('pdf')
        
    #     post.save()
    #     messages.success(request, "Post updated successfully.")
    #     return redirect('account_projects')
    
    # elif request.headers.get('x-requested-with') == 'XMLHttpRequest':
    #     data = {
    #         'category': post.category_id,
    #         'title': post.title,
    #         'sector':post.sector,
    #         'sub_sector':post.sub_sector,
    #         'description':post.description,
    #         'pdf':post.pdf.url if post.pdf else None,
    #     }
    #     return JsonResponse(data)
    
    # context = {
    #     'post': post,
    # }
    
    return render(request, 'user-account-dashboard/account-projects.html')

@login_required(login_url='Login')
def Messages(request):
    return render(request, 'user-account-dashboard/messages.html')

@login_required
def updateProfile(request, username):
    user = get_object_or_404(User, username=username)

    # if request.method == 'POST':
    #     # Handle profile image upload
    #     if 'profile_image' in request.FILES:
    #         user.profile_image = request.FILES['profile_image']
        
    #         # Update profile information
    #         user.full_name = request.POST.get('full_name', user.full_name)
    #         user.username = request.POST.get('username', user.username)
    #         user.email = request.POST.get('email', user.email)
    #         user.phone = request.POST.get('phone', user.phone)
    #         user.nationality = request.POST.get('nationality', user.nationality)
    #         user.gender = request.POST.get('gender', user.gender)
    #         user.role = request.POST.get('role', user.role)
    #         user.sector = request.POST.get('sector', user.sector)
    #         user.skills_expertise = request.POST.get('skills_expertise', user.skills_expertise)
    #         user.address = request.POST.get('address', user.address)

    #         #saving profile
    #         user.save()
    #         messages.success(request, "Profile updated successfully!")

    #         return redirect('viewProfile',username=user.username) 
    
    #     # Handle email update
    #     new_email = request.POST.get('email')
    #     if new_email and new_email != user.email:
    #         user.email = new_email
    #         #saving profile
    #         user.save()
    #         messages.success(request, "Email updated successfully!")

    #         return redirect('viewProfile',username=user.username) 

    #     # Handle password change
    #     current_pass = request.POST.get('current_pass')
    #     new_password = request.POST.get('new_password')
    #     cf_new_password = request.POST.get('cf_new_password')
        
    #     if current_pass and new_password and cf_new_password:
    #         if new_password == cf_new_password:
    #             if authenticate(username=user.username, password=current_pass):
    #                 user.set_password(new_password)
    #                 user.save()
    #                 print("Password updated successfully.")
    #                 messages.success(request, "Password updated successfully.")
    #                 login(request, user)
    #                 return redirect('viewProfile', user.username)
    #             else:
    #                 print("Current password is incorrect.")
    #                 messages.error(request, "Current password is incorrect.")
    #                 return redirect('viewProfile', user.username)
    #         else:
    #             print("New passwords do not match.")
    #             messages.error(request, "New passwords do not match.")
    #             return redirect('viewProfile', user.username)

    return render(request, 'user-account-dashboard/user-profile.html', {'user': user})

def profile(request, username):
    user = get_object_or_404(User, username=username)
    # posts= CommunityPost.objects.filter(user=user)
    # reviews = Review.objects.filter(reviewed_user=user)

    # paginator = Paginator(posts, 3)
    # page_num = request.GET.get('page')
    # posts_data = paginator.get_page(page_num)
    
    
    # Calculate average rating
    # avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    # Calculate distribution of ratings
    # rating_counts = reviews.values('rating').annotate(count=Count('rating')).order_by('rating')
    
    # if request.method == 'POST':
    #     rating = request.POST.get('rating')
    #     content = request.POST.get('content')
    #     reviewer = request.user
    #     Review.objects.create(reviewer=reviewer, reviewed_user=user, rating=rating, content=content)
    #     return redirect('profile', username=username)

    context = {
        'user_data': user,
        # 'posts': posts,
        # 'reviews': reviews,
        # 'avg_rating': avg_rating,
        # 'rating_counts': rating_counts,
        # 'posts_data':posts_data,
    }
    return render(request, 'user-account-dashboard/user-profile.html', context)

# @login_required
# def search_profiles(request):
#     query = request.GET.get('q')
#     results = User.objects.filter(
#         Q(full_name__icontains=query) |
#         Q(role__icontains=query) |
#         Q(company__icontains=query) |
#         Q(city__icontains=query) |
#         Q(zip_code__icontains=query)
#     )
#     return render(request, 'user-account-dashboard/messages.html', {'results': results, 'query': query})

def search_users(request):
    query = request.GET.get('q', '')
    if query:
        users = User.objects.filter(username__icontains=query)
        user_list = list(users.values('id', 'username'))
    else:
        user_list = []

    return JsonResponse(user_list, safe=False)


