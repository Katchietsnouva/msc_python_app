import json
fruits = {"apple":"red","orange":"green"}

with open('data\\fruit.json','w', encoding='utf-8') as file:
    json.dump(fruits,file, ensure_ascii=True, indent=1) 