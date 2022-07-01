#include<iostream>
using namespace std;
int main()
{
	int n[15],div=0,count=0,new_n,t,i;
	cin>>t;
	for(i=0;i<t;i++)
	cin>>n[i];
	for(i=0;i<t;i++)
	{	
		new_n=n[i];
		count=0;
		while(new_n>0)
		{
				div=new_n%10;
				if(div!=0)
				if(n[i]%div==0)
					count++;
				new_n=new_n/10;			
		}
		cout<<count<<endl;
	}
	return 0;
}
