from django.urls import include, path
from .views import user_login, dashboard, register, edit, home, empty, details
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name='main'
urlpatterns = [
    
    path('', home, name='home'),

    #================================================================================================
    # Login and register
    #================================================================================================
    
    # Registration.

    path('register/', register, name='register'),
     
    # Login URL.
        
     path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 

    # Password change.
        
     path('password-change/',
          auth_views.PasswordChangeView.as_view(),
          name='password_change'),
     
     path('password-change/done/',
          auth_views.PasswordChangeDoneView.as_view(),
          name='password_change_done'),    
          
     # Adresy URL przeznaczone do obsługi procedury odzyskiwania hasła.
        
     path('password-reset/',
          auth_views.PasswordResetView.as_view(),
          name='password_reset'),
     
     path('password-reset/done/',
          auth_views.PasswordResetDoneView.as_view(),
          name='password_reset_done'),
     
     path('password-reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(),
          name='password_reset_confirm'),
     
     path('password-reset/complete/',
          auth_views.PasswordResetCompleteView.as_view(),
          name='password_reset_complete'),

    #================================================================================================
    # Panel administracyjny
    #================================================================================================

    # Adresy URL kokpit.

     path('', include('django.contrib.auth.urls')),
     path('panel/main', dashboard, name='dashboard'),

     path('panel/empty/', empty, name='empty'),
     
    # Account URLS. 
     path('account/details/', details, name='details'),  
     path('account/edit/', edit, name='edit'),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)