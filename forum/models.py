from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class Forum(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, default='')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, blank=True, null=True,on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def num_posts(self):
        return sum([t.num_posts() for t in self.topic_set.all()])

    def last_post(self):
        if self.topic_set.count():
            last = None
            for t in self.topic_set.all():
                l = t.last_post()
                if l:
                    if not last: last = l
                    elif l.created > last.created: last = l
            return last

class Topic(models.Model):
    forum = models.ForeignKey(Forum,on_delete = models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=10000, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete = models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(blank=True, default=False)

    def num_posts(self):
        return self.poste_set.count()

    def num_replies(self):
        return max(0, self.poste_set.count() - 1)

    def last_post(self):
        if self.poste_set.count():
            return self.poste_set.order_by("created")[0]

    def __str__(self):
        return "%s - %s" %(self.creator, self.title)

class Poste(models.Model):
    title = models.CharField(max_length=60,default='reponse',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True,on_delete = models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
    body = models.TextField(max_length=10000)
    user_ip = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return u"%s - %s - %s" % (self.creator, self.topic, self.title)

    def short(self):
        return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))

    short.allow_tags = True


class ProfaneWord(models.Model):
    word = models.CharField(max_length=60)

    def __str__(self):
        return self.word
