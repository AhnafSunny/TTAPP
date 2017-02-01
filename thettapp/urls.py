from django.conf.urls import url,include
from . import views


app_name = 'thettapp'

urlpatterns = [
    url(r'^$',views.index, name= 'index'),
    url(r'^player/create/$',views.playerCreate,name='playerCreate'),
    url(r'^player/create/add',views.playerAdd,name='playerAdd'),
    url(r'^player/browse',views.playerBrowse,name='playerBrowse'),
    url(r'^team/create',views.teamCreate,name='teamCreate'),
    url(r'^match/create',views.matchCreate,name='matchCreate'),
]
