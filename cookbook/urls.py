from django.conf.urls.defaults import *


urlpatterns = patterns('',
    # / -- That is the URL Thien uses to represent the recipe list
    # if Thien goes to /, django will go to recipe_list view
    (r'^$', 'thienscorner.cookbook.views.recipe_list'),
    #if Thien goes to /1/, django will go to recipe view
    #(the recipe represent with id '1')
    (r'^(?P<object_id>\d+)/$', 'thienscorner.cookbook.views.recipe'),
)
