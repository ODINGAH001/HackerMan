#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t,k,n,ans[10],a[1000],count,i,j;
    cout<<"Enter the number test cases :";
    cin>>t;
    for(i=0;i<t;i++)
    {
    	count=0;
    	cout<<"Enter the number of students :-";
    	cin>>n;
    	cout<<"Enter the threshold :-";
    	cin>>k;
    	cout<<"Enter the arrival time of each student";
    	for(j=0;j<n;j++)
    	{
    		cin>>a[j];
			if(a[j]<=0)
			count++;
		}
		if(count<k)
			ans[i]=1;//no class
		else
			ans[i]=0;//class
	}
	for(i=0;i<t;i++)
	{
		if(ans[i]==1)
		cout<<"YES";
		else
		cout<<"NO";
	}	
    return 0;
}
