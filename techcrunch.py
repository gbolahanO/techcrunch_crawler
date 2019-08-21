from bs4 import BeautifulSoup
import requests


def techcrunch(url):
    # make requests to web page url
    response = requests.get(url)
    # read the content of the server's response
    content = response.text
    # parse the web page to BeautifulSoup which represents the document as a nested data structure
    soup = BeautifulSoup(content, 'html.parser')
    # find all links with the class 'post-block__title__link'
    links = soup.find_all('a', {'class': 'post-block__title__link'})
    # loop through all the links and get the text within the tag
    for link in links:
        print(link.string)


# call the techcrunch method
techcrunch('https://techcrunch.com')
# techcrunch("https://techcrunch.com/apps")
# techcrunch("https://techcrunch.com/gadgets")
# techcrunch("https://techcrunch.com/startups")

# read a single news


def read_crunch(url):
        # make requests to web page url
    response = requests.get(url)
    # read the content of the server's response
    content = response.text
    # pass the html document to beautiful which represents the document as a nested data structure
    soup = BeautifulSoup(content, 'html.parser')
    # find div with the class 'article-content'
    body = soup.find('div', {'class': 'article-content'})
    # print the text of the document
    print(url)
    print(body.text)


print()
print()

# call the read_crunch method
read_crunch("https://techcrunch.com/2019/08/21/volocopter-reveals-its-first-commercial-aircraft-the-volocity-air-taxi/")
