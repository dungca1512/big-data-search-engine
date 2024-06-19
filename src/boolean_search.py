from pyspark.sql import SparkSession
import article_title


def search_boolean_spark(file_path, keyword):
    spark = SparkSession.builder.appName("BooleanSearchSpark").getOrCreate()

    try:
        # Đọc dữ liệu từ file và chuyển đổi thành RDD
        data_rdd = spark.sparkContext.textFile(file_path)
        # Phân tách mỗi dòng thành cặp (khóa, danh sách giá trị)
        keyword_urls_rdd = data_rdd.map(lambda line: line.split('\t'))
        # Nhóm các giá trị theo khóa
        keyword_grouped_urls = keyword_urls_rdd.groupByKey()
        # Lọc danh sách các URL cho từ khóa cần tìm kiếm
        url_list = keyword_grouped_urls.filter(lambda x: x[0] == keyword).flatMap(lambda x: x[1]).collect()
    except FileNotFoundError as e:
        print("Error: File not found:", e)
        url_list = []  # Set empty list on file not found
    spark.stop()
    return url_list


def main():
    file_path = "/home/dungca/Desktop/big-data-search/resources/index/index.txt"
    while True:
        keyword = input("Nhập từ khóa tìm kiếm (hoặc 'q' để thoát): ")
        if keyword.lower() == 'q':
            break
        results = search_boolean_spark(file_path, keyword)
        if results:
            print(f"Danh sách URL chứa từ khóa '{keyword}':")
            for url in results[0].split(' '):
                print(article_title.get_page_title(url) + "\n")
                print(url + "\n")
        else:
            print(f"Không tìm thấy URL nào chứa từ khóa '{keyword}'.")


if __name__ == "__main__":
    main()
