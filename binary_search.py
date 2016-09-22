#!/usr/bin/python env
# -*- coding:utf-8 -*-
def search(arr,n,v):
	left = -1
	right = n
	while(left+1 != right):
		mid = left + (right - left)/2
		if(arr[mid] < v):
			left = mid
		else:
			right = mid
	if(right >= n or arr[right] != v):
		right = -1
	return right

if __name__=='__main__':
	arr = [1,2,3,23,87,90,555,1222,13333]
	n = len(arr)
	ret = search(arr,n,87)
	print ret