from django.urls import include, path
from buyproperty import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('add_house/', views.create_house_info, name='add_house'),
    path('house_list/', views.house_list, name='house_list'),
    path('house_detail/<int:id>/', views.house_detail, name='house_detail'),
]