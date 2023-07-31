int cmp(int *a, int *b){
    return *a - *b;
}
int threeSumClosest(int* nums, int numsSize, int target){
    qsort(nums, numsSize, sizeof(int), cmp);
    int ans = 99999;
    int sum = 0;
    int i;
    for(i=0; i<numsSize-2; i++){
        if(i>0 && nums[i] == nums[i-1]){
            continue;
        }
        else{
            int j = i+1;
            int k = numsSize-1;
            while(j<k){
                sum = nums[i] + nums[j] + nums[k];
                if(abs(sum-target) < abs(ans-target)){
                    ans = sum;
                }
                if(sum > target){
                    // printf("bbb\n");
                    k--;
                }
                else if(sum < target){
                    j++;
                }
                else{
                    break;
                }
            }
        }
        
    }

    return ans;
}
int main(void){
	int nums[] = {4,0,5,-5,3,3,0,-4,-5};
	int targets = -2;
	int ans = threeSumClosest(nums, sizeof(nums)/sizeof(nums[0]), targets);
	printf("ans: %d",ans);
	
	
}
