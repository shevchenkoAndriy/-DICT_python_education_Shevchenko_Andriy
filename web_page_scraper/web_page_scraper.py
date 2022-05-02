import requests
from bs4 import BeautifulSoup
import string

BASE_URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=3"


def simple_parser():
    url = correct_input_url("Please input URL > ")
    response = requests.get(url)
    if response.ok:
        result = response.json()
        print(result.get('content'))

    else:
        print("Invalid quote resource!")


def parse_html_doc():
    url = correct_input_url("Please input URL > ")
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

    try:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        title = soup.h1.string
        description = soup.find('meta', {'name': 'description'})
        if not title or not description:
            raise AttributeError()
        film_info = {"title": title, "description": description["content"]}
        print(film_info)

    except AttributeError:
        print("Invalid movie page!")


def save_html_page():
    url = correct_input_url("Please input URL > ")
    response = requests.get(url)
    if response.ok:
        save_in_file(response.content)
    else:
        print(f"The URL returned {response.status_code}")


def save_in_file(page):
    with open("web_page.html", "wb") as f:
        f.write(page)
        print("Content saved.")


def parsed_articles():
    response = requests.get(BASE_URL)
    if response.ok:
        links = get_tuple_links(response)

    else:
        print(f"The URL returned {response.status_code}")


def correct_input_url(string):
    url = input(string)
    if url.startswith('http://'):
        return url
    elif url.startswith('https://'):
        return url
    print("URL mast begin with http:// or https://")
    correct_input_url(string)


def get_tuple_links(response):
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    links_tags = soup.find_all("a", class_="c-card__link")
    return map(lambda x: (x.text, x["href"]), links_tags)


def get_article_by_link(link):
    name, path = link
    host = "https://www.nature.com"
    response = requests.get(f"{host}{path}")
    if response.ok:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        div = soup.find("div", class_="c-article-body u-clearfix")
        save_article(name, div.text)


def save_article(name: string, content):
    name = name.replace(" ", "_")
    print("Name: ", name)
    with open(f"articles/{name}.txt", "w") as f:
        f.write(content)
        print("Content saved.")


# simple_parser()
# parse_html_doc()
# save_html_page()
# parsed_articles()
get_article_by_link(('Base edit your way to better crops', '/articles/d41586-022-01117-z'))
