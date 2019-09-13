from django.db import models
from django.contrib.auth.models import User

POST_TYPE = (
    ('V', 'Vent'),
    ('I', 'Info'),
    ('H', 'Help')
)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    categories = models.CharField(
        max_length=1,
        choices=POST_TYPE,
        default=POST_TYPE[0][0]
    )
    company = models.CharField(max_length=50)
    company_office_city = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    views = models.IntegerField()
    flags = models.IntegerField()
    # Add User Auth to get user keys.
    # FOR ROBIN
    # WHEN YOU RUN makemigrations IT WILL GIVE YOU A PROMPT
    # TO SELECT EITHER OPTION 1 OR 2. SELECT OPTION 1 AND PRESS ENTER.
    # IT WILL THEN ASK FOR A DEFAULT VALUE FOR OUR SUPER USER. HIS ID SHOULD
    # BE 1 SINCE HE IS THE SUPER USER. PRESS 1 AND HIT ENTER.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
