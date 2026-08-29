#include <bits/stdc++.h>
using namespace std;

int main() {
	int first_list[]={1,2,4,5,1,2,6};
	int second_list[]= {2,1,1,3,5,4};
	int arr_size= sizeof(first_list)/sizeof(first_list[0]);
	int arr_sizeb=sizeof(second_list)/sizeof(second_list[0]);
	
	unordered_set<int> container; //hash set initialisation
	
	for(int i =0; i < arr_size; i++){
	    if(container.find(first_list[i])!=container.end()){
	    }
	    else{
	        container.insert(first_list[i]);
	    }
	}
	for(int j=0; j<arr_sizeb;j++){
	    if(container.find(second_list[j])!=container.end()){
	        cout<< second_list[j] << endl;
	    }
	    
	}
	
}
