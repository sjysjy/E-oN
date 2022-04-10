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
	int n, sol=0;		//n: ������ ���� ��, sol: ���ڸ� 1���� Ȥ�� 2�������� ������ ����� ��
	
	printf("������ ���� ��: ");
	scanf("%d", &n);

	for (int i = 0; i <= n / 2; i++)		
	{
		sol += factorial(i + (n - 2 * i)) / (factorial(i) * factorial(n - 2 * i));		//���� ���� �ִ� ������ �̿��� ����
	}
	
	printf("%d\n", sol);
	return 0;
}