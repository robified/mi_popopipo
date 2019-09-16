from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

POST_TYPE = (
    ('V', 'Vent'),
    ('I', 'Info'),
    ('H', 'Help')
)

class Post(models.Model):
    title = models.CharField(max_length=255)
    categories = models.CharField(
        max_length=1,
        choices=POST_TYPE,
        default=POST_TYPE[0][0]
    )
    company = models.CharField(max_length=50)
    company_office_city = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    blog_views=models.IntegerField(default=0)
    flags = 0
    # FOR ROBIN
    # WHEN YOU RUN makemigrations IT WILL GIVE YOU A PROMPT
    # TO SELECT EITHER OPTION 1 OR 2. SELECT OPTION 1 AND PRESS ENTER.
    # IT WILL THEN ASK FOR A DEFAULT VALUE FOR OUR SUPER USER. HIS ID SHOULD
    # BE 1 SINCE HE IS THE SUPER USER. PRESS 1 AND HIT ENTER.

    # UNCOMMENT THIS WHEN WE ARE READY TO INTEGRATE USER ONLY FUNCTIONS
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})

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
    
