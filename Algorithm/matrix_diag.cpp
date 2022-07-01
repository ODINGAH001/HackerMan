#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i,j,n=3,sum1=0,sum2=0,diff=0;
    //cin>>n;
    int a[3][3]={11,2,4,
				4,5,6,
				10,8,-12};
//    for(i=0;i<n;i++)
//        for(j=0;j<n;j++)
//        cin >> a[i][j];
    for(i=0;i<n;i++)        
        sum1=sum1+a[i][i];
        i=0;
for(j=(n-1);j>=0;j--)
{
	sum2=sum2+a[i][j];
	i++;
}        
    diff=sum1-sum2;
    cout<<abs(diff);
    return 0;
}
