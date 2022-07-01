#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int h=1,n=4,i,t,ans[10];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n;
		h=1;
		while(n>0)
		{
			h=h*2;
			n--;
			if(n!=0)
			h=h+1;
			n--;
		}
		ans[i]=h;
	}
for(i=0;i<t;i++)
cout<<ans[i]<<endl;
    return 0;
}
