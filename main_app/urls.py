from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('show/', views.show, name='show'),
    # path('show/new', views.show.new, name='new'),
    # path('show/edit', views.show.edit, name='edit'),
    # path('login/', views.login, name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('post/about', views.about, name='about'),
    path('post/<int:post_id>/', views.post_detail, name='detail'),
    path('post/search', views.SearchView.as_view(), name='search'),
    path('post/new/', views.PostCreate.as_view(), name='post_create'),
    path('post/comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('post/comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('vent/', views.vent_index, name='vent_index'),
    path('info/', views.info_index, name='info_index'),
    path('help/', views.help_index, name='help_index'),
    # Path for the routes that send upvote/downvotes
    path('post/<int:post_id>/upVote', views.upVote, name='upVote'),
    path('post/<int:post_id>/downVote', views.downVote, name='downVote'),
]