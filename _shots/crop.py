from PIL import Image
img = Image.open(r"E:\Project\2026\2609芜湖旅行\_shots\芜湖旅行计划_mobile.png")
w, h = img.size
print("size", w, h)
# alert-bar 区域（y 约 780-940）
img.crop((0, 780, w, 940)).save(r"E:\Project\2026\2609芜湖旅行\_shots\crop_alert.png")
# 美食清单区域（y 约 4790-5000）
img.crop((0, 4790, w, 5020)).save(r"E:\Project\2026\2609芜湖旅行\_shots\crop_food.png")
print("done")
