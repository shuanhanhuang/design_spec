char * longestCommonPrefix(char ** strs, int strsSize){
    int min=strlen(strs[0]);
    int index=0;
    char* temp;
    for(int i=1;i<strsSize;i++)
    {
        if(strlen(strs[i])<min)
        {
            min=strlen(strs[i]);
            index=i;
        }
    }
    temp = strs[index];
    for(int i=0;i<min;i++)
    {
        int word=strs[index][i];
        for(int j=0;j<strsSize;j++)
        {
            
            if(strlen(strs[j])==i||strs[j][i]!=word)
            {
                temp[i]='\0';
                
            }
        }
    }
    return temp;
}

// 贺糶猭 
//char * longestCommonPrefix(char ** strs, int strsSize){
//    char* temp;         //????才??秖temp
//    int i, j;           
//    
//    if(strsSize <= 0)   //?????琌0琌???才﹃
//        return "";
//    
//    temp = strs[0];     //?材?才﹃?秖钡??temp
//    for(i=1; i<strsSize; i++){ 
//        
//        j=0;            //–Ω常??才﹃材?才ゑ?
//        
//        while(temp[j] && strs[i][j] && temp[j]==strs[i][j])     //–?才﹃蒓temp?秖?︽ゑ?
//            j ++;
//        
//        temp[j] = '\0'; //ゑ??ぇ篒祏temp
//    }
//    
//    return temp;
//
//}
