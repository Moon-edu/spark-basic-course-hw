# 과제 설명
다음 조건을 만족하도록 `get_count` 함수를 채워넣으세요. 함수는 `week1/src/wordcount.py`에 정의되어 있습니다.  

1. `week1/dataset/questions.txt`를 읽어와서 파일에 있는 총 단어 갯수를 세고, 고유한 단어의 갯수를 세는 프로그램입니다. 단어는 스페이스로 구분합니다.  
예를 들어 He is a boy, She is a girl이면, He/is/a/boy,/She/is/a/girl로 총 8개의 단어이며, 고유한 단어의 갯수는 중복이 제거된 He/is/a/boy,/She/girl로 총 6개입니다. (is, a는 2번 출현했으나 1번만 카운트)
2. 함수는 두 int값을 Tuple로 리턴합니다. Tuple의 첫 번째 값은 총 단어 갯수이며, 두 번째 값은 고유한 단어의 갯수입니다.
```python
# example
def get_count()-> Tuple[int, int]:
    total_word_cnt = ...
    unique_word_cnt = ...

    return (total_word_cnt, unique_word_cnt) # Tuple의 첫 번째 값은 총 단어 갯수, 두 번째 값은 고유한 단어의 갯수입니다.
```
위의 `He is a boy, She is a girl`의 경우는 (8, 6)이 리턴되어야 합니다.

# 참고 사항
1. `wordcount.py` 최초 실행시 파일 압축을 풀기때문에 약간의 시간이 걸릴 수 있습니다.
2. 코드에서 파일에 접근할 때 파일 경로는 "dataset/questions.txt"로 하면 됩니다.
```python
f = open("dataset/questions.txt")
```


# 주의 사항
`__score__.py` 파일은 채점을 위한 파일로 이 파일을 수정해서는 안됩니다.

그럼 Good luck!