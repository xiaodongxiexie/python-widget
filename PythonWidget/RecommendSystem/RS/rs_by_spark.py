# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/2/29

from pprint import pprint

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.ml.feature import StringIndexer, IndexToString
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.mllib.recommendation import ALS
from pyspark.mllib.recommendation import Rating
from pyspark.mllib.recommendation import MatrixFactorizationModel


class LoadFromFile:

    spark = None

    def __init__(self, path: str):
        self.path = path

    def read_csv(self) -> "spark.dataframe":
        return self.spark.read.csv(self.path, inferSchema=True, header=True)

    def create_view(self, dataframe, name) -> None:
        dataframe.registerTempTable(name)

    def load_then_create_view(self, name: str) -> "spark.dataframe":
        dataframe = self.read_csv()
        self.create_view(dataframe, name)
        return dataframe


def show(dataframe: "spark.dataframe", n: int = 20) -> None:
    dataframe.show(n=n, truncate=False)


if __name__ == '__main__':
    spark = SparkSession.builder.appName("rs.alpha").getOrCreate()
    LoadFromFile.spark = spark
    movie_ratings = LoadFromFile("../ml-latest-small/ratings.csv").load_then_create_view("ratings")
    movies = LoadFromFile("../ml-latest-small/movies.csv").load_then_create_view("movies")

    movies_join_ratings = spark.sql("""
                                            SELECT 
                                                ratings.userId,
                                                ratings.movieId,
                                                ratings.rating,
                                                movies.title,
                                                movies.genres
                                            FROM ratings
                                            LEFT JOIN movies
                                            ON ratings.movieId = movies.movieId
                                    """)
    show(movies_join_ratings)
    show(movies_join_ratings.groupBy("rating")
                            .count()
                            .withColumnRenamed("count", "rating_num")
                            .orderBy("rating", ascending=False))

    # 数据特征转换
    string_indexer = StringIndexer(inputCol="title", outputCol="title_to_index")
    string_indexer_model = string_indexer.fit(movies_join_ratings)
    movies_join_ratings_after_indexed = string_indexer_model.transform(movies_join_ratings)
    show(movies_join_ratings_after_indexed)

    # 划分训练集、测试集
    train_dataset, test_dataset = movies_join_ratings_after_indexed.randomSplit([0.8, 0.2])
    train_rating_data = train_dataset.selectExpr("userId as user", "title_to_index as product", "rating")
    test_rating_data  = test_dataset.selectExpr("userId as user", "title_to_index as product", "rating")
    train_rating_data = train_rating_data.rdd.map(lambda obj: Rating(obj.user, obj.product, obj.rating))
    test_rating_data  = test_rating_data.rdd.map(lambda obj: Rating(obj.user, obj.product, obj.rating))

    # 建模
    recommend_system_model = ALS.train(train_rating_data, rank=3,)

    # 预测
    predict_test_rating_data = recommend_system_model.predictAll(test_rating_data
                                                                 .map(lambda obj: (obj.user, obj.product)))

    # 推荐适合 product 204 编号的电影的指定个数的 User 编号
    pprint(recommend_system_model.recommendUsers(204, 10))
    # 推荐适合 User 357 的 指定个数的电影编号
    pprint(recommend_system_model.recommendProducts(357, 10))
    # 每个用户最值得推荐的指定个数电影编号
    pprint(recommend_system_model.recommendProductsForUsers(10))
    # 每个电影最适合的指定个数 User 编号
    pprint(recommend_system_model.recommendUsersForProducts(10))
