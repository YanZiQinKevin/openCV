
def quicksort(nums,left,right):
	if (left>=right):
		return
	temp=nums[left]

	i=left
	j=right

	while (i!=j):
		while (j>i and nums[j]>=temp):
			j-=1
		while (j>i and nums[i]<=temp):
			i+=1
		if i<j:
			tmp=nums[i]
			nums[i]=nums[j]
			nums[j]=tmp

	nums[left] =nums[i]
	nums[i]=temp
	quicksort(nums,left,i-1)
	quicksort(nums,i+1,right)



def quickshort(nums):
	if len(nums) <=1:
		return nums

	frond = list()
	back = list()
	v = nums.pop()

	for x in nums:
		if x < v:
			frond.append(x)
		else:
			back.append(x)
	return quickshort(frond)+[v]+ quickshort(back)


a=[2,6,3,2,68,9,3]
quicksort(a,0,len(a)-1)
print(a)
#answer=quickshort(a)
#print(answer)