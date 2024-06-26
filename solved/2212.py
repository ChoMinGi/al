N = int(input())
K = int(input())
sensor = sorted(list(set(map(int,input().split()))))
diff = []
for i in range(len(sensor)):
    sensor[i] = [sensor[i],sensor[i]]
    if i < len(sensor)-1:
        diff.append(sensor[i+1]-sensor[i][0])

while(len(sensor)>K):
    min_idx = diff.index(min(diff))

    fin_sensor = sensor[min_idx+1]
    sensor.pop(min_idx+1)
    sensor[min_idx][1] = fin_sensor[1]

    diff.pop(min_idx)

res = 0 
for s,f in sensor:
    res += (f-s)

print(res)
# 1 3 6 6 7 9

# 1,1 3,3 6,6 7,7 9,9
#   2   3   1   2

# 1,1 3,3 6,7 9,9
#   2   3   2

# 1,3 6,7 9,9
#   3   2

# 1,3 6,9

