#include <bits/stdc++.h>
using namespace std;


int main(){
    vector <int> list_of_numbers = {1,3,5,7,9,2,1,3};
    
    int sizeof_list = list_of_numbers.size();
    
    unordered_set <int> container; //assigning a hashset
    
    
    for(int i=0; i< sizeof_list; i++){
        if(container.find(list_of_numbers[i])!= container.end()){ //checking for the number in hashset
            cout << "duplicate found " << list_of_numbers[i];
        }
        else{
            container.insert(list_of_numbers[i]);
        }
    }
    
    
    
}
