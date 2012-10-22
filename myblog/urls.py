from django.conf.urls import patterns, include, url
from blogapp.views import posts	
from blogapp.views import index, comment, user_login, user_register, home, users, user_titles, user_logout, newpost, addpost, account
from blogapp.views import deletepost, delete, editpost, edit, editsubmit
from notification.views import get_all_notification
from excel_import.views import CsvImportView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/(.*)/(\d+)/$', posts),
    url(r'^index/$', index),
    url(r'^comment/$', comment),
    url(r'^login/$', user_login),
    url(r'^logout/$', user_logout),
    url(r'^register/$', user_register),
    url(r'^home/$', home),
    url(r'^users/$', users),
    url(r'^posts/(.*)/$', user_titles),
    url(r'^newpost/$', newpost),
    url(r'^addpost/$', addpost),
    url(r'^account/(.*)/$', account),
    url(r'^deletepost/$', deletepost),
    url(r'^deletepost/(\d+)/$', delete),
    url(r'^editpost/$', editpost),
    url(r'^editpost/(\d+)/$', edit),
    url(r'^editsubmit/(\d+)/$', editsubmit),
    url(r'^notify/$', get_all_notification),
    url(r'^fileupload/$', CsvImportView.as_view()),
)