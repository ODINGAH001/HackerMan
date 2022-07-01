#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int a[1000],n,i,min=9999,count;
	cin>>n;
	for(i=0;i<n;i++)
		cin>>a[i];
	while(1)
	{
		min=9999;
		for(i=0;i<n;i++)
		{
			if(a[i]<min & a[i]>0)
			min=a[i];
		}	
		count=0;
		for(i=0;i<n;i++)
		{
			if(a[i]>0)
			{
				a[i]=a[i]-min;
				count++;
				//cout<<a[i]<<"  ";
			}
		}
	if(count==0)
	break;
	else
	cout<<count<<endl;
}
    return 0;
}
