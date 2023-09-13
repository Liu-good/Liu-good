import unittest
import paperChecked


class MyTestCase(unittest.TestCase):
    # 测试读取空文件
    def test_read_empty_file(self):
        orig_path = ""
        orig_add_path = "C:/Users/L/Desktop/3121005134/resource/orig_0.8_add.txt"
        paperChecked.file_handle(orig_path, orig_add_path)
    # 测试读取不存在得文件
    def test_read_notExist_file(self):
        orig_path = "C:/Users/L/Desktop/3121005134/resource/orig_add.txt"
        orig_add_path = "C:/Users/L/Desktop/3121005134/resource/orig_0.8_add.txt"
        paperChecked.file_handle(orig_path, orig_add_path)


if __name__ == '__main__':
    unittest.main()
