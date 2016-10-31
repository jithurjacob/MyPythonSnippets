#include<stdio.h>
int main(){
	long  i,n,arr[2500];
	scanf("%d",&n);
	for(i=0; i < n;i++)
		scanf("%d",arr[i]);
	for(i=0; i < n;i++)
		printf("%d\n", arr[i]);
	return 0;
}