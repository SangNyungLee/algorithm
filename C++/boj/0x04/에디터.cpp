#include <bits/stdc++.h>
using namespace std;

const int MX = 600001;
int pre[MX], nxt[MX];
char dat[MX];
int unused = 1;
int len = 0;
void insert(int addr, char num){
	dat[unused] = num;
	pre[unused] = addr;
	nxt[unused] = nxt[addr];
	if (nxt[addr] != -1) pre[nxt[addr]] = unused;
	nxt[addr] = unused;
	unused++;
}

void erase(int addr){
	nxt[pre[addr]] = nxt[addr];
	if(nxt[addr] != -1) pre[nxt[addr]] = pre[addr];
}

void traverse(){
	int cur = nxt[0];
	while (cur != -1){
		cout << dat[cur];
		cur = nxt[cur];
	}
	cout << '\n';
}
int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);
	fill(pre, pre + MX, -1);
	fill(nxt, nxt + MX, -1);
	string s1;
	cin >> s1;
	int point = 0;
	for(char c : s1){
		insert(point, c);
		point = unused - 1; // 마지막 삽입 위치로 이동
	}
	int M;
	cin >> M;
	while(M--){
		char s2;
		cin >> s2;
		if (s2 == 'P'){
			char s3;
			cin >> s3;
			insert(point, s3);
			point = unused - 1;
		}
		else if (s2 == 'L'){
			if (pre[point] != -1)
				point = pre[point];
		}
		else if (s2 == 'D'){
			if (nxt[point] != -1)
				point = nxt[point];
		}
		else if (s2 == 'B'){
			if (point != 0){
				int to_delete = point;
				point = pre[point];
				erase(to_delete);
			}
		}
	}
	traverse();
}

/*
#include <bits/stdc++.h>

using namespace std;

int main(void){
	ios::sync_with_stdio(0);
	cin.tie(0);

	string str;
	std::list<char> lst;
	cin >> str;
	for(char c : str) lst.push_back(c);
	auto pos = lst.end();
	int N = 0;
	cin >> N;

	while(N--){
		char cc;
		cin >> cc;
		if (cc == 'P'){
			char c;
			cin >> c;
			lst.insert(pos, c);
		}
		else if (pos != lst.begin() && cc == 'L') pos--;
		else if (pos != lst.end() && cc == 'D') pos++;
		else if (pos != lst.begin() && cc == 'B'){
			pos--;
			pos = lst.erase(pos);
		}

	}
	for(char c : lst) cout << c;
}
*/