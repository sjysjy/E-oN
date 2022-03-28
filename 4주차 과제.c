#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main()
{
	int bubble[6];
	int i, tmp;

	for (i = 0; i < 6; i++)
	{
		scanf("%d", &bubble[i]);
	}

	for (i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5-i; j++)
		{
			if (bubble[j] > bubble[j + 1])
			{
				tmp = bubble[j];
				bubble[j] = bubble[j + 1];
				bubble[j + 1] = tmp;
			}
		}
	}
	printf("[%d, %d, %d, %d, %d, %d]", bubble[0], bubble[1], bubble[2], bubble[3], bubble[4], bubble[5]);
	return 0;
}
