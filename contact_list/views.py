from django.shortcuts import render
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request,
            'contact_list/contact_list.html', {'contacts': contacts})

def contact_detail (request, id):
    contact = Contact.objects.get(id=id)
    return render(request,
            'contact_list/contact_detail.html', {'contact': contact})