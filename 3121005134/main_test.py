import unittest

import numpy as np

import paperChecked
import main


class MyTestCase(unittest.TestCase):

    # 测试读取空文件
    def test_read_empty_file(self):
        orig_path = ""
        orig_add_path = "C:/Users/L/Desktop/3121005134/3121005134/resource/orig_0.8_add.txt"
        paperChecked.file_handle(orig_path, orig_add_path)

    # 测试读取不存在的文件
    def test_read_notExist_file(self):
        orig_path = "C:/Users/L/Desktop/3121005134/3121005134/resource/orig_add.txt"
        orig_add_path = "C:/Users/L/Desktop/3121005134/3121005134/resource/orig_0.8_add.txt"
        paperChecked.file_handle(orig_path, orig_add_path)

    # 测试读取的文件能否过滤标点符号
    def test_filter_dot(self):
        orig_path = "C:/Users/L/Desktop/3121005134/3121005134/resource/orig.txt"
        orig_add_path = "C:/Users/L/Desktop/3121005134/3121005134/resource/orig_0.8_add.txt"
        orig_file, orig_add_file = paperChecked.file_handle(orig_path, orig_add_path)
        print(orig_file, orig_add_file)

    # 测试文件内容分词效果
    def test_segment(self):
        orig_path = "C:/Users/L/Desktop/3121005134/3121005134/resource/orig.txt"
        orig_add_path = "C:/Users/L/Desktop/3121005134/3121005134/resource/orig_0.8_add.txt"
        orig_file, orig_add_file = paperChecked.file_handle(orig_path, orig_add_path)
        orig_string, orig_add_string = paperChecked.segment(orig_file, orig_add_file)
        print(orig_string, orig_add_string)

    # 测试分词向量化效果
    def test_vectorize(self):
        orig_string = '今天 天气 很好 晴朗 舒适'
        orig_add_string = '今日 天气 非常好 晴 愉快'
        vector1, vector2 = paperChecked.vector_transform(orig_string, orig_add_string)
        print(vector1, vector2)

    # 测试余弦相似度计算
    def test_calculate_cos_similarity(self):
        vector1 = np.array([1, 2, 3, 4, 5, 6])
        vector2 = np.array([1, 2, 3, 4, 5, 6])
        similarity = paperChecked.calculate_cos_similarity(vector1, vector2)
        print(similarity)

    # 测试输出结果到指定文件中
    def test_save_file(self):
        answer_path = "C:/Users/L/Desktop/3121005134/3121005134/resource/answer02.txt"
        result = 0.86748569623
        similarity = paperChecked.save_file(answer_path, result)
        print(similarity)

    # 测试输出结果到不存在文件中
    def test_save_not_exist_file(self):
        answer_path = ""
        result = 0.86748569623
        similarity = paperChecked.save_file(answer_path, result)
        print(similarity)

    # 测试输出的结果不是浮点型
    def test_result_not_float(self):
        answer_path = "C:/Users/L/Desktop/3121005134/3121005134/resource/answer03.txt"
        answer = 2
        result = paperChecked.save_file(answer_path, answer)
        print(result)

    # 测试文章查重
    def test_paper_check(self):
        main.paper_check()


if __name__ == '__main__':
    unittest.main()
