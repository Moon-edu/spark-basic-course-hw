import os
import lzma, tarfile
from concurrent import futures
import time

# 실행하기 전 sources.txt.zip 파일의 압축을 풀거나 그냥 실행하면 아래 __decompress_if_not 함수에 의해 자동으로 압축이 해제됩니다.
# 압축을 풀면 source-1.txt ~ source-10.txt까지 총 10개의 파일이 생성되며, 이를 병렬 처리해주시면 됩니다.
def find_wrong() -> int:
    pass

# 여기서부터는 절대 수정하지 마세요
def __decompress_if_not() -> None:
    exists = True
    files = []
    if os.path.exists("dataset"):
        files = os.listdir("dataset/")
        for i in range(1, 11):
            print("DEBUG Checking source-" + str(i))
            if "source-" + str(i) + ".txt" not in files:
                exists = False
                break
    else:
        exists = False

    if not exists:
        for f in files:
            if f.endswith(".txt"):
                print("DEBUG: Removing " + f)
                os.remove("dataset/" + f)

        zip_file_path = "../dataset/source.txt.xz"

        with tarfile.open(zip_file_path, "r:xz") as tar:
            tar.extractall("dataset")
    else:
        print("DEBUG: already decompressed")

if __name__ == "__main__":
    __decompress_if_not()
    find_wrong()
    