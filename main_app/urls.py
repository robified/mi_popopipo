from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('show/', views.show, name='show'),
    # path('show/new', views.show.new, name='new'),
    # path('show/edit', views.show.edit, name='edit'),
    # path('login/', views.login, name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('post/', views.post_index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='detail'),
    path('post/new/', views.PostCreate.as_view(), name='post_create'),
    # path('post/<int:post_id>/addComment', views.CommentCreate.as_view(), name='comment_create'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
]