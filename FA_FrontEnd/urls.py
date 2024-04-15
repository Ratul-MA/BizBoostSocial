
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


import FA_overview.views
import Registration.views
import Bizzer_SocialMedia.views
import p2p_network.views

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
    path('Platform Overview.html', Bizzer_SocialMedia.views.PlatformOverview, name='Platform Overview'),
    path('p2p/', include('p2p_network.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
