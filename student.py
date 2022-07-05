student=[
{'Name':'Joseph','Score':85},
{'Name':'James','Score':70},
{'Name':'Mary','Score':90},
{'Name':'Tony','Score':65},
{'Name':'Tuu','Score':49},
{'Name':'Pom','Score':51},
]
for e in student:
    if e['Score'] >= 80:
        print(e['Name'],e['Score'],'grade:4')
    elif e['Score'] >= 70:
       print(e['Name'],e['Score'],'grade:3') 
    elif e['Score'] >= 60:
        print(e['Name'],e['Score'],'grade:2')
    elif e['Score'] >= 50:
        print(e['Name'],e['Score'],'grade:1')
    else:
        print(e['Name'],e['Score'],'grade:0')
    #จิรัชยา บุญอากาศ ม.6/14 35
