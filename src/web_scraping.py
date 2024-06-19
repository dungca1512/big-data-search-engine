import requests
from bs4 import BeautifulSoup
import json
import re
import os


def extract_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return ' '.join([p.get_text() for p in soup.find_all('p')])


def extract_date(url):
    response = requests.get(url)
    html = response.content.decode('utf-8')
    pattern = re.compile(r'<script type="application/ld\+json">(.*?)</script>')
    json_matches = pattern.findall(html)
    for json_str in json_matches:
        try:
            data = json.loads(json_str)
            date_published = data.get('datePublished')
            if date_published:
                return date_published
        except (ValueError, KeyError):
            pass
    return ''


def get_urls(domain):
    response = requests.get(domain)
    html = response.content.decode('utf-8')
    pattern = re.compile(r'https://vnexpress\.net/[\w-]+\d+\.html')
    return set(pattern.findall(html))


def save_json(links, path):
    json_objects = [{'url': link, 'content': extract_text(link), 'date': extract_date(link)} for link in links]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(json_objects, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    domains = [
        "https://vnexpress.net/thoi-su",
        "https://vnexpress.net/goc-nhin",
        "https://vnexpress.net/the-gioi",
        "https://vnexpress.net/podcast",
        "https://vnexpress.net/kinh-doanh",
        "https://vnexpress.net/bat-dong-san",
        "https://vnexpress.net/khoa-hoc",
        "https://vnexpress.net/giai-tri",
        "https://vnexpress.net/the-thao",
        "https://vnexpress.net/phap-luat",
        "https://vnexpress.net/giao-duc",
        "https://vnexpress.net/suc-khoe",
        "https://vnexpress.net/doi-song",
        "https://vnexpress.net/du-lich",
        "https://vnexpress.net/so-hoa",
        "https://vnexpress.net/oto-xe-may",
        "https://vnexpress.net/y-kien",
        "https://vnexpress.net/tam-su",
        "https://vnexpress.net/thu-gian"
    ]
    path = "../resources/data/data.json"
    merged_links = set()
    for domain in domains:
        links = get_urls(domain)
        merged_links.update(links)
    save_json(merged_links, path)
