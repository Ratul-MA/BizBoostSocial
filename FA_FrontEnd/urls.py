"""
URL configuration for FA_FrontEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


import FA_overview.views
import Registration.views
import Bizzer_SocialMedia.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FA_overview.views.index, name='home'),
    path('login.html', Registration.views.login_user, name='login'),
    path('logout/', Registration.views.logout_user, name='logout'),
    path('register.html', Registration.views.register, name='register'),
    path('MyBizBoostProfile.html/', FA_overview.views.MyBizBoostProfile,),
    path('base.html', Bizzer_SocialMedia.views.Bizzer, name='Bizzer'),
    path('update_user/', Bizzer_SocialMedia.views.update_user, name='update_user'),
    path('profile_list/', Bizzer_SocialMedia.views.profile_list, name='profile_list'),
    path('profile/<int:pk>', Bizzer_SocialMedia.views.profile, name='profile'),
    path('profile/followers/<int:pk>', Bizzer_SocialMedia.views.followers, name='followers'),
    path('beep_like/<int:pk>', Bizzer_SocialMedia.views.beep_like, name="beep_like"),
    path('beep_show/<int:pk>', Bizzer_SocialMedia.views.beep_show, name="beep_show"),
    path('unfollow/<int:pk>', Bizzer_SocialMedia.views.unfollow, name="unfollow"),
    path('follows/<int:pk>', Bizzer_SocialMedia.views.follows, name="follow"),
    path('delete_beep/<int:pk>', Bizzer_SocialMedia.views.delete_beep, name="delete_beep"),
    path('edit_beep/<int:pk>', Bizzer_SocialMedia.views.edit_beep, name="edit_beep"),
    path('search/', Bizzer_SocialMedia.views.search, name='search'),
    path('Bizzer.html', Bizzer_SocialMedia.views.Bizzer),
    path('Bwhitepaper.html', Bizzer_SocialMedia.views.whitepaper, name='Business WhitePaper'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
