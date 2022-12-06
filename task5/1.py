
def max_heapify(A, k) :
   l = 2*k+1
   r = 2*k+2
   if l < len(A) and A[l] > A[k]:
      largest = l
   else:
      largest = k
   if r < len (A) and A[r]> A[largest]:
      largest = r
   if largest != k:
      A[k], A[largest] = A[largest], A[k]
      max_heapify(A,largest)

def buildmaxheap (A):
   n = int((len (A) //2)-1)
   for k in range (n, -1, -1):
     max_heapify(A,k)
n=int(input())
l1=[]
for i in range (n):
    Numbers=int(input())
    l1.append(Numbers)
buildmaxheap(l1)
print (l1)