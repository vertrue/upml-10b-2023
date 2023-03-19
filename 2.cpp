#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    // розмір масиву
    int n;
    cin >> n;
    
    // створення масиву
    int a[n];
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    
    // знаходження мінімуму
    int min_el = a[0];
    for(int i = 1; i < n; i++)
    {
        min_el = min(min_el, a[i]);
    }
    
    // виведення мінімального елемента
    cout << min_el << endl;
    return 0;
}
