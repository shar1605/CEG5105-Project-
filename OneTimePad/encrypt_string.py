"""
Aim, replace all strings, enclosed in a '' or "" with str1 XOR str2, which hides
the original string. Simple One time pad implementation

"""

import random
import sys
from typing import Tuple, List

def get_otp_vals(input_str:str)->Tuple[List[int], List[int]]:
    """m1 xor m2 = input_str

    Args:
        input_str (str): _description_

    Returns:
        Tuple[str,str]: c1, c2
    """
    
    c1_char_arr = []
    c2_char_arr = []
    
    input_str_arr = [] # c1 xor c2 = input_str
    
    for i in range(len(input_str)):
        ascii_char = ord(input_str[i])
        
        input_str_arr.append(ascii_char)
        
        c1_rand = random.randint(0,255) # ASCII 0, 255, might not be readable!
        c2_res = ascii_char ^ c1_rand
        
        c1_char_arr.append(c1_rand)
        c2_char_arr.append(c2_res)
        
        #assert c1_rand ^ c2_res ==  ascii_char
    
    return c1_char_arr, c2_char_arr

def code_from_char_array(arr:List[int]):
    res = ["{"]
    for val in arr:
        res.append(str(val))
        res.append(",")

    res[-1] = "}" # Replace last comma
    
    return ''.join(res)

def encrypt_code(code):
    """c1, c2 ... c99 must not exist in the .ino

    Args:
        code (_type_): _description_

    Returns:
        _type_: _description_
    """
    new_code = []
    variable_counter = 0 # variables are c0, c1, c2....
    
    for line in code:
        
        string_delitter = None
        
        # Edge cases, where delimitters are there but string replacement not needed
        if "#include" in line:
            pass
        # Ignore snprintf as it doenst really help to provide attacker with info
        elif "%" in line: 
            pass
        
        
        # Search for delimiter
        if '"' in line:
            string_delitter = '"'

        if string_delitter is None:
            new_code.append(line)
        else:
            # Assume only one string value!
            left, string, right = line.split(string_delitter)
            
            c1, c2 = get_otp_vals(string)
            
            text_len = len(c1)
            
            c1_var_counter = f"c{variable_counter}"
            variable_counter+=1
            c2_var_counter = f"c{variable_counter}"
            variable_counter += 1
            xor_var_counter = f"xor{variable_counter}"
            variable_counter += 1
            
            # declare and assign, c1, c2, xor
            # to improve: add indentation, put all in one line so its neater
            new_code.append(f"const char {c1_var_counter}[] = {code_from_char_array(c1)};")
            new_code.append(f"const char {c2_var_counter}[] = {code_from_char_array(c2)};")
            new_code.append(f"char {xor_var_counter}[{text_len+1}];")
            new_code.append(f"OTP_Cipher({c1_var_counter}, {c2_var_counter}, {text_len}, {xor_var_counter});")
            new_code.append("".join((left,xor_var_counter,right)))
            new_code.append(f"memset({xor_var_counter}, 0, sizeof({xor_var_counter}));")
    
    return new_code


if __name__ == "__main__":
    args = sys.argv
    if len(sys.argv) < 2:
        print("Usage: python encrypt_string.py <target.ino>")
        sys.ext(1)
        
    ino_filepath = args[1]
    with open(ino_filepath, 'r') as f:
        orig_code = f.read()
        orig_code_split = orig_code.split("\n")
        
    new_ino_filepath = "new_" + ino_filepath
    with open(new_ino_filepath, 'w') as f:
        for line in encrypt_code(orig_code_split):
            f.write(line + "\n")

    print("Orig:", ino_filepath)
    print("New :", new_ino_filepath)