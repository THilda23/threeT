"""
URL configuration for threeT project.

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
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.quiz, name='quiz'),  # 이 부분을 추가합니다.
    path('quiz/', views.quiz, name='quiz'),
    path('admin/', admin.site.urls),
    path('reset_quiz/', views.reset_quiz, name='reset_quiz'),
    path('get_next_question/<int:question_id>/', views.get_next_question),
    path('get_previous_question/<int:question_id>/', views.get_previous_question, name='get_previous_question'),
    path('review_page/', views.review_page, name='review_page'),
    path('save_choice/', views.save_choice, name='save_choice'),

    path('ads.txt',views.Ads),
    path('sitemap.xml', RedirectView.as_view(url='/sitemap.xml', permanent=False), name='django.contrib.sitemaps.views.sitemap'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


