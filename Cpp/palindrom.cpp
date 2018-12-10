/*
 * palindrom.cpp
 * 
 */


#include <iostream>
#include <string.h>

using namespace std;

bool palindrom(char w[], int r) {
    bool pal = false;
    for( int i = 0; i < (ilosc / 2); i++){
        if (wyraz[i] == wyraz[ilosc - (i+1)]){
                pal = true
        }
    }
    return pal;
}

int main(int argc, char **argv)
{
	int roz = 20;
    char wyraz[20];
    cout << "Podaj wyraz: ";
    cin.getline(wyraz, roz);
    // cout << cin.gcount() << endl;
    int ilosc = strlen(wyraz);
    cout << palindrom(wyraz, ilosc) << endl;
	return 0;
}

