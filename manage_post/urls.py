from django.urls import path
from manage_post import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', views.ListAllCategoriesView.as_view(), name='all_categories'),
    path('article/<slug:slug>', views.ShowPostDetailView.as_view(), name='post'),
]
