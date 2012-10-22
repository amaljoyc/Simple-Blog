from blogapp.models import Post
from blogapp.models import Comment
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	list_display = ('uname', 'title', 'article', 'pub_date')

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('uname', 'comment', 'com_date')

admin.site.register(Comment, CommentAdmin)