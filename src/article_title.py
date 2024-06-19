import requests
from bs4 import BeautifulSoup


def get_page_title(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.content
            soup = BeautifulSoup(html_content, "html.parser")

            title_tag = soup.find("title")
            if title_tag:
                page_title = title_tag.text.strip()
                return page_title
            else:
                return None
        else:
            raise Exception(f"Error accessing website: {response.status_code}")

    except Exception as e:
        raise Exception(f"Error extracting title: {e}")


if __name__ == "__main__":
    url = input("Nhập URL trang web: ")
    page_title = get_page_title(url)

    if page_title:
        print(f"Tiêu đề trang web: {page_title}")
    else:
        print("Không thể lấy tiêu đề trang web.")