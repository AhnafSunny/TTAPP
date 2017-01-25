from django.conf.urls import url,include
from . import views


app_name = 'thettapp'

urlpatterns = [
    url(r'^$',views.index, name= 'index'),
    url(r'^player/create',views.playerCreate,name='playerCreate'),
    url(r'^team/create',views.teamCreate,name='teamCreate'),
    url(r'^match/create',views.matchCreate,name='matchCreate'),
]
