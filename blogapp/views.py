# Create your views here.
from django.shortcuts import render_to_response
from blogapp.models import Post
from blogapp.models import Comment
from blogapp.cform import CommentForm
from blogapp.cform import PostForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import datetime

def posts(request, uname, get_id):
    get_post = Post.objects.get(id = get_id)
    get_comment_list = Comment.objects.filter(post_fkey_id = get_id)
    form = CommentForm(initial={'hidden_id': get_id, 'hidden_name': uname})
    return render_to_response('getpost.html', locals(), context_instance=RequestContext(request))

def user_titles(request, uname):
    get_user = User.objects.get(username = uname)
    title_list = Post.objects.filter(uname_id = get_user.id)
    return render_to_response('user_titles.html', locals())

def index(request):
    title_list = Post.objects.all()
    return render_to_response('index.html', locals())

def comment(request):
    now = datetime.datetime.now()
    if request.method == 'POST': # If the form has been submitted...
        form = CommentForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            try:
                form_name = User.objects.get(username = request.user)
            except User.DoesNotExist:
                return HttpResponseRedirect('/login/')
            form_comment = form.cleaned_data['comment']
            form_hid_id = form.cleaned_data['hidden_id']
            form_hid_name = form.cleaned_data['hidden_name']
            c = Comment(post_fkey_id = form_hid_id, uname = form_name, comment = form_comment, com_date = now)
            c.save()
            return HttpResponseRedirect('/posts/%s/%d/' %(form_hid_name, form_hid_id)) # Redirect after POST

def addpost(request):
    form = PostForm()
    return render_to_response('newpost.html', locals(), context_instance=RequestContext(request))

def newpost(request):
    now = datetime.datetime.now()
    if request.method == 'POST': # If the form has been submitted...
        form = PostForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            try:
                form_name = User.objects.get(username = request.user)
            except User.DoesNotExist:
                return HttpResponseRedirect('/login/')
            form_title = form.cleaned_data['title']
            form_article = form.cleaned_data['article']
            p = Post(uname = form_name, title = form_title, article = form_article, pub_date = now)
            p.save()
            return HttpResponseRedirect('/posts/%s/' %(form_name.username)) # Redirect after POST

def user_register(request):
    state = 'Please register below..'
    if request.POST:
      username = request.POST['username']
      password = request.POST['password']
      user = User.objects.create_user(username, '',password)
      user.save()
      state = 'You have successfully registered..'
    return render_to_response('register.html',{'state':state}, context_instance=RequestContext(request))

def user_login(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username = username, password = password)
      if user is not None:
          if user.is_active:
              login(request, user)
              # Redirect to a success page.
              state = "You're successfully logged in!"
              return HttpResponseRedirect('/account/%s/' %(username))
          else:
              # Return a 'disabled account' error message
              state = "Your account is not active, please contact the site admin."
      else:
          # Return an 'invalid login' error message.
          state = "Your username and/or password were incorrect."
    return render_to_response('login.html',{'state':state, 'username': username}, context_instance=RequestContext(request))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')
    # Redirect to a success page.

def home(request):
    title_list = Post.objects.all()
    return render_to_response('home.html', locals())

def users(request):
    user_list = User.objects.all()
    return render_to_response('users.html', locals())

def account(request, uname):
    messages.info(request, 'Three credits remain in your account.')
    messages.success(request, 'Profile details updated.')
    messages.warning(request, 'Your account expires in three days.')
    messages.error(request, 'Document deleted.')
    return render_to_response('account.html', locals(), context_instance=RequestContext(request))   

def deletepost(request):
    user = User.objects.get(username = request.user)
    title_list = Post.objects.filter(uname_id = user.id)
    return render_to_response('delete.html', locals())

def delete(request, get_id):
    p = Post.objects.get(id = get_id)
    p.delete()
    return HttpResponseRedirect('/deletepost/')

def editpost(request):
    user = User.objects.get(username = request.user)
    title_list = Post.objects.filter(uname_id = user.id)
    return render_to_response('edit.html', locals())    

def edit(request, get_id):
    p = Post.objects.get(id = get_id)
    form = PostForm(initial={ 'title': p.title, 'article': p.article })
    return render_to_response('editform.html', locals(), context_instance=RequestContext(request))

def editsubmit(request, get_id):
    now = datetime.datetime.now()
    if request.method == 'POST': # If the form has been submitted...
        form = PostForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            try:
                form_name = User.objects.get(username = request.user)
            except User.DoesNotExist:
                return HttpResponseRedirect('/login/')
            form_title = form.cleaned_data['title']
            form_article = form.cleaned_data['article']
            p = Post.objects.get(id = get_id)
            p.uname = form_name
            p.title = form_title
            p.article = form_article
            p.pub_date = now
            p.save()
            return HttpResponseRedirect('/editpost/') # Redirect after POST