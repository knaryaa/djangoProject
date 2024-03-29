from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.forms import ContactForm
from home.models import Setting, ContactFormMessage
from product.models import Product, Category


# Create your views here.
def index(request):
    text = "BTK Django Kursu"
    slider = Product.objects.order_by('?')[:4]
    trendy_product = Product.objects.order_by('?')[:9]
    context = {"text": text,
               "page":"home",
               "slider": slider,
               "trendy_product": trendy_product,
               }
    return render(request, 'index.html', context)

def hakkimizda(request):
    context = {"page": "Hakkımızda"}
    return render(request, 'aboutus.html', context)

def iletisim(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.subject = form.cleaned_data['subject']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent. Thank you for contacting")
            return HttpResponseRedirect('/iletisim')

    form = ContactForm
    context = {"page":"İletişim",
               "form": ContactForm}
    return render(request, 'contact.html', context)

def referanslar(request):
    context = {"page": "Referanslar"}
    return render(request, 'references.html', context)

