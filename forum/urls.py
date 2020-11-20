from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.index, name='forum-index'),
    path('new_forum/', views.new_forum, name='new-forum'),
    path('<int:forum_id>/', views.forum, name='forum-detail'),
    path('topic/<int:topic_id>/', views.topic, name='topic-detail'),
    path('reply/<int:topic_id>/', views.post_reply, name='reply'),
    path('newtopic/<int:forum_id>/', views.new_topic, name='new-topic'),
    path('newtopic_question/', views.question_topic, name='question-topic'),
    
    
    
]
