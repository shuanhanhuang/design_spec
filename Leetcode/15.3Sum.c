#include<stdio.h>
#include<stdlib.h>
//int index = 0;
//void transfer(int* temp,int** returnColumnSizes){
//	printf("returnColumnSizes11: %d\n",**returnColumnSizes);
//    returnColumnSizes[index] = (int*)malloc(sizeof(int)*3);
//    returnColumnSizes[index] = temp;
//    index ++;
//}
 int cmp(int *a, int *b)
 {
     printf("%d,%d\n",*a,*b);
     return *a - *b;
 }
int** threeSum(int *nums, int numsSize, int *returnSize)
{
    int **rst;
    int rstSize = 0;
    int basicSize = 8;
    int i, j, k, sum;

//    rst = (int **)malloc(sizeof(int *) * basicSize);
////    *returnColumnSizes = (int **)malloc(sizeof(int) * basicSize);
//	int it,jt;
//    for(it=0;it<numsSize-1;it++){
//        int min = it;
//        for(jt=it+1; jt<numsSize; jt++){
//            if(nums[jt]< nums[min]){
//                min = jt;
//            }
//        }
//        int temp = nums[min];
//        nums[min]  = nums[it];
//        nums[it] = temp;
//    }
//
//     for(it=0;it<numsSize;it++){
//         printf("%d ",nums[it]);
//     }
//	
//	printf("\n");
     qsort(nums, numsSize, sizeof(int), cmp);

    for (i = 0; i < numsSize - 1; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }

        j = i + 1;
        k = numsSize - 1;
        while (j < k) {
            sum = nums[i] + nums[j] + nums[k];
            if (sum == 0) {
                rst[rstSize] = (int *)malloc(sizeof(int) * 3);
//                (*returnColumnSizes)[rstSize] = 3;
                rst[rstSize][0] = nums[i];
                rst[rstSize][1] = nums[j];
                rst[rstSize][2] = nums[k];

                rstSize++;

                while (j < k && nums[j] == nums[j + 1]) {
                    j++;
                }
                j++;
                k--;

                if (rstSize == basicSize) {
                    basicSize *= 2;
                    rst = (int **)realloc(rst, sizeof(int *) * basicSize);
//                    (*returnColumnSizes) = (int **)realloc((*returnColumnSizes),sizeof(int) * basicSize);
				}

            } else if (sum > 0) {
                k--;
            } else {
                j++;
            }
        }
    }

    *returnSize = rstSize;

    return rst;
}
int main(void){
	int nums[] = {0,1,1};
	int numsSize = 3;
	int index1,tempindex;
	int size = 0;
	int* returnSize = &size;
//	int ColumnSizes[2][3] = {{32,29,3},{4,5,6}};
	int **returnColumnSizes;
	int** answer = threeSum(nums, numsSize, returnSize);
	
//	printf("%d  \n",answer[0][1]);
//	printf("%d",*returnSize);
	printf("answer \n");
	for(tempindex=0; tempindex< size; tempindex++){
		for(index1 =0; index1<3; index1++){
 			printf("%d   ",answer[tempindex][index1]);
		}
		printf("\n");
	}
}
