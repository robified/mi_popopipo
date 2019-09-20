##
#
#
#
# PLEASE DONT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING
# DO NOT RUN MAKEMIGRATIONS. IF YOU RUN MAKE MIGRATIONS, 
# TELL US SO WE CAN SYNC OR DROP THE LOCAL DATABASE. 
#
#
##
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Importing the django-vote package
from vote.models import VoteModel

# Our drop down menu for post category type
POST_TYPE = (
    ('V', 'Vent'),
    ('I', 'Info'),
    ('H', 'Help')
)

# Post model - We pass in VoteModel from the django-vote package
class Post(VoteModel, models.Model):
    title = models.CharField(max_length=255)
    categories = models.CharField(
        max_length=1,
        choices=POST_TYPE,
        default=POST_TYPE[0][0]
    )
    company = models.CharField(max_length=50)
    company_office_city = models.CharField(max_length=50)
    body = models.TextField()
    summary = models.TextField(default='No Summary Was Found')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    blog_views = models.IntegerField(default=0)
    comment_size = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})

    # The upvote method for each post. Inherited from the VoteModel
    def upvote(self, user):
        try:
            self.post_votes.create(user=user, post=self, vote_type='up')
            self.votes += 1
            self.save()
        except IntegrityError:
            return 'already_upvoted'
        return'ok'
    
    # The downvote method for each post. Inherted from the VoteModel
    def downvote(self, user):
        try:
            self.post_votes.create(user=user, post=self, vote_type="down")
            self.votes -= 1
            self.save()
        except IntegrityError:
            return 'already_downvoted'
        return 'ok'

# Creating a model for our votes
class UserVotes(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='user_votes'
        )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_votes'
    )
    vote_type = models.CharField(max_length=100)

    class Meta:
        unique_together = ('user', 'post', 'vote_type')

# The comment model
class Comment(models.Model):
    body = models.TextField()
    views = 0
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = 0
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('comment', kwargs={'comment_id': self.id})