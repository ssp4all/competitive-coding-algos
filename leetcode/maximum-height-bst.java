https://leetcode.com/discuss/interview-question/968148/wissen-softwere-engineering-oa-maximum-height

/*
Question:-  You are given an array of positive integer. You are required to construct a BST based on following rules:

1. You can choose any element A[i] as root 0 <= i < N
2. If j < i, then A[j] must be in left subtree of the root node
3. If j > i, then A[j] must be in right subtree of the root node


Constraints:
1 <= N <= 10^5
1 <= A[i] <= 10^5


Output: Print Maximum height can be possible
Example:

Given A = [5, 4, 6, 2, 3, 4]

One BST possible is 
  
2
 \
  3
   \
    4
	
Similarly, We can form   2 more BSTs 6 as root. But height of those trees also is 2. So, Output for this is 2.
*/
	if(nums == null || nums.length == 0)
		return 0;
	int len = nums.length;
	
	int[][] arr = new int[len][2];
	
	for(int i = 0 ; i < len; i++)
	{
		int min = 0, max = 0;
		
		for(int j = 0 ; j < len; j++)
		{
			if(i == j || nums[i] == nums[j])
				continue;
			else if( j < i && nums[j] < nums[i])
				min++;
			else if( j > i && nums[j] > nums[i])
				max++;
		}
		
		arr[i][0] = min;
		arr[i][1] = max;
	}
	
	
	int answer = 0;
	
	for(int[] a: arr)
		answer = Math.max(answer, Math.max(a[0], a[1]));
	return answer + 1;