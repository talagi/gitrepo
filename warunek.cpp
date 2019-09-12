/*
 * warunek.cpp
 * 
 */


#include <iostream>
using namespace std;

int main()
{
    int licz(0);
    int max(0);
    
    cout << "Podaj 3 liczby \n";
    for (int i(0); i<3; i++)
    {
        cin >> licz;
        if (licz > max)
        {
            max= licz;
        }
        
    }
    cout << "Największa liczba: " << max << endl;
    
	return 0;
}

