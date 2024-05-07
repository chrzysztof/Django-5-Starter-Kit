from django.urls import include, path
from .views import user_login, dashboard, register, edit, home, empty
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name='main'
urlpatterns = [
    
    path('', home, name='home'),

    #================================================================================================
    # Logowanie i rejestracja
    #================================================================================================
    
    # Adresy URL rejestracja.

    path('register/', register, name='register'),
     
    # Adresy URL logowanie.
        
    path('login/', user_login, name='login'),

    # Adresy URL przeznaczone do obsługi zmiany hasła.
        
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

     path('panel/main/', include('django.contrib.auth.urls')),
     path('panel/main/', dashboard, name='dashboard'),

     path('panel/empty/', empty, name='empty'),
     
    # Adresy URL panel użytkownika. 
       
     path('panel/edit/', edit, name='edit'),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)