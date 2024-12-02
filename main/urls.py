from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('adminku/', views.show_admin, name='show_admin'),
    path('adminkudelete/<int:id>', views.delete_user, name='delete_user'),
    path('get_user_details/<int:user_id>/', views.get_user_details, name='get_user_details'),
    path('edit-admin/<int:id>', views.edit_admin, name='edit_admin'),
    path('profile/', views.profile_view, name='profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
