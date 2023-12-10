#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int t[26], f[26] = { 0, }, degree[26];
	vector<int> adj[26];

	string str;
	while(getline(cin, str)) {
		string tmp = "";
		vector<string> v;
		for (auto& i : str) {
			if (i != ' ')
				tmp.push_back(i);
			else
				v.push_back(tmp), tmp = "";
		}
		v.push_back(tmp);

		char task = v[0][0];
		int day = stoi(v[1]);
		string tasks = (v.size() == 2 ? "" : v[2]);

		for (auto& j : tasks)
			adj[j - 'A'].push_back(task - 'A');
		degree[task - 'A'] = tasks.size();
		t[task - 'A'] = day;
	}

	queue<int> q;

	for (int i = 0; i < 26; i++) {
		if (t[i] && !degree[i]) {
			q.push(i);
			f[i] = t[i];
		}
	}

	while (!q.empty()) {
		int now = q.front();
		q.pop();

		for (auto& next : adj[now]) {
			f[next] = max(f[next], f[now] + t[next]);

			if (!--degree[next])
				q.push(next);
		}
	}

	int ans = 0;
	for (int i = 0; i < 26; i++)
		ans = max(ans, f[i]);

	cout << ans << '\n';
	return 0;
}