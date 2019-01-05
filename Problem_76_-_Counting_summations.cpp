/*
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

REPONSE :
190569291
*/

#include <iostream>
using namespace std;

int cible = 100;

int fonc(int somme, int dernier){
    
    if (somme > cible)
        return 0;
    
    if (somme == cible)
        return 1;

    int total = 0;
    for (int i = 1; i <= dernier; i++){
        total += fonc(somme + i, i);
    }
    return total;
}

int main() {
  cout << fonc(0, cible) - 1;
}