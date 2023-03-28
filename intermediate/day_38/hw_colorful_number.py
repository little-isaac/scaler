class Solution:
	# @param A : integer
	# @return an integer
    def colorful(self, n):
        # Convert input number to string
        s = str(n)
        # Initialize hash set to store products of consecutive subsequences
        products = set()
        # Loop over all possible subsequence lengths
        for length in range(1, len(s)+1):
            # Loop over all possible starting positions for current subsequence length
            for i in range(len(s)-length+1):
                # Calculate product of current subsequence
                product = 1
                for j in range(i, i+length):
                    product *= int(s[j])
                # If product is already in hash set, input number is not colorful
                if product in products:
                    return 0
                # Otherwise, add product to hash set
                products.add(product)
        # If we processed all possible subsequences without finding a duplicate product, input number is colorful
        return 1

solu = Solution()
array = [
    [23] , # 1
    [236] , # 0
    [99] , # 0
    [123] , # 0
]
for A in array:
    ans = solu.colorful(A[0])
    print("output for ",A," is ",ans)