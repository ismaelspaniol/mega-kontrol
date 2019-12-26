
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from django.views.generic import TemplateView
from .router import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls')),
    path('', TemplateView.as_view(template_name="index.html")),
    path('api/', include(router.urls))

]
