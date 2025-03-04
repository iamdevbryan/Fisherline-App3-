from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('messages/',views.message_view, name='message'),
    path('alert/', views.alert_confirm, name="alert"),
    path('home/', views.accueil, name='home'),
    path('database', views.database, name='database')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)