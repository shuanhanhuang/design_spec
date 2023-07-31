int cal1(char c){
    switch(c){
        case 'I':return 1;
        case 'V':return 5;
        case 'X':return 10;
        case 'L':return 50;
        case 'C':return 100;
        case 'D':return 500;
        case 'M':return 1000;
    }    
    return 0;
}

int romanToInt(char * s){
    int i,length=strlen(s),temp=0,val=0;
    for(i=0;i<length;i++){
        if(i==length-1){
            val+=cal1(s[i]);
            break;
        }
        if((temp=cal1(s[i+1])-cal1(s[i]))>0){
            val+=temp;
            i++;
            temp=0;
            continue;
        }        
        val+=cal1(s[i]);
    }
    return val;
}
