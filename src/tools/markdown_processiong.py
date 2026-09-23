import mistune
from bs4 import BeautifulSoup

def to_html_text(markdown_text) : 
    html_text = mistune.html(markdown_text)
    return html_text

def to_text(markdown_text) : 
    html_text = to_html_text(markdown_text)
    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text()
    return text

def to_html(markdown_text) : 
    html_text = to_html_text(markdown_text)
    return parse_html(html_text)

def parse_html(html_text) : 
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup