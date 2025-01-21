from django.urls import path
from . import views
from .views import MessageView, AlertConfirm


urlpatterns = [
    path('', views.index, name='index'),
    path('messages/', MessageView.as_view(), name='message'),
    path('alert/', AlertConfirm.as_view(), name="alert")

]