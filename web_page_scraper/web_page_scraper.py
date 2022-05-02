import requests


def simple_parser():
    url = correct_input_url("Please input URL > ")
    response = requests.get(url)
    if response.ok: 
        result = response.json()
        print(result.get('content'))

    else:
        print("Invalid quote resource!")
        

def correct_input_url(string):
    url = input(string)
    if url.startswith('http://'):
        return url
    elif url.startswith('https://'):
        return url
    print("URL mast begin with http:// or https://")
    correct_input_url(string)


simple_parser()
