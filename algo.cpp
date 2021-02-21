#include<bits/stdc++.h>
using namespace std;
vector<string> names;
int n;
int numSlots = 48;//TODO change this later
vector<vector<int>> schedule;
int main(){
	cin>>n;
	names.resize(n);
	schedule.resize(n);
	for(int i = 0;i<n;i++){
		schedule[i].resize(numSlots);
		cin>>names[i];
		for(int j = 0;j<numSlots;j++) cin>>schedule[i][j];
	}
	cout<<n<<endl;
	for(int i = 0;i<n;i++){
		cout<<names[i]<<" ";
		for (int j : schedule[i]) cout<<j<<" ";
		cout<<endl;
	}
	int maxAttendance = 0;
	int timeSlot = 0;
	for(int j = 0;j<numSlots;j++){
		int sum = 0;
		for(int i = 0;i<n;i++) sum+=schedule[i][j];
		if(sum>maxAttendance){
			maxAttendance = sum;
			cout<<"max at : " <<j<<endl;
			timeSlot = j;
		}
	}
	cout<<"hold meeting at: "<<timeSlot<<endl;
	cout<<"attendance: "<<endl;
	for(int i = 0;i<n;i++){
		if(schedule[i][timeSlot]!=0) cout<<names[i]<<endl;
	}
	for(int i = 0;i<n;i++) schedule[i][timeSlot] = 0;
}