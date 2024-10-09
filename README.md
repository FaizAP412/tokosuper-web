### TUGAS 2

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


### TUGAS 3

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


### TUGAS 4

1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`

   `HttpResponseRedirect` adalah class dari bawaan django yang digunakan untuk membuat respons pengalihan HTTP ke url tertentu

   Contoh:
   ```
   response = HttpResponseRedirect(reverse('main:login'))
   ```
   `redirect()` adalah fungsi yang ada di dalam library dari Django untuk mempermudah pembuatan response perpindahan halaman.

   Contoh:
   ```
   if form.is_valid():
        form.save()
        messages.success(request, "Your account has been created successfully")
        return redirect('main:login')
    ```

2. Jelaskan cara kerja penghubungan model `Product` dengan `User`!

    Untuk menghubungkan model `ProductEntry` dengan `User` diperlukan `ForeignKey` yang memuat kode unik dari user. `ForeignKey` digunakan untuk membuat hubungan *many-to-one* antara `ProductEntry` dan `User`.
    Cara untuk melakukan menghubungkan:
    1. Import model user: Django terlah memiliki model bawaan untuk mengelola pengguna
       
       ```
       from django.contrib.auth.models import User
       ```
    2. Mengkonfigurasi ForeignKey: `ForeignKey` perlu didefiniskan untuk mendapatkan spesific user.

        ```
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ```


3. Apa perbedaan antara *authentication* dan *authorization*, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.


    **Authentication** adalah proses verifikasi dari identitas user. Dalam proses ini user akan memasukkan kredensial seperti username dan password, kemudian input ini akan diverifikasi dengan data yang disimpan dalam database.
    **Authorization** adalah proses untuk menentukan akses dari pengguna setelah dilakukan autentikasi. Hal ini berkaitan dengan akses apa yang diperbolehkan dan apa yang tidak diperbolehkan.

    Implementasi Authentication:
    
    1. Menggunakan model: ```from django.contrib.auth.models import User```
    2. Membuat form login:
        ```
        def login_user(request):
        if request.method == "POST":
            form = AuthenticationForm(request, request.POST)

            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse('main:show_main'))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
        ```

    Implementasi Authorization:
    1. Menggunakan decorator: Decorator yang digunakan pada proyek kali adalah `@login_required`
        ```
        @login_required(login_url='/login')
        def show_main(request):
        product_entries = ProductEntry.objects.all()
        ...
        ...
        ```
    2. Cara lain untuk mengimplementasikannya adalah dengan mensetting izin yang ada pada model dari user.
        ```
        from django.contrib.auth.models import Permission

        user.user_permissions.add(Permission.objects.get(codename='can_edit'))
        ```
4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari *cookies* dan apakah semua *cookies* aman digunakan?

    Cara Django mengingat pengguna setelah login:
    - Django menyimpan pengguna dengan membuat sesi login baru
    - Menyimpan waktu terakhir pada cookie browser dan menyimpannya dalam response

    ```
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse('main:show_main'))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ```        
    Kegunaan lain dari *cookies*:
    - Menyimpan preferensi pengguna.
    - Pelacakan aktivitas pengguna.
    - Menyimpan token autentikasi yang digunakan pada sistem berbasis token.

    Apakah semua *cookies* aman?
    
    **Tidak**, cookies masih memiliki resiko keamanan. Hal ini dapat terjadi apabila cookies tidak dienkripsi dan tidak dilindungi secara benar.

    Cara mengamankan cookies:
    - Gunakan HTTPS
    - Enkripsi data sensitif
    - Gunakan atribut `HttpOnly`
    
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
    
    - Membuat fungsi registrasi, login, dan logout

        ```
        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)

                if form.is_valid():
                    form.save()
                    messages.success(request, "Your account has been created successfully")
                    return redirect('main:login')
            context = {
                'form': form,
            }
            return render(request, "xregister.html", context)
        ```
        ```
        def login_user(request):
            if request.method == "POST":
            form = AuthenticationForm(request, request.POST)

            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse('main:show_main'))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

            else:
                form = AuthenticationForm(request)
            context = {'form': form}
            return render(request, 'login.html', context)
        ```

        ```
            def logout_user(request):
                logout(request)
                response = HttpResponseRedirect(reverse('main:login'))
                response.delete_cookie('last_login')
                return redirect('main:login')
        ```

    - Membuat file `.html` untuk form registrasi dan login dan menambahkan button logout
    - Melakukan konfigurasi path url pada `urlpatterns` pada `urls.py`

        ```
        urlpatterns = [
        ...
        ...
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        path('register/', register, name='register'),
        ...
        ...
        ```
    - Melakukan konfigurasi untuk merestriksi akses pada halaman main.
        ```
        @login_required(login_url='/login')
        ```
    - Menambahkan aplikasi *cookies* untuk mendapatkan data
        ```
        def login_user(request):
        ...
        ...
                if form.is_valid():
                    ...
                    ...
                    response = HttpResponseRedirect(reverse('main:show_main'))
                    response.set_cookie('last_login', str(datetime.datetime.now()))
        ...
        ...
        ```
        ```
        def logout_user(request):
        ...
        ...
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        ...
        ...
        ```
    - Menghubungkan `ProductEntry` dengan `User`
        ```
        class ProductEntry(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)

        ```

### TUGAS 5

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    
    **Urutan prioritas pengambilan CSS selector**
    1. Inline Style: CSS diterapkan langsung pada elemen HTML menggunakan atribut `style` memiliki prioritas paling tinggi.
    2. ID Selector: ID selector memiliki prioritas paling tinggi kedua dibandingkan dengan `class`, `atribute`, `tag`. ID selector direpresentasikan dnegan `#id`.
    3. Class Selector: Class selector berada dibawah dari *inline style* dan ID Selector.
    4. Element Selector (`p, div, h1`)
    5. Universal Selector (`*`)
2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
    
    Responsive design memungkinkan aplikasi web untuk bisa ditampilkan dalam berbagai jenis perangkat, web akan menyesuaikan tampilannya berdasarkan ukuran layar dari perangakat. Sehingga, web bisa diakses oleh berbagai jenis ukuran dan resolusi layar yang berbeda.
    Contoh:
    - Sudah menerapkan: Google.com, halaman web sudah menyesuaikan elemen ui dengan ukuran pada berbagai perangkat
    - Belum menerapkan: SIAK.NG, halaman web hanya memiliki tampilan untuk desktop, sehingga ketika pengguna membuka menggunakan handphone tampilannya akan tetap serupa dengan desktop.
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    
    - Margin: Ruang kosong di laur border dari elemen, gunanya untuk memisahkan antara elemen dengan elemen lainnya pada halaman.
    - Border: Garis di sekitar padding dan konten elemen.
    - Padding: Ruang antara konten elemen dengan border-nya.
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
    - Flexbox: Layout yang fleksibel yang memungkinkan elemen di dalam container untuk disejajarkan secara dinamis dan responsif, ini bisa diimplementasikan secara horizontal atau vertikal. Gunannya untuk layout satu dimensi, baik baris atau kolom.
    - Grid Layout: Layout dua dimensi yang memungkinkan penataan elemen dalam baris dan kolom secara terstruktur. Berguna untuk tata letak yang kompleks.
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

    1. Melakukan konfigurasi Tailwind untuk digunakan sebagai framework CSS pada aplikasi Django. Proses ini mencakup menambahkan Tailwind ke dalam pengaturan proyek serta menyusun file konfigurasi agar dapat berfungsi dengan baik.

    2. Mengembangkan fitur edit dan hapus produk. Fitur ini memberikan pengguna kemampuan untuk memperbarui atau menghapus data produk dengan mudah, sehingga meningkatkan interaktivitas serta fleksibilitas aplikasi.

    3. Merancang dan membuat komponen navbar dengan menyusun file navbar.html di dalam direktori aplikasi. Navbar ini menjadi elemen navigasi utama yang memudahkan pengguna berpindah antar halaman.

    4. Mengimplementasikan navbar ke berbagai template HTML dalam aplikasi untuk memastikan konsistensi navigasi di seluruh halaman.

    5. Menambahkan file statis, termasuk CSS dan gambar, ke dalam aplikasi. Hal ini mencakup pengorganisasian file dalam struktur direktori yang sesuai agar mudah diakses.

    6. Menerapkan styling menggunakan utility classes dari Tailwind CSS. Dengan ini, desain yang responsif dan modern dapat dicapai tanpa menulis banyak kode CSS manual.


### TUGAS 6
1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

    1. Interaktivitas: JavaScript memungkinkan pengembang untuk membuat aplikasi web yang dinamis dan interaktif. Misalnya, JavaScript memungkinkan untuk memperbarui konten halaman tanpa perlu me-refresh halaman sepenuhnya, seperti pada AJAX.

    2. Pengalaman Pengguna yang Lebih Baik: Dengan JavaScript, pengembang dapat membuat fitur yang merespons secara real-time, seperti validasi form di sisi klien, animasi, dan kontrol UI yang lebih baik, sehingga memberikan pengalaman pengguna yang lebih baik.

    3. Asynchronous Processing: JavaScript mendukung asynchronous processing melalui fungsi seperti fetch(), memungkinkan komunikasi dengan server tanpa menghentikan alur kerja di frontend, misalnya mengambil data atau mengirimkan form melalui AJAX tanpa memuat ulang halaman.

    4. Kompatibilitas Lintas Platform: JavaScript adalah bahasa yang didukung oleh semua browser modern, sehingga memungkinkan pengembangan aplikasi web yang kompatibel dengan berbagai perangkat.

    5. Framework dan Library: Pengembang dapat memanfaatkan framework dan library seperti React, Vue, dan Angular untuk mengembangkan aplikasi web yang kompleks dengan lebih cepat dan terstruktur.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

    await digunakan untuk menunggu penyelesaian promise yang dikembalikan oleh fetch(). Dalam hal ini, ketika kita menggunakan fetch() untuk melakukan permintaan HTTP, permintaan ini bersifat asynchronous, dan fetch() mengembalikan sebuah promise.

    - Tanpa await: Jika kita tidak menggunakan await, JavaScript akan mengeksekusi baris berikutnya tanpa menunggu respons dari server. Hasil dari fetch() akan berupa promise yang belum diselesaikan (pending promise), sehingga kita tidak dapat langsung mendapatkan datanya.

    - Dengan await: Saat kita menambahkan await sebelum fetch(), eksekusi akan berhenti sementara hingga fetch() selesai, sehingga kita bisa mendapatkan respons yang sudah diselesaikan dan menggunakannya langsung dalam variabel yang telah disiapkan.

    Contoh:
    ```
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);  // Data yang sudah diambil dari server
    ```
    Jika await tidak digunakan, kita hanya akan mendapatkan promise yang belum terselesaikan, bukan datanya.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

    csrf_exempt digunakan untuk mengecualikan suatu view dari mekanisme Cross-Site Request Forgery (CSRF) protection. Dalam aplikasi Django, CSRF digunakan untuk melindungi pengguna dari serangan CSRF, yang memanfaatkan session dan cookie pengguna untuk mengirimkan permintaan yang tidak sah.

    #### Dalam kasus AJAX POST:

    Jika CSRF token tidak dikirimkan atau tidak ada dalam permintaan AJAX, Django akan menolak permintaan tersebut.

    Namun, dalam beberapa situasi, kita mungkin mengirimkan permintaan AJAX tanpa CSRF token (misalnya, ketika menggunakan API eksternal). Dengan menambahkan decorator csrf_exempt, kita menginstruksikan Django untuk tidak memeriksa token CSRF pada view ini.


    Namun, penggunaan csrf_exempt harus digunakan dengan hati-hati, karena menonaktifkan proteksi CSRF dapat meningkatkan risiko keamanan. Jika memungkinkan, selalu tambahkan CSRF token dalam request AJAX.

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

    Meskipun kita bisa membersihkan input pengguna di frontend (seperti menggunakan JavaScript untuk sanitasi input), tetap penting untuk melakukan pembersihan di backend karena:

    1. Keamanan: Frontend mudah dimanipulasi oleh pengguna, termasuk penyerang. Mereka bisa dengan mudah menonaktifkan validasi atau memodifikasi data yang dikirim ke server. Oleh karena itu, membersihkan input di backend sangat penting untuk mencegah serangan seperti SQL Injection atau XSS (Cross-Site Scripting).


    2. Integritas Data: Backend adalah sumber kebenaran utama untuk data. Meskipun frontend dapat membantu dengan validasi awal, backend harus memastikan bahwa hanya data yang valid yang disimpan di database. Ini juga mencegah data yang tidak diinginkan masuk ke dalam sistem.


    3. Penggunaan Data di Layanan Lain: Data dari backend sering digunakan untuk layanan lain, seperti API atau analisis. Oleh karena itu, menjaga integritas data sangat penting di sisi backend.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

    1. AJAX GET untuk Mengambil Data Produk:

        Saya memulai dengan membuat view Django untuk mendapatkan produk (get_product_entries) yang hanya mengembalikan data produk dalam format JSON. Data ini diambil berdasarkan pengguna yang login.

        Di frontend, saya menggunakan JavaScript dengan fetch() dan await untuk mengambil data produk dari endpoint ini. Data tersebut kemudian dirender secara dinamis ke halaman menggunakan innerHTML dengan template card produk yang sudah ditentukan.



    2. AJAX POST untuk Menambahkan Produk:

        Untuk menambahkan produk, saya membuat view add_product_entry_ajax di Django, yang menangani request POST dan menambahkan produk ke dalam database. Di frontend, saya menggunakan form modal yang memanggil fungsi JavaScript untuk mengirimkan data produk baru menggunakan fetch() (POST). Setelah produk berhasil ditambahkan, form direset, modal ditutup, dan daftar produk di-refresh dengan memanggil ulang AJAX GET.



    3. Menambahkan Modal untuk Form Produk:

        Modal ini digunakan untuk input produk baru dengan validasi input seperti nama, harga, dan deskripsi. Saya menggunakan JavaScript untuk mengontrol pembukaan dan penutupan modal, serta memastikan form direset setelah berhasil menambahkan produk.



    4. Pembersihan Input di Backend:

        Selain membersihkan input di frontend dengan validasi sederhana (seperti required), saya juga membersihkan input di backend untuk memastikan data yang masuk ke database aman dan valid.