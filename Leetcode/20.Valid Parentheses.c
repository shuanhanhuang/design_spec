bool isValid(char * s){
    char stack[5000];
    int top = 0;
    for(int i = 0;i<strlen(s);i++){
        if(s[i] == '(' || s[i] == '[' || s[i] == '{' ){
            stack[top] = s[i];
            top++;
        }
        else if(s[i] == ')'){
            if(top==0)
                return false;
            else if(stack[top-1] == '('){
                top--;
            }
            else{
                return false;
            }
        }
        else if(s[i] == ']'){
            if(top==0)
                return false;
            else if(stack[top-1] == '['){
                top--;
            }
            else{
                return false;
            }
        }
        else if(s[i] == '}'){
            if(top == 0)
                return false;
            else if(stack[top-1] == '{'){
                top--;
            }
            else{
                return false;
            }
        }
        else{
            return false;
        }
    }
    
    if(top != 0)
        return false;
    
    return true;
    
    
}
