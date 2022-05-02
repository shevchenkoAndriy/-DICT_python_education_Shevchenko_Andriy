import requests
from bs4 import BeautifulSoup


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


def correct_input_url(string):
    url = input(string)
    if url.startswith('http://'):
        return url
    elif url.startswith('https://'):
        return url
    print("URL mast begin with http:// or https://")
    correct_input_url(string)


# simple_parser()
# parse_html_doc()
save_html_page()
