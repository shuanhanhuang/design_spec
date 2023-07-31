int maxArea(int* height, int heightSize){
    int left = 0 ,right = heightSize-1;
    int area = 0;
    while(left<right){
        printf("%d,%d\n",left,right);
        if(height[left]<=height[right] ){
            if((right-left) * height[left]>area){
                area = (right-left) * height[left];
            }
            left = left + 1;
        }
        else if(height[left]>height[right] ){
            if((right-left) * height[right]>area){
                area = (right-left) * height[right];
            }
            right = right - 1;
        }

    }
    // for(int i=0;i<heightSize;i++){
    //     width = 0;
    //     for(int j=0;j<heightSize;j++){
    //         if(i != j){
    //             if(height[i]<=height[j] && abs(j-i)>width){
    //                 // printf("width:%d\n",width);
    //                 width = abs(j-i);
    //             }
    //         }
    //     }
    //     area = width * height[i];
    //     if(area>max){
    //         max = area;
    //     }
    //     // printf("i:%d,area:%d\n",i,area);
    // }

    // return max;
    
    return area;
}
