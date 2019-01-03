/*
 * petle.cpp
 * 
 */


#include <iostream>
using namespace std;

int cw01() {
    int suma = 0;
    
    for(int i = 10; i <=99; i++){
        if (i % 2 ==0)
        suma = suma + i;
    }
    cout << "Suma: " << suma;

}
 
 
int cw02(){
    int a, b, suma;
    bool czy = true;
    
    while(czy == true) {
        cout << "Podaj liczbę; ";
        cin >> a;
        
        if (a == suma)
            czy = false;
        suma = b +a;
        b = a;
    }
    return 0;
}

int cw03(){
    int liczba;
    int suma = 0;
    int podzielnych = 0;
    
    for(int i = 0; i < 8; i++){
        cin >> liczba;
        suma += liczba;
        if(liczba % 5 == 0) podzielnych++;
    }
    cout << "Suma : " << suma <<endl;
    cout << "Średnia: " << suma/8.0 << endl;
    cout << "Podzielne przez 5: " << podzielnych << endl;
    
    cin.get();
    cin.ignore(1);
    
    return 0;
}

int main(int argc, char **argv)
{
    cw03();
	//cw02();
    // cw01();
	return 0;
}

