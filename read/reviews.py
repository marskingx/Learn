# 分析留言

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1  # count = count +1
        if count % 1000 == 0:
            print(len(data))

# print(data[0])
# print('------------------')
# print((data[1]))
print('檔案讀完了，總共有', len(data), '筆資料')

print(data[0])

wc = {}  # 文字計數
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1  # 新增新的key進入wc字典

for word in wc:
    if wc[word] > 100:
        print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
    word = input('請問你想查什麼字?')
    if word == 'Q':
        break
    print(word, '出現過的次數為：', wc[word])

print('感謝使用本查詢功能')

# sum_len = 0
# for d in data:
#     sum_len += len(d)
#     print(sum_len)
# print('平均是', sum_len / len(data))
#
# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)
# print("一共有", len(new), "筆留言小於100個單字")
# print(new[0])
# print(new[1])
#
# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
# print('一共有', len(good), '筆資料有含GOOD')
# print(good[0])
#
# good = [d for d in data if 'good' in d]
# print(len(good))
#
# test = []
# for t in data:
#     if 'test' in t:
#         good.append(t)
# print('一共有', len(test), '筆資料有含test')
# print(test)
#
# test = [t for t in data if 'test' in t]
# print(test)
