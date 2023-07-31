#include<stdio.h>
#include<stdlib.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
	
//	*returnSize=2;
//	for(int i = 0; i < 2; i++) {
//        printf("*(p + %d): %d\n", i , *(returnSize + i));
//    }
//	int * returnSize1=(int*)malloc(2*sizeof(int));
	int i,j;
	for(i=0; i<numsSize; i++){
		for(j=i+1; j<numsSize; j++){
			if(nums[i] + nums[j] == target){
				printf("%d %d\n",nums[i],nums[j]);
				printf("%d %d\n",i,j);
				returnSize[0] = i;
				returnSize[1] = j;
			} 
		}
	}
	return returnSize;
}

int main(void){
	
	int i,a;
	int nums[5];
	
	int ret2[2];
	int* returnSize = ret2;

	printf("請輸入五個數字:\n");
	for(i=0; i<5; i++){
		scanf("%d",&a);
		nums[i] = a;
	}
	
	printf("輸入一個目標數字:\n");
	int target;
	scanf("%d",&target);
	
	int returnSize1_index = 0;
	returnSize = twoSum(nums,5,target,returnSize);
	
	printf("結果:\n");
	for(returnSize1_index=0; returnSize1_index<2; returnSize1_index++){
		printf("%d ",returnSize[returnSize1_index]);
	}
}
