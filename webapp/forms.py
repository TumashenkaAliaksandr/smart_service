from django import forms
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Your name'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Your email'}
        )
    )

    message = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Message', 'cols': 30, 'rows': 5}
        )
    )


def contact(request):
    context = {}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка отправки формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Отправка письма
            send_mail(
                'Feedback from your website',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                'tumashenkaaliaksandr@gmail.com',  # Отправитель
                ['recipient@example.com'],  # Получатель
                fail_silently=False,
            )

            return HttpResponseRedirect('')  # Перенаправление на страницу "Спасибо"
    else:
        form = ContactForm()

    context['form'] = form
    return render(request, 'webapp/contact.html', context=context)
