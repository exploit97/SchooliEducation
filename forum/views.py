
from django.forms import models as forms_models
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from forum.models import Forum, Topic
from forum.models import Poste as Post
from forum.forms import TopicForm, PostForm,ForumForm,TopicForm2
from django.contrib.auth.decorators import login_required



def index(request):
    """Main listing."""
    forums = Forum.objects.order_by('-created')
    context = {
        'forums': forums, 
        'user': request.user
        }
    return render(request,"forum/list.html",context )



    

def forum(request, forum_id):
    """Listing of topics in a forum."""
    topics_list = Topic.objects.filter(forum=forum_id).order_by("-created")
    paginator = Paginator(topics_list, 9)
    page = request.GET.get('page')


    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)
    
    forum = get_object_or_404(Forum, pk=forum_id)
   
    context ={
       'topics':topics,
       'forum':forum
       }

    return render(request,"forum/forum.html", context)

def topic(request, topic_id):
    """Listing of posts in a topic."""
    posts = Post.objects.filter(topic=topic_id).order_by("created")
    topic = Topic.objects.get(pk=topic_id)
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
   
    context ={
       'topic':topic,
       'posts':posts
       }
   
    return render(request,"forum/topic.html", context)

@login_required
def post_reply(request, topic_id):
    form = PostForm()
    topic = Topic.objects.get(pk=topic_id)
    
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():

            post = Post()
            post.topic = topic
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.creator = request.user
            post.user_ip = request.META['REMOTE_ADDR']

            post.save()

            return HttpResponseRedirect(reverse('forum:topic-detail', args=(topic.id, )))

    return render(request,'forum/reply.html', {
            'form': form,
            'topic': topic,
        })

@login_required
def new_topic(request, forum_id):
    form = TopicForm()
    forum = get_object_or_404(Forum, pk=forum_id)
    
    if request.method == 'POST':
        form = TopicForm(request.POST)

        if form.is_valid():

            topic = Topic()
            topic.title = form.cleaned_data['title']
            topic.description = form.cleaned_data['description']
            topic.forum = forum
            topic.creator = request.user

            topic.save()

            return HttpResponseRedirect(reverse('forum:forum-detail', args=(forum_id, )))

    return render(request,'forum/new-topic.html', {
            'form': form,
            'forum': forum,
        },)


@login_required
def new_forum(request):
    form = ForumForm()
    
    
    if request.method == 'POST':
        form = ForumForm(request.POST)

        if form.is_valid():

            forum = Forum()
            forum.title = form.cleaned_data['title']
            forum.description = form.cleaned_data['description']
            
            forum.creator = request.user

            forum.save()

            return HttpResponseRedirect(reverse('forum:forum-index'))

    return render(request,'forum/new-forum.html', {
            'form': form
            
        },)


@login_required
def question_topic(request):
    form = TopicForm2()
    
    if request.method == 'POST':
        form = TopicForm2(request.POST)

        if form.is_valid():

            topic = Topic()
            topic.title = form.cleaned_data['title']
            topic.description = form.cleaned_data['description']
            topic.forum = form.cleaned_data['forum']
            topic.creator = request.user
           

            topic.save()

            return HttpResponseRedirect(reverse('forum:forum-index' ))

    return render(request,'forum/question-topic.html', {
            'form': form,
            
        },)
