import html


def create_link(text, url):
    encoded_text = html.escape(text)
    link = f'<a href="{url}">{encoded_text}</a>'
    return link


if __name__ == "__main__":
    # Ví dụ sử dụng
    text = "Tìm hiểu thêm về Python"
    url = "https://www.python.org/downloads/"

    link = create_link(text, url)
    print(link)
