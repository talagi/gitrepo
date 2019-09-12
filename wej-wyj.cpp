/*
 * wej-wyj.cpp
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	char imie[10];
    char nazwisko[10];
    
    cout << "Podaj imię: ";
    cin >> imie;
    cout << "Podaj nazwisko: ";
    cin >> nazwisko;
    
    cout << "Witaj " << imie << " ";
    cout << nazwisko;
    
	return 0;
}

