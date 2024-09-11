* Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
> 1. Membuat Proyek Django:
>Membuat proyek baru dengan menjalankan ``` django-admin startproject tokosuper ```
> 2. Membuat Aplikasi Django:
> membuat aplikasi baru dengan nama main dengan menjalankan ``` python manage.py startapp main ``` , dan menambahkan aplikasi main ke INSTALLED_APPS di settings.py dan mengatur routing untuk mengarahkan aplikasi main pada tokosuper/urls.py. 
> 3. Membuat Model: mendefinisikan model di models.py yang ada didalam aplikasi main, class ProductEntry dengan atribut name, description, price.
> 4. Melakukan migrasi: melakukan migrasi untuk melacak migrasi basis data dengan menjalankan 
```
python manage.py makemigrations
python manage.py migrate
```
> 5. Mendifinisikan views.py dalam aplikasi main:
```
def show_main(request):
    products = {
        'produk' : 'Gulfstream G650ER',
        'harga': 'Rp.15.000.000.000',
        'deskripsi': 'Pesawat terbang'
    }

    context = {
        'products': products,
        'app_name': 'TokoSuper',
        'name': 'Faiz Akram Pribadi',
        'npm': '2306221353',
        'class': 'PBP A',
        'image' : 'https://i0.wp.com/sellallyourstuff.com/wp-content/uploads/2015/10/StickmanWhatToSell.jpg?fit=600%2C298'
    }

    return render(request, "main.html", context)
```
> 6. Membuat file html bernama main.html yang akan merender data yang akan ditampilkan 
> 7. Mengatur routing pada urls.py dalam directory main.
> 8. Melakukan deployment kepada PWS

* Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
* Jelaskan fungsi git dalam pengembangan perangkat lunak!
> Git merupakan sistem kontrol yang digunakan untuk melacak perubahan versi pada pengembangan perangkat lunak, memungkinkan untuk berkolaborasi dengan banyak pengembang pada proyek, memungkinkan adanya pengembangan fitur tanpa perlu mengganggu kode utama, dan menyiapkan cadangan kode sumber yang aman. Pada mata kuliah PBP, Git akan membantu dalam pengembangan proyek tugas kelompok, yang membantu siswa berkolaborasi dalam mengembangkan aplikasi.
* Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
> Django dipilih sebagai framework pembelajaran karena didalamnya telah disediakan berbagai fitur bawaan untuk pengembangan perangkat lunak, memiliki kemampuan ORM, dan scalability yang baik. Selain itu, yang utama adalah pendekatan dari konsep MVT.(Model-View-Template).
* Mengapa model pada Django disebut sebagai ORM?
> Django disebut dengan ORM karena Django melakukan penyederhanaan pada interaksi kode python dan database, ORM memungkinkan pengembang untuk menulis query SQL dalam bahasa python.

