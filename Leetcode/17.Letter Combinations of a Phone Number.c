#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char letter[10][5]={{}, {}, {"abc"}, {"def"}, {"ghi"}, {"jkl"}, {"mno"}, {"pqrs"}, {"tuv"}, {"wxyz"}};
char** re;
char* dist;
int index = 0;
void rsum(int size, char* tempstr){
	int i, j;
	printf("size1: %d\n",size);
	if(dist[size] == '\0'){
//		re[index] = '\0';
		re[index] = (char*)malloc(sizeof(char)*3);
		strcpy(re[index], tempstr);
		printf("re[index]: %s,index: %d \n",re[index],index);
		index++;
	}
	else{
		for(i=0; i<strlen(letter[dist[size]-'0']); i++){
			printf("size2: %d\n",size);
			tempstr[size] = letter[dist[size]-'0'][i];
			printf("tempstr[size]: %s\n",tempstr);
//			size = size+1;
			rsum(size+1, tempstr);
		}	
	}

} 
char ** letterCombinations(char * digits, int* returnSize){
	dist = digits;
//	printf("%c",dist[0]);
	if(strlen(digits)!= 0){
		*returnSize = 1;	
		int i,j;
		for(i=0; i<strlen(digits); i++){
			*returnSize = *returnSize * strlen(letter[digits[i]-'0']);
		}
		printf("returnSize: %d\n",*returnSize);
	}
	else{
		*returnSize = 0;
	}
	
	re = (char**)malloc(sizeof(char*)*(*returnSize));
	char tempstr[5] = {0};
	if(*returnSize > 0){
		rsum(0 ,tempstr);
	}
	
	return re;

}
int main(void){
	char* digits = "23";	
	int i,j;
	int returnSize;
	
	char** answer =  letterCombinations(digits,&returnSize);
	for(i=0; i<returnSize; i++){
		printf("%s  ",answer[i]);	
	}
	
}

