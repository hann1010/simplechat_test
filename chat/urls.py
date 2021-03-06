from . import views
from django.urls import path
from .views import (
    Chat_View,
    #AllDetailView,
    #ThreadDetailView,
    #TopicCreateView,
    #CommentCreateView,
    ChatUpdateView,
    ChatDeleteView,
    UserDetailView
    
)


urlpatterns = [
    path('', views.home, name='chat-home'),
    path('chat/chat_json/', views.jsonChat, name='chat-json'),
    path('chat/chat-view/', Chat_View.as_view(), name='chat-view'),
    #path('latest/comments/', views.latest_comments, name='forum-latest_comments'),
    #path('latest/all/', views.latest_all, name='forum-latest_all'),
    #path('topic/new/', TopicCreateView.as_view(), name='forum_topic-create'),
    #path('all/<int:pk>/comment/new/', CommentCreateView.as_view(), name='forum_comment-create'),
    #path('all/<int:pk>/open/', AllDetailView.as_view(), name='forum_open_one_post'),
    #path('all/<int:pk>/thread/', ThreadDetailView.as_view(), name='forum_thread'),
    path('chat/<int:pk>/update/', ChatUpdateView.as_view(), name='chat_update'),
    path('chat/<int:pk>/delete/', ChatDeleteView.as_view(), name='chat_delete'),
    path('chat/<int:pk>/user_info/', UserDetailView.as_view(), name='chat-user_info'),
    
	
]