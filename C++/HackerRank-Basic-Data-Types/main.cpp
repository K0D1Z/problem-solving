//
// Created by konrad on 3/4/26.
//
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int var1;
    long var2;
    char var3;
    float var4;
    double var5;

    scanf("%d %ld %c %f %lf", &var1, &var2, &var3, &var4, &var5);

    printf("%d\n%ld\n%c\n%f\n%lf", var1, var2, var3, var4, var5);

    return 0;
}