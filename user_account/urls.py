from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('Sign/',views.SignIn,name='Sign'),
    path('login',views.Login,name='Login'),
    path('Logout/',views.Logout,name='Logout'),
    path('account/@<str:username>/', views.userProfile, name='viewProfile'),
    path('account-notification/', views.accountNotification, name='account_notification'),
    path('account-projects/', views.accountProjects, name='account_projects'),
    path('accountProject/update/<int:id>/', views.accountProject_update, name='accountProject_update'),
    path('messages/', views.Messages, name='messages'),
    path('update/@<str:username>/', views.updateProfile, name='updateProfile'),
    path('profile/@<str:username>/', views.profile, name='profile'),
    path('search/', views.search_profiles, name='search_profiles'),
    path('search-users/', views.search_users, name='search_users'),
    path('chat/', views.messages_page,name='chat'),
    # path('rooms/', views.rooms, name='rooms'),
    # path('<slug:slug>/',views.room,name='room'),
    # path('<str:room_name>/send/', views.send_message, name='send_message'),
]