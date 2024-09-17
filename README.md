### TUGAS 1

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
![Bagan Request Client](media/README/Bagan.png)

* Jelaskan fungsi git dalam pengembangan perangkat lunak!
> Git merupakan sistem kontrol yang digunakan untuk melacak perubahan versi pada pengembangan perangkat lunak, memungkinkan untuk berkolaborasi dengan banyak pengembang pada proyek, memungkinkan adanya pengembangan fitur tanpa perlu mengganggu kode utama, dan menyiapkan cadangan kode sumber yang aman. Pada mata kuliah PBP, Git akan membantu dalam pengembangan proyek tugas kelompok, yang membantu siswa berkolaborasi dalam mengembangkan aplikasi.
* Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
> Django dipilih sebagai framework pembelajaran karena didalamnya telah disediakan berbagai fitur bawaan untuk pengembangan perangkat lunak, memiliki kemampuan ORM, dan scalability yang baik. Selain itu, yang utama adalah pendekatan dari konsep MVT.(Model-View-Template).
* Mengapa model pada Django disebut sebagai ORM?
> Django disebut dengan ORM karena Django melakukan penyederhanaan pada interaksi kode python dan database, ORM memungkinkan pengembang untuk menulis query SQL dalam bahasa python.


### TUGAS 2

* Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
> Data delivery diperlukan untuk mengirimkan data antara server dan client. Hal ini memungkinkan data ditampilkan secara dinamis dan interaktif kepada pengguna. Aplikasi hanya akan menampilkan konten statis yang tidak dapat diperbarui atau diubah berdasarkan input dari pengguna.
* Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
> 1. JSON lebih baik dibandingkan XML dalam banyak kasus karena lebih mudah dibaca oleh manusia. 
> 2. JSON menggunakan sintaks yang lebih sederhana dan lebih mudah diparse oleh mesin.
> 3. JSON lebih efisien dalam ukuran data dan kecepatan parsing.
> 
> Sehingga JSON jauh lebih populer dibandingkan XML dalam pengembangan aplikasi web dan API.
* Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
> Method  is_valid() pada form Django digunakan untuk memeriksa apakah data yang dimasukkan sudah sesuai dengan validasi yang telah ditentukan. Method ini akan memastikan bahwa data yang diterima dari pengguna adalah valid sebelum disimpan ke database.
* Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
> csrf_token digunakan untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). Tanpa csrf_token pada form Django, penyerang dapat membuat permintaan palsu dari situs lain yang akan dijalankan oleh pengguna yang telah login. Hal ini dapat menyebabkan tindakan yang tidak diinginkan seperti perubahan data atau penghapusan data tanpa sepengetahuan pengguna. csrf_token akan meminta token yang valid pada setiap permintaan POST.
* Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
> * Mempersiapkan skeleton untuk kerangka dari views dan menambahkan directory dari skeleton pada settings.py
> * Merubah html utama yaitu main.html dengan menyambungkan template skeleton.
> * Meng-import UUID pada models.py dan menambahkannya pada ProductEntry. Setelah itu, melakukn migrations karena ada perubahan pada models.
> * Membuat file forms.py, didalamnya terdapat model untuk menerima entry product.
> * Pada views.py tambahkan forms.py dengan membuat fungsi yang akan memanggil forms.py dan menambahkan datanya pada database.
> * Membuat file html baru untuk menampilkan forms.py, serta mengubah main.html untuk bisa menampilkan data yang didapat dari form.
> * Membuat fungsi show_json, show_json_by_id, show_xml, show_xml_by_id untuk bisa mengembalikan data dalam bentuk xml dan json.
> * Melakukan git add, commit, dan push, untuk memperbarui data pada repository github dan pws.

JSON dan XML di Postman
![JSON Postman](media/README/Hasil_JSON_Postman.png)
![JSON by ID Postman](media/README/Hasil_JSON_by_ID_Postman.png)
![XML Postman](media/README/Hasil_XML_Postman.png)
![XML by ID Postman](media/README/Hasil_XML_by_ID_Postman.png)



