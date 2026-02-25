# urls.py principal
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # CORRECTION ICI : admin.site.urls au lieu de admin.site.get_admin_urls()
    path('admin/', admin.site.urls), 
    
    path('api/', include('sales.urls')),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]