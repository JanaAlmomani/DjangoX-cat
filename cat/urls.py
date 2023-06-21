from django.urls import path
from .views import CatListView, CatDetailView, CatCreateView, CatUpdateView, CatDeleteView

urlpatterns = [
    path('cat/', CatListView.as_view(), name='cat_list'),
    path('cat/<int:pk>/', CatDetailView.as_view(), name='cat_detail'),
    path('cat/create/', CatCreateView.as_view(), name='cat_create'),
    path('cat/<int:pk>/update/', CatUpdateView.as_view(), name='cat_update'),
    path('cat/<int:pk>/delete/', CatDeleteView.as_view(), name='cat_delete'),
]