#!/usr/bin/env python
#python 2.7.13

#NOPQRSTUVWXYZABCDEFGHIJKLM


def rot13(msg):
    msg = msg.upper()
    key = {"A":"N", "B":"O", "C":"P", "D":"Q", "E":"R", "F":"S", "G":"T", 
           "H":"U", "I":"V", "J":"W", "K":"X", "L":"Y", "M":"Z", "N":"A",
           "O":"B", "P":"C", "Q":"D", "R":"E", "S":"F", "T":"G", "U":"H", 
           "V":"I", "W":"J", "X":"K", "Y":"L", "Z":"M"}
    
    msgEncode = ""
    
    for char in msg:
        try:
            msgEncode = msgEncode + key[char]
        except Exception as error:
            msgEncode = msgEncode +char

    base64encode(msgEncode)

def base64encode(msgEncode):
    
    try:
        import base64
    except Exception:
        pass
    
    try:
        base64Encode = base64.b64encode(msgEncode)
        print base64Encode
        base16Encode = base64.b16encode(base64Encode)
        print base16Encode
    
    except Exception as error:
        pass

def main():
    msg = str(raw_input("Enter String to Encode: "))

    rot13(msg)


main()