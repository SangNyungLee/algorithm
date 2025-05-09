#include <bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int a1[26] = {};
	string s1, s2;
	int res = 0;
	cin >> s1 >> s2;
	for(char c : s1) a1[c - 'a']++;
	for(char c : s2) a1[c - 'a']--;
	for(int i = 0 ; i < 26 ; i++){
		res += abs(a1[i]);
	}
	cout << res;
}