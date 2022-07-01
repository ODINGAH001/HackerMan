#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
int a,b,count,j,i,ans[100],t;
cin>>t;
while(t--)
{
	cin>>a>>b;
	count=0;
	for(i=a;i<=b;i++)
	{
		if((int)sqrt(i)==sqrt(i))
		count++;
	}
	cout<<count<<endl;
}
    return 0;
}
