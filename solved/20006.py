import sys

input = sys.stdin.readline

p,m = map(int,input().split())

room_list = []

def joinable(room_info, playner_lv):
    if room_info[0]:
        return 0
    if room_info[1]-10<=playner_lv and room_info[1]+10>=playner_lv:
        return 1
    return 0


for _ in range(p):
    lv, name = map(str,input().split())
    cnt=1
    for room_info in room_list:
        if joinable(room_info,int(lv)):
            room_info[2].append([lv,name])
            if len(room_info[2])==m:
                room_info[0]=1
            cnt=0
            break        
    if cnt:
        if m==1:
            room_list.append([1,int(lv),[[lv,name]]])    
        else:
            room_list.append([0,int(lv),[[lv,name]]])

for room in room_list:
    if room[0]:
        print("Started!")
    else:
        print("Waiting!")
    user_list = sorted(room[2], key=lambda x: x[1])
    for user in user_list:
        print(*user)