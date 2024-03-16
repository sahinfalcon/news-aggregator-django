from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NewsArticle
from . import news_scraper  # Import your news_scraper file


def scrape_articles(request):
    if request.method == "POST":
        article_url = request.POST.get("article_url")

        try:
            # Call your scraping function from news_scraper.py
            news_data = news_scraper.scrape_article(article_url)

            # Check if an article with the same URL already exists
            if NewsArticle.objects.filter(url=article_url).exists():
                # Article already exists, handle according to your requirement
                # For example, redirect to the article list with a message
                return redirect("news:article_list")
            else:
                # Create a NewsArticle object and save to the database since it's a new URL
                news_data["url"] = (
                    article_url  # Ensure the URL is included in the news_data
                )
                article = NewsArticle(**news_data)
                article.save()
                # Redirect to the article list view
                return redirect("news:article_list")

        except Exception as e:
            # Handle scraping errors gracefully
            return HttpResponse(f"An error occurred: {e}")
    else:
        # Render the input form
        return render(request, "news/scrape_form.html")


def article_list(request):
    # Retrieve all articles from the database, ordered by the most recent publication date
    articles = NewsArticle.objects.all().order_by("-publication_date")
    # Render the article list to the specified template, passing the articles as context
    return render(request, "news/article_list.html", {"articles": articles})
