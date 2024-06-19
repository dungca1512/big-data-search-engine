import json
from collections import defaultdict


def create_index(documents):
    # Tạo inverted index
    inverted_index = defaultdict(set)
    for doc in documents:
        url = doc['url']
        content = doc['content']
        for word in content.split():
            word = word.lower()
            inverted_index[word].add(url)

    # Tạo file index.txt và ghi chỉ số vào file
    with open('../resources/index/index.txt', 'w') as file:
        for key, urls in inverted_index.items():
            line = f"{key}\t{' '.join(urls)}"
            file.write(line + '\n')


if __name__ == '__main__':
    # Đọc dữ liệu từ file JSON
    with open('../resources/data/data.json', 'r') as file:
        documents = json.load(file)
    create_index(documents)


