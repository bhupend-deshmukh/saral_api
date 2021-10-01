import requests
import json

f=requests.get("http://saral.navgurukul.org/api/courses").text
data=json.loads(f)
with open("maindata.json","w") as f:
    json.dump(data,f,indent=4)

a=1
id=[]
for i in data['availableCourses']:
    print(str(a)+"} "+i['name'])
    id.append(i['id'])
    a+=1
    
user1=int(input("enter the number:-"))
print("")
mm=requests.get(f"http://saral.navgurukul.org/api/courses/{id[user1-1]}/exercises").text    
m0=json.loads(mm)

with open("midledata.json","w") as z:
    json.dump(m0,z,indent=4)

b=1 
sluge={}
qe={}

for k1 in m0["data"]:
    print(str(b)+"}",k1["name"])    
    x1=1
    qe[str(b)]=k1["slug"] 
    for k2 in k1["childExercises"]:
        print("             "+str(b)+"."+str(x1)," "+k2["name"])
        sluge[str(b)+"."+str(x1)]=k2["slug"]
        qe[str(b)+"."+str(x1)]=k2["slug"]
        x1+=1
    b+=1

user2=input("enter the num:-")
llll=requests.get(f"http://saral.navgurukul.org/api/courses/{id[user1]}/exercise/getBySlug?slug={qe[user2]}").text
l=json.loads(llll)

with open("lastdata.json","w") as n:
    json.dump(l,n,indent=4)
data=l["content"]
main_data=json.loads(data)

for x in main_data:
    for y in x:
        co=x["value"]
    print(co)
