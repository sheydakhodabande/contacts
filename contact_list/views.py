from django.shortcuts import render, get_object_or_404
from .models import Contact
from .forms import ContactForm


def contact_list(request):
    contacts = Contact.objects.all()

    return render(request,
'contact_list/contact_list.html',
{'contacts': contacts}
)


def contact_detail(request, slug):

    contact = get_object_or_404(Contact, slug=slug)

    return render(request,
'contact_list/contact_detail.html',
{'contact': contact}
)


def contact_create(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = ContactForm()

    return render(request,
        'contact_list/contact_form.html',
        {'form': form}
    )