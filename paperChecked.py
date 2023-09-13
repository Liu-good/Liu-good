import math
import sys

import jieba as jb
from sklearn.feature_extraction.text import TfidfVectorizer


# 处理文件函数
def file_handle(path1, path2):
    try:
        # 读取文件内容
        with open(path1, 'r', encoding='utf-8') as orig_file, open(path2, 'r', encoding='utf-8') as orig_add_file:
            orig_file = orig_file.read()
            orig_add_file = orig_add_file.read()
    except FileNotFoundError:
        print("请输入正确的文件路径")
        return FileNotFoundError
    # 定义两个变量，用于接收过滤标点符号后的文件内容
    first_file, second_file = '', ''
    # 过滤文件内容的标点符号
    dot_str = "\n\r 、，。；：？‘’“”''""！《》,.;:?!<>"
    for char in dot_str:
       first_file = orig_file.replace(char, '')
       second_file = orig_add_file.replace(char, '')
    return first_file, second_file


# 分词函数
def segment(orig_file, orig_add_file):
    # 使用结巴分词将文件内容分词，空格分隔关键词
    orig_string = ' '.join(jb.lcut(orig_file))
    orig_add_string = ' '.join(jb.lcut(orig_add_file))
    return orig_string, orig_add_string


# 将分词后的内容转换为向量
def vector_transform(orig_string, orig_add_string):
    # 使用TFIDF算法实现向量化
    tfidf_vec = TfidfVectorizer()
    text = [orig_string, orig_add_string]
    # 将文本内容转为向量
    features = tfidf_vec.fit_transform(text).toarray()
    return features[0], features[1]


# 计算余弦相似度函数
def calculate_cos_similarity(vector1, vector2):
    # 计算两个向量的余弦相似度，cos = 向量的数量积 / 模乘积
    dot = sum(vector1[i] * vector2[i] for i in range(len(vector1)))
    norm1 = math.sqrt(sum(pow(i, 2) for i in vector1))
    norm2 = math.sqrt(sum(pow(i, 2) for i in vector2))
    similarity = dot / (norm1 * norm2)
    # similarity = np.dot(features[0], features[1]) / (np.linalg.norm(features[0]) * np.linalg.norm(features[1]))
    return similarity


# 保存结果到文件中，保留两位小数
def save_file(answer_path, answer):
    with open(answer_path, 'w') as answer_file:
        print('%.2f' % answer, file=answer_file)


# 获取命令行参数
def get_args():
    args = []
    try:
        if len(sys.argv) < 4:
            raise ValueError
        else:
            for i in range(1, 4):
                if isinstance(sys.argv[i], str):
                    args.append(sys.argv[i])
                else:
                    raise TypeError
    except ValueError:
        print("请输入正确的参数个数")
        return ValueError
    except TypeError:
        print("请输入正确的参数类型")
        return TypeError
    return args
