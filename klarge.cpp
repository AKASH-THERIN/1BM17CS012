//#include<bits/stdc++.h>
#include<iostream>
using namespace std;
void ksmall(int a[], int n,int k){
    int min,temp;
    for(int i=0;i<k;i++){
        for(int j=0;j<n-1-i;j++){
           if(a[j]>a[j+1]){
                  temp=a[j];
               a[j]=a[j+1];
               a[j+1]=temp;
           }
        }
      cout<<"\n  "<<a[n-i-1];       
    }
    cout<<"\n\n ";
    //for(int i=0;i<n;i++){cout<<a[i]<<"   ";}
    
}
int main(){
    int a[100],n,k;
    cout<<"enter number of elemnts in array";
    cin>>n;
    cout<<"enter elemnts in array";
    for(int i=0;i<n;i++){cin>>a[i];}
    cout<<"enter kth value ...";
    cin>>k;
    ksmall(a,n,k);
    return 0;
}