/*
 * Program to blink 3 LEDs according to the binary values from 1 through 7
 * First steps in AVR hacking ;)  - Ershad K, Shafeeq K  
 *
 * Connect 3 LEDs in PD1, PD0, PC5 and common ground. 
 */

#include <avr/io.h>
#include <compat/ina90.h>    // needed for  _NOP()
void waitd()
{
    register unsigned short int t = 0;
    while(++t) _NOP();
}

void glow(unsigned short int* b)
{
    PORTC = 0;
    PORTD = 0;
    waitd();
    waitd();
    if (*b)
        PORTC = 0x20;
    if (*(b+1))
        PORTD |= 0b00000001;
    if(*(b+2))
        PORTD |= 0b00000010;

    waitd();
    waitd();
}

int main()
{
    DDRC |= 0x20;
    DDRD |= 0xFF;
    PORTC = 0;
    PORTD = 0;
  
    unsigned short int i = 0;
    unsigned short int k;
    unsigned short int n;
    unsigned short int b[3];
  
    for (; i <= 7; i++ )  {
        n = i;
        k = 0;
        b[0] = b[1] = b[2] = 0;
        for(; n!= 0; n /=2) {
            b[k++] = n % 2;
        }
        glow(b);
        if(i == 7)
            i = 0;
    }
    return 1;
}
