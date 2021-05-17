"""dj_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from posts.views import (
    home_view,
    create_post,
    post_detail_view,
    post_update_view,
    delete_post_view
)
from useraccounts.views import (
    register_view,
    login_view,
    logout_view,
    profile_view,
    profile_settings_view
)
from useraccounts.forms import (
    MyPasswordChangeForm,
    MyPasswordResetForm,
    MySetPasswordForm
)

urlpatterns = [
    path('', home_view, name='home'),
    path('new/', create_post, name='create_post'),
    path('<int:pk>/', post_detail_view, name='post_detail'),
    path('<int:pk>/update/', post_update_view, name='post_update'),
    path('<int:pk>/delete/', delete_post_view, name='delete_post'),
    path('register/', register_view, name='register'),
    path('profile/settings/', profile_settings_view, name='profile_settings'),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<str:username>/change-password/', auth_views.PasswordChangeView.as_view(form_class=MyPasswordChangeForm ,success_url='/profile/settings/'), name='password_change'),
    path('password-reset/', auth_views.PasswordResetView.as_view(form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)