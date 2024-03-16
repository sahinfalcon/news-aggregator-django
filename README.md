**# News Aggregator with Sentiment Analysis**

This project aims to build a comprehensive news aggregator web application using Django.  It will combine news article scraping from various sources, insightful sentiment analysis, and user-friendly visualizations.

## Key Features

* **News Scraping:** Efficiently scrape news articles from multiple online sources.
* **Sentiment Analysis:** Perform analysis to determine the sentiment (positive, negative, neutral) of news content.
* **Organized Display:** Present scraped news articles in a clear and well-formatted manner along with their sentiment classification.
* **Search (Future):** Allow users to search for news articles by keywords and track sentiment specifically related to their query

## Technologies

* **Python:** Programming language for the project.
* **Django:**  Web framework for application structure and functionality.
* **Beautiful Soup:** Python library for web scraping tasks.
* **VADER:**  Sentiment analysis library.

## Setup Instructions

1. **Clone the repository:** 
   ```bash
   git clone https://github.com/sahinfalcon/news-aggregator-django.git
   ```

2. **Create a virtual environment (recommended):**  
   ```bash
   python -m venv env
   source env/bin/activate 
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database:**
   * Within your Django project's `settings.py`, adjust the `DATABASES` settings for your desired database (SQLite, PostgreSQL, etc.).

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Contributing

Contributions are welcome! Please feel free to:

* **Report Issues:** Open issues for feature requests or bug reports.
* **Submit Pull Requests:**  Follow the project's style guide (if applicable) for code contributions.  

## License

MIT

