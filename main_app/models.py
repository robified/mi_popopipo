from django.db import models

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
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
