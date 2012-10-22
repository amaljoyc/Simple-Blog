from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    article = models.TextField()
    pub_date = models.DateTimeField('date published')
    uname = models.ForeignKey(User)

    def __unicode__(self):
      return self.title

class Comment(models.Model):
	post_fkey = models.ForeignKey(Post)
	comment = models.TextField()
	com_date = models.DateTimeField('date commented')
	uname = models.ForeignKey(User)

	def __unicode__(self):
		return self.name