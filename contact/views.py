from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.


def contact(request):
    contactform = ContactForm()
    if request.method == "POST":
        contactform = ContactForm(data=request.POST)
        if contactform.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # enviamos el correo
            email = EmailMessage(
                "corpcitti",
                "De {} <{}>\n\n{}".format(name, email, content),
                "no contestar",
                ["corpsales280@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact') + "?ok")
            except:
                return redirect(reverse('contact') + "?fail")

    return render(request, 'contact/contact.html', {'form': contactform})

