"""hackathon_helper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new
from helpapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('helper/log_in/', LoginView.as_view(template_name='helpapp/log_in.html'),
         name='log-in'),
    path('helper/sign_out/', LogoutView.as_view(next_page='/'),
         name='log-out'),
    path('helper/sign_up/', helper_sign_up, name='sign-up'),
    path('helper/account/', helper_account, name='account'),
    path('helper/account/information/<int:id>/', helper_account_information,
         name='information-account'),
    path('helper/problems/', helper_problems, name='problems'),
    path('helper/problems/add/', helper_add_problems, name='add-problems'),
    path('helper/problems/delete/<int:id>/', helper_delete_problems, name='delete-problems'),
    path('helper/problems/edit/<int:id>/', helper_edit_problems, name='edit-problems'),
    path('helper/feedback/', helper_feedback, name='feedback'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
