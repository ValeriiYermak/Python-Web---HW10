from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import AuthorForm, QuoteForm
from django.contrib import messages
from .models import Author, Quote
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


def new_author(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author successfully added.')
            return redirect('users:new_author')
    else:
        form = AuthorForm()
    return render(request, 'new_author.html',
                  {'form': form, 'authors_set': authors})


def new_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            author_name = form.cleaned_data['author']
            author, created = Author.objects.get_or_create(fullname=author_name)
            quote_text = form.cleaned_data['quote']
            tags = form.cleaned_data['tags']
            quote = Quote(author=author, quote=quote_text, tags=tags)
            quote.save()
            messages.success(request, 'Quote successfully added.')
            return redirect('users:success_url')
    else:
        form = QuoteForm()
    return render(request, 'new_quote.html', {'form': form})


def success_url(request):
    context = {
        'message': 'You added a new quote successfully',
    }
    return render(request, 'success.html', context)
