from django.shortcuts import render
from django.core.paginator import Paginator
from .utils import get_mongodb
from .models import Author



def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html",
                  context={"quotes": quotes_on_page})

def author_info(request, author):
    author = Author.objects.get(fullname=author)
    return render(request, 'quotes/author_info.html', {'author': author})
