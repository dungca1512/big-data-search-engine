from pyspark.sql import SparkSession
import article_title


def search_boolean_spark(file_path, keyword):
    spark = SparkSession.builder.appName("BooleanSearchSpark").getOrCreate()

    try:
        # Read data from file and convert to RDD
        data_rdd = spark.sparkContext.textFile(file_path)
        # Split line into (key, value)
        keyword_urls_rdd = data_rdd.map(lambda line: line.split('\t'))
        # Group values by key
        keyword_grouped_urls = keyword_urls_rdd.groupByKey()
        # Filter the list of URLs for keywords to search for
        url_list = keyword_grouped_urls.filter(lambda x: x[0] == keyword).flatMap(lambda x: x[1]).collect()
    except FileNotFoundError as e:
        print("Error: File not found:", e)
        url_list = []  # Set empty list on file not found
    spark.stop()
    return url_list


def main():
    file_path = "/home/dungca/Desktop/big-data-search-engine/resources/index/index.txt"
    while True:
        keyword = input("Enter search keyword (or 'q' to exit): ")
        if keyword.lower() == 'q':
            break
        results = search_boolean_spark(file_path, keyword)
        if results:
            print(f"List of URLs containing keyword '{keyword}':")
            for url in results[0].split(' '):
                print(article_title.get_page_title(url) + "\n")
                print(url + "\n")
        else:
            print(f"No URLs containing the keyword {keyword} were found.")


if __name__ == "__main__":
    main()
