from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings 
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Python 33 API",
        description="makers bootcamp",
        default_version="v1",
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('review/',include('review.urls')),
    path('docs/',schema_view.with_ui('swagger')),
    path('product/',include('products_shop.urls'))
    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Добавляем обработку статических файлов