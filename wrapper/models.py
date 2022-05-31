from django.db import models

from users.models import User

PR_STATES = (
    ('open', 'open'),
    ('merged', 'merged'),
    ('merging', 'merging')
)


class PullRequest(models.Model):
    title = models.CharField(null=False, blank=False, max_length=500)
    description = models.TextField()
    main_branch = models.CharField(null=False, blank=False, max_length=500)
    head_branch = models.CharField(null=False, blank=False, max_length=500)
    state = models.CharField(choices=PR_STATES, max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pull_requests")
