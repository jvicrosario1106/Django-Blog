from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('catresult/<str:cats>/', views.catresult, name="catresult"),
    path('results/', views.results, name="results"),
    path('the_project/<str:pk>/', views.the_project, name="the_project"),




    path('addpost/', views.addpost, name="addpost"),
    path('addcat/', views.addcat, name="addcat"),
    path('deletecat/<str:pk>/', views.deletecat, name= "deletecat"),
    path('addauthor/', views.addauthor, name="addauthor"),

    


    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('register/', views.register, name="register"),


    path('updatepost/<str:pk>/', views.updatepost, name="updatepost"),
    path('deletepost/<str:pk>/', views.deletepost, name="deletepost"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)