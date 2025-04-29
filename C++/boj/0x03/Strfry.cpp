#include <bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N;
	cin >> N;
	// for(int i = 0 ; i < N ; i++){
	// 	int arr[26]= {};
	// 	int arr2[26] = {};
	// 	string a, b;
	// 	cin >> a >> b;
	// 	for(char c : a) arr[c - 'a']++;
	// 	for(char c : b) arr2[c - 'a']++;
	// 	bool flag = true;
	// 	for(int i = 0 ; i < 26 ; i++){
	// 		if (arr[i] != arr2[i]) flag = false;
	// 	}
	// 	if (!flag) cout << "Impossible" << '\n';
	// 	else cout << "Possible" << '\n';
	// }
	while (N--){
		int a[26] = {};
		string s1, s2;
		cin >> s1 >> s2;
		for(char c : s1) a[c - 'a']++;
		for(char c : s2) a[c - 'a']--;
		bool isPossible = true;
		for(int i : a){
			if (i != 0) isPossible = false;
		}
		if(isPossible) cout << "Possible\n";
		else cout << "Impossible\n";
	}
}