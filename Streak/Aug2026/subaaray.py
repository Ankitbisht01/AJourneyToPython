nums = [0,0]
k = 2


sub = []
freq = {}
largest  = float('-inf')

for i in range(0, len(nums)-k+1):
    sub.append(nums[i:i+k])

for i in range(0, len(sub)):
    for num in sub[i]:
        if num in freq:
            freq[num]+=1
        else:
            freq[num] = 1

for key, val in freq.items():
    if key > largest and val ==1:
        largest = key
    else:
        pass


print(sub)
print(largest)
