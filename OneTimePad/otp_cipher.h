#ifndef OTP_CIPHER_H
#define OTP_CIPHER_H

#include <stdint.h>
#include <stdio.h>       //Add verbose
#include <string.h>


class OTP_Cipher
{
    public:
        OTP_Cipher(uint8_t * c1, uint8_t * c2, int c1_c2_length, char *xor_result);

};




#endif //OTP_CIPHER_H