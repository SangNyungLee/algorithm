#include <bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);

	std::list<int> lst = {};

	int N, M;
	cin >> N >> M;

	for(int i = 1 ; i <= N ; i++){
		lst.push_back(i);
	}
	int position = 0;
	cout << "<";
	while(N){
		auto pos = lst.begin();
		position = (position + (M - 1)) % N;
		for(int i = 0 ; i < position ; i++) pos++;
		int removed = *pos;
		lst.erase(pos);
		if(N != 1)
			cout << removed << ", ";
		else
			cout << removed;
		N--;
	}
	cout << ">";
 }

 /*
 #include <bits/stdc++.h>
using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);

	vector<int> lst;
	int N, M;
	cin >> N >> M;
	int pos = 0;

	for(int i = 1 ; i <= N ; i++)
		lst.push_back(i);
	cout << '<';
	while(N){
		pos = (pos + (M - 1)) % N;
		int tmp = lst[pos];
		lst.erase(lst.begin() + pos);
		if (N != 1)
			cout << tmp << ", ";
		else
			cout << tmp;
		N--;
	}
	cout << '>';
 }
 */
