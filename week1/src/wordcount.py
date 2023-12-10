from typing import Tuple
import lzma
import os


# pass를 지우고 README.md에 명시된 조건을 만족하는 함수를 여기에 작성하세요
# Hint: 데이터 파일 경로는 dataset/questions.txt. 아래와 같이 읽어오면 됩니다.
# open("dataset/questions.txt")
def get_count() -> Tuple[int, int]:
    pass
    



# 여기서부터는 절대 수정하지 마세요
def __decompress_if_not() -> None:
    if not os.path.exists("dataset/questions.txt"):
        dest_file = "dataset/questions.txt"
        zip_file_path = os.path.abspath(f"../{dest_file}.xz")
        extract_to = os.path.abspath(dest_file)
        with lzma.open(zip_file_path, "rb") as r, open(extract_to, "wb") as w:
            w.write(r.read())

if __name__ == "__main__":
    __decompress_if_not()

    total_cnt, unique_cnt = get_count()
    print(f"총 출현 단어 갯수: {total_cnt}, 고유 단어 갯수: {unique_cnt}")
