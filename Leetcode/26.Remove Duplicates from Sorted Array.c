#include<stdio.h>
#include<stdlib.h>
int removeDuplicates(int* nums, int numsSize){
    int i,j;
    int count = 1;
    for(i=0; i<numsSize-1; i++){
        if(nums[i] != nums[i+1]){
            nums[count] = nums[i+1];
            count++;
        }
    }
    return count;
    
}
int main(void){
	int nums[] = {0,0,1,1,1,2,2,3,3,4};
	int nums_len = sizeof(nums)/sizeof(nums[0]);
	
	printf("nums : ");
	int i;
	for(i=0; i<nums_len; i++){
		printf("%d ",nums[i]);
	}
	
	int count = removeDuplicates(nums,nums_len);
	printf("\nnums 非重複值有%d個",count);
	
	int j;
	printf("\nnums 非重複的值為 : ");
	for(j=0; j<count; j++){
		printf("%d ",nums[j]);
	}
}

