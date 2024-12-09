# artikel/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Artikel  # Pastikan model Artikel sesuai
from .forms import ArtikelForm  # Pastikan form ArtikelForm sudah dibuat

# Menampilkan daftar artikel
def show_article_list(request):
    artikel_list = Artikel.objects.all()  # Ambil semua artikel
    return render(request, 'artikel/article_list.html', {'artikel_list': artikel_list})

# Menampilkan detail artikel
def show_article_detail(request, id):
    artikel = get_object_or_404(Artikel, id=id)  # Ambil artikel berdasarkan ID
    return render(request, 'artikel/article_detail.html', {'artikel': artikel})

# Membuat artikel baru
def create_article(request):
    if request.method == 'POST':
        form = ArtikelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artikel:show_article_list')  # Redirect ke daftar artikel
    else:
        form = ArtikelForm()
    return render(request, 'artikel/create_article.html', {'form': form})
