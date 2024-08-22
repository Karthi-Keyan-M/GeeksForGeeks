#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        z=arr.count(0)
        o=arr.count(1)
        t=arr.count(2)
        c=0
        for i in range(z):
            arr[c]=0
            c+=1
        for j in range(o):
            arr[c]=1
            c+=1
        for k in range(t):
            arr[c]=2
            c+=1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends