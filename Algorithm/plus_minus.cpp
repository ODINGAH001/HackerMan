#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,a[100],pos=0,min=0,zero=0;
    cin>>n;
    for(int i=0;i<n;i++)
     {
        cin>>a[i];
        if(a[i]>0)
            pos++;
        if(a[i]<0)
            min++;
        if(a[i]==0)
            zero++;
     }
    cout<<pos/(float)n<<endl;
    cout<<min/(float)n<<endl;
    cout<<zero/(float)n;
    return 0;
}
