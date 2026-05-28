from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Importações do drf-spectacular
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    
    # Endpoints do Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # Gera o arquivo de esquema (YAML/JSON)
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Interface Swagger
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # Interface alternativa Redoc
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)