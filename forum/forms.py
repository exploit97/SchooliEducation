from django import forms
from forum.models import Topic, Poste, ProfaneWord,Forum

from django.conf import settings

DJANGO_SIMPLE_FORUM_FILTER_PROFANE_WORDS = getattr(settings, 'DJANGO_SIMPLE_FORUM_FILTER_PROFANE_WORDS', True)

class ForumForm(forms.ModelForm):

    title = forms.CharField(max_length=60, required=True)

    class Meta():
        model = Forum
        exclude = ('creator','updated', 'created',)

class TopicForm(forms.ModelForm):

    title = forms.CharField(max_length=60, required=True)

    class Meta():
        model = Topic
        exclude = ('creator','updated', 'created', 'closed', 'forum',)

class TopicForm2(forms.ModelForm):

    title = forms.CharField(max_length=60, required=True)

    class Meta():
        model = Topic
     
        exclude = ('creator','updated', 'created', 'closed',)


class PostForm(forms.ModelForm):
    
    class Meta():
        model = Poste
        exclude = ('creator', 'updated', 'created','topic', 'user_ip',)

    def clean_body(self):
        body = self.cleaned_data["body"]

        if DJANGO_SIMPLE_FORUM_FILTER_PROFANE_WORDS:
            profane_words = ProfaneWord.objects.all() 
            bad_words = [w for w in profane_words if w.word in body.lower()]

            if bad_words:
                raise forms.ValidationError("Bad words like '%s' are not allowed in posts." % (reduce(lambda x,y: "%s,%s" % (x,y),bad_words)))
        
        return body
