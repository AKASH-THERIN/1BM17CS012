#include<iostream>
using namespace std;
void swap(int *a, int *b)
{
    int temp=*a;
    *a=*b;
    *b= temp;
}
int part(int a[], int low, int high)
{
    int pi=a[high];
    int i=low-1;
    for(int j=low;j<= high-1;j++)
    {
        if(a[j]<pi)
        {    
            i++;
            swap(&a[j],&a[i]);
        }
    }
    swap(&a[i+1],&a[high]);
    return (i+1);
}
void quicksort(int a[],int low,int high)
{
    if(low<high)
    {
     int p=part(a,low,high);
     quicksort(a,p-1,low);
     quicksort(a,p+1,high);
     
    }
}

void disp(int a[],int low,int high)
{
  for(int i=low;i<high;i++){cout<<" "<<a[i];}
}
int main()
{
    int n,a[100];
    cout<<"enetr the number of elements";
    cin>>n;
    cout<<"\n enter the elements";
    for(int i=0;i<n;i++){cin>>a[i];}
    cout<<"\n before sort";
    disp(a,0,n);
    quicksort(a,0,n-1);
    cout<<"\n after sort";
    disp(a,0,n);
    return 0;
}