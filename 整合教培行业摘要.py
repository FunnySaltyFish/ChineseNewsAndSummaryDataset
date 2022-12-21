import os
import re
import json

PATTERN_URL = r"!\[.*?]\(.+?\)"
# summary{{方直科技拟以自有资金1.2亿元共同投资设立嘉道方直投资基金}}
PATTERN_SUMMARY = r"summary{{(.+)}}"
PATTERN_TEXT = r"text{{(.+)}}"

files = os.listdir("./教培行业摘要")
print(len(files))

data = []

for each in files:
    if each.startswith("_") or each.startswith("."):
        continue
    with open("./教培行业摘要/" + each, "r", encoding="utf-8") as f:
        content = f.read()
        # print(content)
        arr = content.split("\n")
        data.append({
            "summary": re.sub(PATTERN_SUMMARY, r"\1", arr[0]),
            "content": re.sub(PATTERN_URL, "", re.sub(PATTERN_TEXT, r"\1", arr[1])),
        })

print(len(data))
with open("./教培行业摘要.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(data, ensure_ascii=False, indent=2))
