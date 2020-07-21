from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('catresult/<str:cats>/', views.catresult, name="catresult"),
    path('results/', views.results, name="results"),
    path('the_project/<str:pk>/', views.the_project, name="the_project"),

    path('remove_comment/<str:pk>/', views.remove_comment, name="remove-comment"),

    path('addpost/', views.addpost, name="addpost"),
    path('addcat/', views.addcat, name="addcat"),
    path('deletecat/<str:pk>/', views.deletecat, name= "deletecat"),
    path('addauthor/', views.addauthor, name="addauthor"),

    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('register/', views.register, name="register"),

    path('updatepost/<str:pk>/', views.updatepost, name="updatepost"),
    path('deletepost/<str:pk>/', views.deletepost, name="deletepost"),

    path('contact/', views.contact, name="contact"),


    path("change-password/",views.change_password, name="change-password"),
    path("edit_profile/",views.edit_profile, name="edit-profile"),
    
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    # path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('reset_password_complete/<uidb64>/<token>/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)