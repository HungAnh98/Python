def largestNumInList(_list):
	maxNum = _list[0]
	idx = 0
	for i in _list:
		if i > maxNum:
			maxNum = i
	return maxNum
def binarySearch (_list, l, r, x): 
	if r >= l: 
		mid = l + (r - l) // 2
		if _list[mid] == x: 
			return mid 
		elif _list[mid] > x: 
			return binarySearch(_list, l, mid-1, x) 
		else: 
			return binarySearch(_list, mid + 1, r, x) 
	else: 
		return -1

def bubbleSort(_list):
	_len = len(_list)
	for i in range(_len):
		for j in range(0, _len-i-1):
			if _list[j] > _list[j+1]:
				_list[j], _list[j+1] = _list[j+1], _list[j]
print("Enter a sequence of numbers separated by spaces")
Str = input()                 
_list = list(map(int, Str.split()))
print("The largest number is : ",largestNumInList(_list))
bubbleSort(_list)
for l in _list:
	print(l)
print("Enter the number you want to find : ")
x = int(input())
indx = binarySearch(_list,0,len(_list),x)
print("The index of the number ",x," is : ",indx)




