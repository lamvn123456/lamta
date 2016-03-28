import sys 
import heapq
if __name__ == "__main__":	
	f = sys.stdin
	k = int(f.readline().strip())
	a = []
	answer = []
	second = []
	secondindex = []
	for i in range(k):
		c = []
		for line in f.readline().strip().split():		
			heapq.heappush(c, int(line))
		a.append(c)
	minsum = 0
	for i in range(k):
		minsum += a[i][0]
		for y in range(k-1,-1,-1):
			a[i][y] = a[i][y] - a[i][0]
		heapq.heappop(a[i])
	answer.append(minsum)
	while (len(answer) < k):
		low = a[0][0]
		pos = 0
		for i in range(k):
			if (low > a[i][0]):
				low = a[i][0]
				pos = i
		answer.append(minsum+low)
		for i in range(len(second)):
			if pos != secondindex[i] and len(answer) < k:
				answer.append(minsum+second[i]+low)
		second.append(heapq.heappop(a[pos]))
		secondindex.append(pos)
	print(answer)
