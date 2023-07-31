int lengthOfLongestSubstring(char * s){
    int ht[127];
    //int *ht=(int*)malloc(128*sizeof(int)),i;
    for(int i=0;i<127;i++){
        ht[i]=-1; //都先初始化成-1
    }
    int max=0,strsize=strlen(s),substring_start=0;
    for(int i=0;i<strsize;i++){
        if((ht[s[i]])>=substring_start){ //在子字串裡了
            substring_start=ht[s[i]]+1;
            ht[s[i]]=i;
        }
        else{  //不在子字串裡
            ht[s[i]]=i;
            if(i-substring_start+1>max)max=i-substring_start+1;
        }
    }
    return max;
}
