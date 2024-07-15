from assertpy import assert_that
import pytest

def ss_1_2_2_9(home_gnb_page_param, json_data):
    Auto_Home.ss_1_2_2_9(json_data[0]['ss_1_2']['ss_1_2_2_9']['use_type'],
                                   json_data[0]['ss_1_2']['ss_1_2_2_9']['value1'],
                                   json_data[0]['ss_1_2']['ss_1_2_2_9']['value2'],
                                   json_data[0]['ss_1_2']['ss_1_2_2_9']['value3'],
                                   json_data[0]['ss_1_2']['ss_1_2_2_9']['value4'])  # 1.2.2-9