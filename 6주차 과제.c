#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

int factorial(int num)
{
	if (num == 0 || num == 1)
		return 1;

	return (num * factorial(num - 1));
}

int main()
{
	int n, sol=0;		//n: 피자의 조각 수, sol: 피자를 1조각 혹은 2조각으로 나누는 방법의 수
	
	printf("피자의 조각 수: ");
	scanf("%d", &n);

	for (int i = 0; i <= n / 2; i++)		
	{
		sol += factorial(i + (n - 2 * i)) / (factorial(i) * factorial(n - 2 * i));		//같은 것이 있는 순열을 이용한 공식
	}
	
	printf("%d\n", sol);
	return 0;
}