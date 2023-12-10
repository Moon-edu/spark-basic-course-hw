import os
import zipfile
from pyspark.sql import SparkSession

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
# 3) 길이가 5 이상인 단어가 몇 개인지 리턴을 합니다..
def find_all_longer_than_5() -> int:
    pass


# 실행하기 전 questions.csv.zip 파일의 압축을 풀거나 그냥 실행하면 아래 __decompress_if_not 함수에 의해 자동으로 압축이 해제됩니다.
# 압축을 풀면 dataset 디렉토리 밑에 questions.csv파일이 생기는데, 
# 이를 읽어 조건에 만족하도록 Transformation을 수행한 후 Dataframe을 반환하는 함수를 구현하세요.
# 1) 아래 함수의 주어진 SparkSession을 이용하여 dataset 디렉토리 밑에 있는 모든 파일을 읽습니다.
# 2) 파일은 2개의 칼럼을 가진 csv입니다 여기서 첫 번째 칼럼(영어 문장)을 공백(space)으로 분리하여 각각의 단어로 쪼갭니다.
# 3) 길이가 5 이상인 단어만 필터링하되, 중복을 제거한 후 몇 개인지 리턴을 합니다.
def find_all_longer_than_5_unique() -> int:
    pass



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
    # find_all_longer_then_5()
    __explode_example()
    