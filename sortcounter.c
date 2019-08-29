#include<stdio.h>
int a[50]; 
int b[50];
int counter=0,co=0;
void ssort(int a[],int l,int h){
    int temp;
    for(int i=0;i<h;i++)
    {   
        int min=i; int temp;
        for(int j=i+1;j<h;j++)
        {
            counter++;
            if (a[j]<a[i])
            {
            
                min=j;
            }

        }
        temp=a[i];
        a[i]=a[min];
        a[min]=temp;
    }
}

void bsort(int a[],int l,int h){
    int temp;
    for(int i=0;i<h;i++)
    {   
        for(int j=0;j<h-i-1;j++)
        {
          
            if (a[j]>a[j+1])
            {
                  co++;
                temp=a[j];
               a[j]=a[j+1];
               a[j+1]=temp;
            }

        }
       
    }
}
int main()
{
 int n,i;
 printf("No of elements");
 scanf("%d",&n);
 printf("Enter %d elements:\n",n);
 for(i=0;i<n;i++)
  {scanf("%d",&a[i]); b[i]=a[i];}
 ssort(a,0,n);
 ssort(b,0,n);
 printf("the value of slection sort counter is  %d  \n",co);
 printf("The resultant array of selection sort:\n");
 for(i=0;i<n;i++)
   printf("%d\t",a[i]);


   printf("\nthe value of sbubble sort counter is  %d  \n",co);
 printf("The resultant array of bubble sort:\n");
 for(i=0;i<n;i++)
   printf("%d\t",b[i]);
 return 0;
}