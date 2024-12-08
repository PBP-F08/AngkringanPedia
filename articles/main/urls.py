from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Mengimpor views dari `articles/views.py`

app_name = 'articles'

urlpatterns = [
    # Routes untuk halaman utama dan fungsi utama
    path('', views.show_main, name='show_main'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),

    # Routes untuk autentikasi
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # Routes untuk admin
    path('adminku/', views.show_admin, name='show_admin'),
    path('adminkudelete/<int:id>/', views.delete_user, name='delete_user'),
    path('edit-admin/<int:id>/', views.edit_admin, name='edit_admin'),
    path('get_user_details/<int:user_id>/', views.get_user_details, name='get_user_details'),

    # Routes untuk user dashboard dan pengaturan profil
    path('dashboard/', views.redirect_dashboard, name='redirect_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('edit-user/<int:id>/', views.edit_user, name='edit_user'),

    # Routes untuk artikel (menggunakan class-based views)
    path('articles/', views.ArticleListView.as_view(), name='list'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
]

# Menangani media file jika DEBUG diaktifkan
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# commit