/*
author : Suraj S. Pawar
ps : april2018/chefwork
site : codechef.com
*/
#include <iostream>
#include <limits>
using namespace std;
int main() {
	long t, i;
	cin >> t;

	long coins[t];
	long types[t];

	for (i = 0; i < t; i++)
		cin >> coins[i];

	for (i = 0; i < t; i++)
		cin >> types[i];

	long auth = 0, translator = 0, legend = 0;
	long cost = 0, temp = 0, tone = 0, ttwo = 0, duo = 0;
	long trio = numeric_limits<long>::max();
	long one = numeric_limits<long>::max();
	long two = numeric_limits<long>::max();

	// cout << trio;

	for (i = 0; i < t; i++) {
		if (types[i] == 3) {
			legend++;
			temp = coins[i];
			if (temp <= trio)
				trio = temp;
		} else if (types[i] == 1) {
			auth++;
			tone = coins[i];
			if (tone <= one)
				one = tone;
		} else if (types[i] == 2) {
			translator++;
			ttwo = coins[i];
			if (ttwo <= two)
				two = ttwo;
		}
	}
	if (auth != 0 && translator != 0) {
		cost = one + two;
		if (cost < trio)
			cout << cost << endl;
		else if (legend != 0)
			cout << trio << endl;
	} else if (legend != 0)
		cout << trio << endl;

	return 0;
}