# Quick WHO Scraper writtin at midnight

goodOnes = {}

print("typing")

import urllib.request, json 
with urllib.request.urlopen("https://apps.who.int/gho/athena/api/GHO?format=json") as url:
    data = json.loads(url.read().decode())

print(len(data["dimension"][0]["code"]))


try:
    for dim in range(len(data["dimension"][0]["code"])):
        try:
            label = data["dimension"][0]["code"][dim]["label"]
            print(dim, label)
            with urllib.request.urlopen(f"https://apps.who.int/gho/athena/api/GHO/{label}?format=json&profile=simple") as url2:
                data2 = json.loads(url2.read().decode())
            try:
                int(data2["fact"][0]["dim"]["YEAR"])
                obj = {
                    "Title": data["dimension"][0]["code"][dim]["display"],
                    "Unit": "",
                    "Size": len(str(data2)),
                    "Reversed": False
                }
                goodOnes[label] = obj
                print(obj)
            except Exception as e:
                print("fail")
                print(e)
                continue
        except Exception as e:
            print("ultra fail")
            print(e)
            continue
except Exception as e:
    print(e)
    pass

print("\n\n\n\n\n\n\n\n")
print(json.dumps(goodOnes))

text_file = open("Output.txt", "w")
text_file.write(json.dumps(goodOnes))
text_file.close()















input()