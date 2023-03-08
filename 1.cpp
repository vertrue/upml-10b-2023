#include <iostream>

using namespace std;

int main()
{
    // розмір масиву
    int n;
    cin >> n;
    
    // створення масиву
    int *a = new int[n];
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    
    // знаходження максимуму
    int max_el = a[0];
    for(int i = 1; i < n; i++)
    {
        if(max_el<a[i]){
            max_el = a[i];
        }
    }
    cout << max_el << endl;
}