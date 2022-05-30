from django.db import models


class PullRequest(models.Model):
    title = models.CharField(null=False, blank=False, max_length=500)
    description = models.TextField()
    main_branch = models.CharField(null=False, blank=False, max_length=500)
    head_branch = models.CharField(null=False, blank=False, max_length=500)
    state = models.CharField()