

from django.urls import path

import articles
from . import views



urlpatterns = [

    path('',views.articles_list),

]
