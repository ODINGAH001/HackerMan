#include<iostream>
using namespace std;
int main()
{
int n,c,m,chocolate=0,wrapper=0,temp=0,t;
cin>>t;
while(t--)
	{
		cin>>n>>c>>m;
		chocolate=n/c;
		wrapper=chocolate;
		while(1)
		{
			temp=wrapper/m;//choclate got by using wrapper
			if(temp==0)
				break;
			chocolate=chocolate+temp;
			wrapper=wrapper-(temp*m);
			wrapper=wrapper+temp;
		}		
		cout<<chocolate<<endl;
	}
return 0;
}
