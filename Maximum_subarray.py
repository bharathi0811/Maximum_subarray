a = int(input("Enter the array size(A): "))
b = int(input("Enter the Maximum number (B):"))
array=list(map(int,input("Enter the Array Elements: ").split()))
class MaximumSubarray:
    @staticmethod
    def max_sub(array, a, b):
        n = len(array)
        l = []
        for i in range(n):
            for j in range(i, n):
                l.append(array[i:j + 1])
        count = 0
        for k in l:
            new = k
            sum_ = 0
            for m in new:
                sum_ += m
            if sum_ < b:
                count += 1
        return count
obj=MaximumSubarray()
print(obj.max_sub(array,a,b))


