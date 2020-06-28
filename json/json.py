# 儲存檔案
# file=open("data.txt", mode="w", encoding="utf-8") # 開啟
# file.write("Hello file\nSecond Line\n怪屁股啾") # 操作
# file.close() # 關閉
# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("測試中文\n好棒棒")

# # 讀取檔案
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     data=file.read()
# print(data)

# 把檔案數字資料一行一行讀取並加總
sum=0
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n3")
with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file: # 一行一行的讀取
        sum+=int(line)
print(sum)

# 使用 JSON 格式讀取、複寫檔案
import json
# 從檔案中讀取JSON資料，放入變數data裡面
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data) # data 是一個字典資料
data["name"]="NEW NAME" # 修改變數中的資料
# 把最新的資料複寫回檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)

# print("Name: ", data["name"])
# print("Version: ", data["version"])
