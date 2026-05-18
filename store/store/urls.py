from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve # Імпортуємо вбудований сервіс роздачі


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('storeapp.urls'))
]

# Напряму кажемо Django роздавати папку media за будь-яких умов
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
