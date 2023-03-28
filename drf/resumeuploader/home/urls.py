from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.ProfileView.as_view(),name='resume'),
    path('list/',views.ProfileView.as_view(),name='list'),
    path('all/',views.ProfileView.as_view(),name='all'),
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
