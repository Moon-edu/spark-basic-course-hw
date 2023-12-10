"""
이 파일은 채점을 위한 파일로 절대로 수정해서는 안됩니다.
"""
import transformer

EXPECTED_TOTAL_CNT = 1165987

actual_total_cnt = transformer.find_all_longer_then_5()

assert actual_total_cnt == EXPECTED_TOTAL_CNT

