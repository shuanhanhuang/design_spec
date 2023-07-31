int myAtoi(char * s){
    if(strlen(s) == 0){
        return 0;
    }
    int index = 0;
    int y = 0;
    int some = 0;
    char *word = (char*)malloc((strlen(s)+1)*sizeof(char));
    for(int i=0;i<strlen(s);i++){
        
        if((int)s[i] >=48 && (int)s[i]<=57){
            word[index] = s[i];
            index = index + 1;
        }
        
        else if((int)s[i] == 32 && index == 0 && some ==0){
            index = index + 0;
        }
        else if((int)s[i] == 45 && some == 0 && index ==0){
            some = -1;
        }
        else if((int)s[i] == 43 && some == 0 && index ==0){
            some = 1;
        }
        else{
            if(index == 0){
                return 0;
            }
            else{
                i=strlen(s);
            }
        }
    }
    if(some == 0){
        some = 1;
    }
    word[index] = '\0';
    int j = 0 ;
    int first = 0;
    while(j<index){
        
        first = some*((int)word[j]-48);
        if(y > INT_MAX/10){
            return INT_MAX;
        }
        else if(y< INT_MIN/10){
            return INT_MIN;
        }
        else if(y == INT_MAX/10 || y == INT_MIN/10){
            if(first >7){
                return INT_MAX;
            }
            else if(first<-8){
                return INT_MIN;
            }
        }
        
        y = y*10 + first ;
        
        j = j + 1;
    }


    return y;
}
