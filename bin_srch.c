#include<stdio.h>
#include<stdlib.h>
void main()
{
int beg,mid,end,n,flag=0,arr[100],ele,temp,i,j,k;
printf("Enter the number of elements in the array:");
scanf("%d",&n);
printf("The elements are:");
	for(i=0;i<n;i++)
	{	
	arr[i]=rand()%100;
	}
	for(j=0;j<n-1;j++)
	{
		for(k=0;k<n-j-1;k++)
		{
			if(arr[k]>arr[k+1])
			{
			temp=arr[k];
			arr[k]=arr[k+1];
			arr[k+1]=temp;
			}
		}
	}
for(i=0;i<n;i++)
printf("%d\t",arr[i]);
printf("\n");
printf("Enter the search element:");
scanf("%d",&ele);
beg=0,end=n-1;
	while(beg<=end)
	{
	mid=(beg+end)/2;
	if(arr[mid]==ele)
	{
	flag=1;
	break;
	}
	else if(arr[mid]<ele)
	{
	beg=mid+1;
	}
	else
	end=mid-1;
	}
if(flag==1)
{
printf("The element is found at position %d",mid+1);
printf("\n");
}
else
printf("Element not found in the given array!!");
printf("\n");
}

