#include<stdio.h>
#include<stdlib.h>
void main()
{
  int arr[100],n,max;
  printf("Enter the number of elements in the array:");
  scanf("%d",&n);
  printf("The array elements are:");
  for(int i=0;i<n;i++)
  {
  arr[i]=rand()%50;
  printf("%d\t",arr[i]);
  }
  max=arr[0];
  for(int i=0;i<n;i++)
  {
  if(arr[i]>max)
  max=arr[i];
  }
  printf("The largest element in the array is: %d",max);
}
