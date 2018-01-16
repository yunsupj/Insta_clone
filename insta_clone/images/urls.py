from django.conf.urls import url
from . import views
 
urlpatterns= [
    url(
        regex=r'^all$',
        view=views.ListAllImage.as_view(),
        name='all_images'
    ),
    url(
        regex=r'^comments/',
        view=views.ListAllComment.as_view(),
        name='all_commments'
    ),
]
