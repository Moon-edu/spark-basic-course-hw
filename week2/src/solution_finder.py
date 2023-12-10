import os
import zipfile
from concurrent import futures
import time

# 실행하기 전 sources.zip 파일의 압축을 풀거나 그냥 실행하면 아래 __decompress_if_not 함수에 의해 자동으로 압축이 해제됩니다.
# 압축을 풀면 source-1.txt ~ source-10.txt까지 총 10개의 파일이 생성되며, 이를 병렬 처리해주시면 됩니다.

def get_partial_wrong_count(num):
    print(f"DEBUG: Process {num} start")
    
    FILE=f"dataset/source-{num}.txt"
    wrong_cnt = 0

    with open(FILE, "r", encoding="utf-8") as f:
        for n in f:
            sum = 0
            for w in n.split(","):
                sum = sum + int(w)
                if (sum > 100):
                    wrong_cnt = wrong_cnt + 1
                    break
                
    print(f"DEBUG: Process {num} done")
    return wrong_cnt

def find_wrong():
    start_time = time.time()

    with futures.ProcessPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(get_partial_wrong_count, list(range(1, 11)))) # Collection of partial count
    sum = 0
    for r in results:
        sum = sum + r

    end_time = time.time()
    print(f"Fast result {sum}, took: {end_time - start_time}")
    return sum

# 여기서부터는 절대 수정하지 마세요
def __decompress_if_not() -> None:
    files = os.listdir("dataset/")
    exists = True
    for i in range(1, 11):
        print("DEBUG Checking source-" + str(i))
        if "source-" + str(i) + ".txt" not in files:
            exists = False
            break

    if not exists:
        for f in files:
            if f.endswith(".txt"):
                print("DEBUG: Removing " + f)
                os.remove("dataset/" + f)

        zip_file_path = "dataset/source.txt.zip"
        extract_to_dir = os.path.dirname(os.path.abspath(zip_file_path))
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to_dir)
    else:
        print("DEBUG: already decompressed")

def slow_find_wrong():
    start_time = time.time()
    wrong_cnt = 0
    for i in range(1, 11):
        FILE = "dataset/source-" + str(i) + ".txt"
        with open(FILE, "r", encoding="utf-8") as f:
            for n in f:
                sum = 0
                for w in n.split(","):
                    sum = sum + int(w)
                    if (sum > 100):
                        wrong_cnt = wrong_cnt + 1
                        break
    end_time = time.time()
    print(f"Slow result {wrong_cnt}, took: {end_time - start_time}")


if __name__ == "__main__":
    __decompress_if_not()
    slow_find_wrong()
    find_wrong()
    
    # print(f"총 출현 단어 갯수: {total_cnt}, 고유 단어 갯수: {unique_cnt}")
