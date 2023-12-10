import os
import zipfile
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import explode, split

def build_sparksession() -> SparkSession:
    return SparkSession.Builder() \
        .appName("PySparkExample") \
        .master("local[8]") \
        .getOrCreate()

# 실행하기 전 questions.csv.zip 파일의 압축을 풀거나 그냥 실행하면 아래 __decompress_if_not 함수에 의해 자동으로 압축이 해제됩니다.
# 압축을 풀면 dataset 디렉토리 밑에 questions.csv파일이 생기는데, 
# 이를 읽어 조건에 만족하도록 Transformation을 수행한 후 Dataframe을 반환하는 함수를 구현하세요.
# 1) 아래 함수의 주어진 SparkSession을 이용하여 dataset 디렉토리 밑에 있는 모든 파일을 읽습니다.
# 2) 파일은 2개의 칼럼을 가진 csv입니다 여기서 첫 번째 칼럼(영어 문장)을 공백(space)으로 분리하여 각각의 단어로 쪼갭니다.
# 3) 길이가 5 이상인 단어만 필터링합니다. 해당 데이터 프레임을 반환합니다.
# Hint1: SparkSession에서 csv파일을 어떻게 읽는지 기억하세요
# Hint2: split 함수를 사용하면 단어로 쪼갤 수 있습니다.
# Hint3: split 함수를 사용한 결과는 Array[String] 타입이므로, 이를 DataFrame으로 변환하기 위해선 explode 함수를 사용해야 합니다.
# 즉(예를 들어) 레코드가 "a b c d e"라면 split 이후 array("a", "b", "c", "d", "e")가 되고, 
# explode 이후 1개의 array 레코드가 총 5개의 레코드("a", "b", "c", "d", "e")로 뻥튀기 됩니다.
# Hint4: explode 이후에 각각의 레코드는 1개의 단어가 되며 이를 필터링하기 위해선 length 함수를 사용할 수 있습니다.
# Hint5: 이 함수는 Transformation이 된 Dataframe을 반환해야 합니다. 어떠한 Action도 사용해서는 안됩니다.
def find_all_longer_than_5() -> DataFrame:
    pass






def __explode_example():
    spark = build_sparksession()

    df_split = spark.createDataFrame([("a b c d e",)], ["numbers"])
    df_split.select(split("numbers", " ").alias("words")).show()

    df = spark.createDataFrame([([1,2,3,4,5],)], ["numbers"])
    df.show()

    df2 = df.select(explode(df.numbers).alias("number"))
    df2.show()



# 여기서부터는 절대 수정하지 마세요
def __decompress_if_not() -> None:
    files = os.listdir("dataset/")
    exists = True
    print("DEBUG Checking questions.csv")
    if "questions.csv" not in files:
        exists = False

    if not exists:
        for f in files:
            if f.endswith(".csv"):
                print("DEBUG: Removing " + f)
                os.remove("dataset/" + f)

        zip_file_path = "dataset/questions.csv.zip"
        extract_to_dir = os.path.dirname(os.path.abspath(zip_file_path))
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to_dir)
    else:
        print("DEBUG: already decompressed")

if __name__ == "__main__":
    __decompress_if_not()
    __explode_example()
    find_all_longer_than_5().show()
    