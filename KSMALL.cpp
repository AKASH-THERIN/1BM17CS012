//#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int ksmall(int a[], int n,int k){
    int min,temp;
    for(int i=0;i<k;i++){
        min=i;
        for(int j=i+1;j<n;j++){
           if(a[min]>a[j]){
                min=j;
           }
        }
               temp=a[i];
               a[i]=a[min];
               a[min]=temp;
    }
    
    return a[k-1];
}
int main(){
    int a[100],n,k;
    cout<<"enter number of elemnts in array";
    cin>>n;
    cout<<"enter elemnts in array";
    for(int i=0;i<n;i++){cin>>a[i];}
    cout<<"enter kth value ...";
    cin>>k;
    cout<<"here is your value..."<<ksmall(a,n,k);
    return 0;
}