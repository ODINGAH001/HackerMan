#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <iomanip>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int h,m,s;
    char c;
    std::stringstream ss;
    scanf("%d:%d:%d%c",&h,&m,&s,&c);
    if(c=='P')
    {
    	if(h==12)
    		ss << "12";
    	else
	        ss << (h+12);
	        ss << ":";
	        ss << std::setfill('0') << std::setw(2) << m;
	        ss << ":";
	        ss << std::setfill('0') << std::setw(2) << s;
    }
    if(c=='A')
    {
    	//12:40:22AM		//op -00:40:22
    	if(h==12)
    		ss << "00";
    	else
    		ss<<std::setfill('0') << std::setw(2) << h;
    	ss << ":";
	    ss << std::setfill('0') << std::setw(2) << m;
	    ss << ":";
	    ss << std::setfill('0') << std::setw(2) << s;
	}
    //ss << std::setfill('0') << std::setw(2) << 5; // Prints 05
    std::cout << ss.str();
    return 0;
}
