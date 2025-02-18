#include <stdio.h>

int main(){
    int num1,num2;
    int op;
    printf("Enter the first number:");
    scanf("%d",&num1);
    printf("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n");
    printf("Enter your choice:");
    scanf("%d",&op);
    printf("Enter the second number:");
    scanf("%d",&num2);

    if (op==1){
        printf("%d",num1+num2);
    }
    else if (op==2){
        printf("%d",num1-num2);
    }
    else if (op==3){
        printf("%d",num1*num2);
    }
    else if (op==4){
        printf("%d",num1/num2);
    }
    else{
        printf("Invalid input");
    }



    return 0;
}