from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.views.generic import TemplateView
from buyproperty.views import HouseViewSets

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token

# making the router for the house
# router = routers.DefaultRouter()
# router.register(r'house', HouseViewSets)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    
    #local apps
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('user.urls')),
    #path('buyproperty/', include('buyproperty.urls')),

    #user management
    path('accounts/', include('django.contrib.auth.urls')),

    #api management
    path('api/', include('api.urls')),
    path('rest_auth/', include('rest_framework.urls', namespace='rest_auth')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

