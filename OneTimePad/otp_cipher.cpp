#include "otp_cipher.h"


/**
 * @brief Construct a new otp cipher::otp cipher object. Populates
 * xor_result with the char[] representation
 * 
 * @param c1 - length = c1_c2_length
 * @param c2 - length = c1_c2_length
 * @param c1_c2_length 
 * @param xor_result - length = c1_c2_length + 1, for null termination
 */
OTP_Cipher::OTP_Cipher(uint8_t * c1, uint8_t * c2, int c1_c2_length, char *xor_result)
{
    for(int i = 0; i < c1_c2_length; i++)
    {
        xor_result[i] = c1[i] ^ c2[i];
    }

    xor_result[c1_c2_length] = '\0'; //Null termination
}