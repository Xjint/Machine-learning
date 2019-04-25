#include<iostream>
#include<list>
#include<array>
#include<vector>
using namespace std;

float getdis(array<float, 2> a, array<float, 2> b){
	return sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]));
}

void disp(list<list<array<float, 2>>> a) {
	int i = 1;
	for (auto l : a) {
		cout << "¾ÛÀà:" << i << endl;
		for (auto v : l) {
			cout << v[0] << "," << v[1] << endl;
		}
		++i;
	}	
}

void julei(list<array<float, 2>> center, list<array<float, 2>> content) {
	int len = center.size();
	list<list<array<float, 2>>> lei;
	for (auto cen : center) {
		list<array<float, 2>> tmp = {};
		lei.push_back(tmp);
	}
	list<list<array<float, 2>>>::iterator it;
	for (auto con : content) {
		float res = 1000;
		int index = 0;
		int num = 0;
		int count = 0;
		for (auto cen : center) {
			float tmp = getdis(cen, con);
			if (tmp < res) {
				res = tmp;
				index = num;
			}
			num++;
		}
		for (it = lei.begin(); it != lei.end(); ++it,++count) {
			if (count == index) {
				
				(*it).push_back(con);
				break;
			}
		}	
	}
	disp(lei);
}

void startjulei(list<array<float, 2>>& center, list<array<float, 2>> content, float threshold) {
	while (1) {
		float result = 0;
		array<float, 2> replace;
		for (auto con : content) {
			float tmp = 0;
			float jiaoxiao = 100;
			for (auto cen : center) {
				tmp = getdis(cen, con);
				jiaoxiao = min(jiaoxiao, tmp);
			}
			if (jiaoxiao > result) {
				result = jiaoxiao;
				replace = con;
			}
		}
		if (result < threshold)
			break;
		else
			center.push_back(replace);
	}
}

int main() {
	list<array<float, 2>> content = { {0,0 },{3,8},{2,2},{1,1},{5,3},{4,8},{6,3},{5,4},{6,4},{7,5} };
	list<array<float, 2>> center = { {0,0} };
	list<array<float, 2>>::iterator it;
	list<array<float, 2>>::iterator it_center;
	float res = 0.0;
	float theta = 0.5;
	float threshold;
	array<float, 2> replace;
	for (auto con : content) {
		float tmp = getdis({ 0,0 }, con);
		if (tmp > res) {
			res = tmp;
			replace = con;
		}
	}
	center.push_back(replace);
	threshold = theta * res;

	startjulei(center, content, threshold);
	julei(center, content);
	return 1;
}