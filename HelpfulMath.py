nums = input().split('+')
nums.sort() 
str =""
for i in range(len(nums)):
    if i != len(nums)-1:
        str += nums[i]+'+'
    else:
        str += nums[i]
print(str)        