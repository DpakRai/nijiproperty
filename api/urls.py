from django.urls import include, path
from rest_framework import routers
from api.views import *
from api import views
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from buyproperty.models import House, HouseImage, Comment 
from rentproperty.models import Renthouse, Renthouseimage
from sellproperty.models import Sellhouse, Sellhouseimage

#router = routers.DefaultRouter()
#router.register(r'users', views.BuyViewSets)

app_name = 'api'
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    path('buyhouse/',Houseinfo.as_view(), name="Houseinfo"),
    path("buyhousedetail/<int:pk>/",views.HouseDetail.as_view(),name="HouseDetail"),
    path('renthouse/',Renthouseinfo.as_view(), name="Renthouseinfo"),
    path("renthousedetail/<int:pk>/",views.RenthouseDetail.as_view(),name="RenthouseDetail"),
    path('sellhouse/',Sellhouseinfo.as_view(), name="Sellhouseinfo"),
    path("sellhousedetail/<int:pk>/",views.SellhouseDetail.as_view(),name="SellhouseDetail"),
    path('houseimage/',Houseimageinfo.as_view(), name="Houseimageinfo"),
    # path('sellinfo/',Sellinfo.as_view(), name="Sellinfo"),
    # path("selldetail/<int:pk>/",views.SellDetail.as_view(),name="SellDetail"),
    # #path('buyhouse/', include('rest_framework.urls', namespace='rest_framework')),
    
]