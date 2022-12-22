from django.urls import path
from main import views

urlpatterns = [
    path('users/', views.UserListApiView.as_view()),
    path('users/<int:pk>/', views.UserDetailsApiView.as_view()),
    path('orders/', views.OrderListApiView.as_view()),
    path('orders/<int:pk>/', views.OrderDetailsApiView.as_view()),
    path('recipes/', views.RecipeListApiView.as_view()),
    path('recipes/<int:pk>/', views.RecipeDetailsApiView.as_view()),
    path('comments/', views.CommentListApiView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailApiView.as_view()),
    
]