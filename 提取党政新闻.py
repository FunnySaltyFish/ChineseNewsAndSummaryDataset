# 根据关键词提取党政新闻
keywords = ["党", "人民", "治理", "制度", "政府", "政策", "政治", "体制"]
keywords = set(keywords)

def match_keywords_more_than_3(sentence):
    i = 0
    for each in keywords:
        if each in sentence:
            i += 1
    if i >= 3:
        return True
    else:
        return False

import json
print("start to load data...")
d = json.load(open("./CNews_sum.json", "r", encoding="utf-8"))
data = d["data"]
l = len(data)
print(l)
result = []
for each in data:
    # 如果有三个及以上关键词匹配
    if match_keywords_more_than_3(each["content"]):
        result.append(each)
print(len(result))

print("start to load data...")
d = json.load(open("./nlpcc2017_clean.json", "r", encoding="utf-8"))
data = d["data"]
l = len(data)
print(l)
for each in data:
    # 如果有三个及以上关键词匹配
    if match_keywords_more_than_3(each["content"]):
        result.append(each)
print(len(result))

json.dump(result, open("CNews_sum_dz.json", "w", encoding="utf-8",), ensure_ascii=False, indent=2)
print("done")
