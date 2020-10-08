from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/homePage.html')

def contact(request):
    connect = {
        'mob': ['Якщо залишилися питання, телефонуйте:', '(065) 985 76 34', 'Telegram:', \
            't.me/asdf', 'Instagram:', 'instagram.com/asdasf'],
    }
    return render(request, 'mainapp/contacts.html', connect)

def book(request):
    return render(request, 'mainapp/books.html')