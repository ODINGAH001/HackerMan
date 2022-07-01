 #include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
            long long int n,k,carry,l,x,j,ans[1000];
            carry = 0;
                        cin>>n;
                        if(n==1 || n==0)
                        {
                                    cout<<"1";
                                    return 0;
                        }
                        x=n*(n-1);
                        l=0;
                        while(x>0)
                        {
                                    ans[l] = x%10;
                                    x = x/10;
                                    l++;
                        }
                        for(j=n-2;j>0;j--)
                        {
                                    carry = 0;
                                    for(k=l-1;k>=0;k--)
                                    {
                                                ans[k] = ans[k]*j;
                                    }
                                    for(k=0;k<l;k++)
                                    {
                                                ans[k] = ans[k] + carry;
                                                carry = ans[k]/10;
                                                ans[k] = ans[k]%10;
                                    }
                                    if(carry != 0)
                                    {
                                                while(carry>0)
                                                {
                                                            l++;
                                                            ans[l-1] = carry%10;
                                                            carry = carry/10;
                                                }
                                               
                                    }
                        }
                        for(k=l-1;k>=0;k--)
                                    {
                                                cout<<ans[k];
                                    }
                                   
return 0;
}

