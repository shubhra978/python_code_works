#include <bits/stdc++.h>
using namespace std;



int manual_binary_search(vector <int> &nums, int target){
    int left = 0;
    int right = nums.size()-1;
    
    while(left < right){
        int mid = left+(right-left)/2; //dividing both sides to find the mid value
        if (nums[mid]== target){ //checking if value found
            return mid; 
        }
        else if(nums[mid]< target){
            mid ++; //moving mid towards right
        }
        else{
            mid --; //moving mid towards left
        }
    }
    return -1;
}





int main() {
	// your code goes here
    vector <int> nums ={1,5,6,8,12,23};
    int target = 12;
    int result = manual_binary_search(nums,target);
    if(result != -1){
       cout <<"found at index"<< result; 
    }
    
    else{
        cout << "not found";
    }
}
