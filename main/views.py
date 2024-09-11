from django.shortcuts import render

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