void push(char a,char * stack,int* top){
    *top = *top+1;
    stack[*top] = a;
    return ;
}
char pop(char* stack,int* top){
    char temp = stack[*top];
    *top = *top-1;
    return temp;
}
char * longestPalindrome(char * s){
    int first =0, last =0;
    int length = strlen(s);
    char stack[length];
    int top = -1, k=0, max = 0, ans = 0;
    int count = 0;
    if(length == 1){
        return s;
    }
    else{
        for(int i=0;i<length-1;i++){
            top = -1;
            ans = 0;
            for(int j=length-1;j>=i+1;j--){
                ans = 0;
                if(j-i+1>max && s[i] == s[j]){
                    count = j-i+1;
            
                    for(k=i;k<i+count/2 ;k++){
                        push(s[k],stack,&top);
                    }
                    if(count % 2 != 0){
                        k=k+1;
                        ans = ans + 1;
                    }
                    for(int new=k ;new<=j ;new++){
                        char temp = pop(stack,&top);
                        if(temp != s[new]){
                            ans = 0;
                            top = -1;
                            break;
                        }
                        else{
                            ans = ans+2;
                        }
                    }
                    if(ans > max){
                        first = i;
                        last = j;
                        max = count;
                        break;
                    }
                    
                }
                
            }
            
        }
        if(max == 0){
            max = 1;
        }
        int index=0;
        char *word = (char*)malloc((max+1)*sizeof(char));
        while(first<=last){
            word[index] = s[first];
            first = first+1;
            index = index+1;
        }
        word[max] = '\0';
        
        return word;
    }
    
    
    
}
