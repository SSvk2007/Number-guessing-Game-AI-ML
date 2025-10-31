#include <stdio.h>
#include <stdlib.h>
int main() {
    system("cls");
    int a, b, c;
    printf("Enter breadth of rectangle:\n"); 
        scanf("%d", &a);
    printf("Enter length of rectangle:\n");
    scanf("%d", &b);

    c = a * b;
    printf("Area of rectangle: %d\n", c);

    return 0
} 
