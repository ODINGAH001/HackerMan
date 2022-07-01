#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<ctime>
using namespace std;


// A date has day 'd', month 'm' and year 'y'
struct Date
{
	int d, m, y;
};

// To store number of days in all months from January to Dec.
const int monthDays[12] = {31, 28, 31, 30, 31, 30,
						31, 31, 30, 31, 30, 31};

// This function counts number of leap years before the
// given date
int countLeapYears(Date d)
{
	int years = d.y;

	// Check if the current year needs to be considered
	// for the count of leap years or not
	if (d.m <= 2)
		years--;

	// An year is a leap year if it is a multiple of 4,
	// multiple of 400 and not a multiple of 100.
	return years / 4 - years / 100 + years / 400;
}

// This function returns number of days between two given
// dates
int getDifference(Date dt1, Date dt2)
{
	// COUNT TOTAL NUMBER OF DAYS BEFORE FIRST DATE 'dt1'

	// initialize count using years and day
	long int n1 = dt1.y*365 + dt1.d;

	// Add days for months in given date
	for (int i=0; i<dt1.m - 1; i++)
		n1 += monthDays[i];

	// Since every leap year is of 366 days,
	// Add a day for every leap year
	n1 += countLeapYears(dt1);


	// SIMILARLY, COUNT TOTAL NUMBER OF DAYS BEFORE 'dt2'

	long int n2 = dt2.y*365 + dt2.d;
	for (int i=0; i<dt2.m - 1; i++)
		n2 += monthDays[i];
	n2 += countLeapYears(dt2);

	// return difference between two counts
	return (n2 - n1);
}

// Driver program
int main()
{
	Date dt_ac;//={10, 6, 2016};//expected return
	Date dt_ex;//={9, 6, 2015};//actual return
	cin>>dt_ac.d>>dt_ac.m>>dt_ac.y;
	cin>>dt_ex.d>>dt_ex.m>>dt_ex.y;    
	Date dt1=dt_ex;
	Date dt2=dt_ac;
	int diff, fine;
//	cin>>dt1.d>>dt1.m>>dt1.y;
//	cin>>dt2.d>>dt2.m>>dt2.y;
	//If the book is returned on or before the expected return date, no fine will be charged, in other words fine is 0.
	diff=getDifference(dt1,dt2);
	//If the book is returned in the same calendar month as the expected return date, Fine = 15 Hackos × Number of late days 
	if(dt1.m==dt2.m && diff>0 && dt1.y==dt2.y)
		fine=15*diff;
	//If the book is not returned in the same calendar month but in the same calendar year as the expected return date, Fine = 500 Hackos × Number of late months 
	if(dt2.m>dt1.m && diff>0 && dt1.y==dt2.y)
		fine=500*(dt2.m-dt1.m);
	//If the book is not returned in the same calendar year, the fine is fixed at 10000 Hackos
	if(diff>0 && dt2.y>dt1.y)
		fine=10000;
	cout<<fine;
	return 0;
}


