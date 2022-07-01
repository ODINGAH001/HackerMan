#include<iostream>
using namespace std;
int main()
{	
int k,i=0,n,j;
char s[100];
cin>>n;
cin>>s;
cin>>k;
for(i=0;i<n;i++)
{
	if(s[i]>=65 && s[i]<=90)
	{
		for(j=1;j<=k;j++)
			if((s[i]+1)>90)
			 s[i]='A';
			else
			s[i]=s[i]+1;
		 
	}
	if(s[i]>=97 && s[i]<=122)
	{		
			for(j=1;j<=k;j++)
			if((s[i]+1)>122)
			 s[i]='a';
			else
			s[i]=s[i]+1;
	}	
}
cout<<s;
return 0;
}
