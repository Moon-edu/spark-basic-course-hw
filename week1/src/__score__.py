import wordcount

EXPECTED_TOTAL_CNT = 162233152
EXPECTED_UNIQUE_CNT = 2436985

actual_total_cnt, actual_unique_cnt = wordcount.get_count()

assert actual_total_cnt == EXPECTED_TOTAL_CNT
assert actual_unique_cnt == EXPECTED_UNIQUE_CNT

