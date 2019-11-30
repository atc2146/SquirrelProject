from django.urls import path



from . import views


app_name = 'tracker'
urlpatterns = [
    # ex: /sightings/
    path('sightings', views.index, name='index'),
    
    # ex: /sightings/<unique-squirrel-id>
    path('sightings/<slug:unique_squirrel_id>/', views.update, name='update'),

    # ex: /sightings/add
    path('sightings/add', views.add, name='add'),

    # ex: /sightings/stats
    path('sightings/stats', views.stats, name='stats'),

    # ex: /map
    path('map', views.map, name='map'),
]
