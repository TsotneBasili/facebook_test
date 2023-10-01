from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostCollectionView.as_view(), names='posts'),
    path("<int:pk>/", views.PostSingletonView.as_view(), name='post_detail')
]
