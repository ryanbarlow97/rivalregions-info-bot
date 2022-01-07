import json

dict = json.load(open("price_stats.txt"))
for i in dict:
    print(i)
    #print(", ".join(dict[i])) #list
    #for each in dict[i]: # removing pound symbols and spaces and adding enters for excel.
    #    print(each.split(" ")[0])
    print()