from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from favorites.views import get_makanan_favorite, create_favorite, delete_favorite, cek_favorit,get_makanan_favorite_admin
from main.views import edit_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('search/', search_recipes, name='search_recipes'),
    path('add-recipe/', add_recipe, name='add_recipe'),
    path('delete/<int:id>', delete_product, name='delete_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)