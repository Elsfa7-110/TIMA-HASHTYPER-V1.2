import hashlib
from platform import system
import os , sys

if system() == 'Linux':
    os.system('clear')
elif system() == 'Windows':
    os.system('cls')
print ('''
[*] TIMA HASHTYPER V1.2
\033[1;31;40m AHMED SALAH ABDALHAFZ  \n
  _____   _          __           _____           _   _    ___   
 | ____| | |  ___   / _|   __ _  |___  |         / | / |  / _ \  
 |  _|   | | / __| | |_   / _` |    / /   _____  | | | | | | | | 
 | |___  | | \__ \ |  _| | (_| |   / /   |_____| | | | | | |_| | 
 |_____| |_| |___/ |_|    \__,_|  /_/            |_| |_|  \___/  



''')

while True:
    the_hash = input ('[*]enter your hash > ')
    if int(len(the_hash))==32:
        print ('[+] hash >>> MD5' + ' or ' + 'MD4')
    elif int (len (the_hash)) ==40:
        print ('[+] hash >>> SHA1' +' or ' + 'ecdsa-with-SHA1' + ' or ' +' DSA-SHA  or ripemd160')
    elif int (len (the_hash)) == 56 :
        print ('[+] hash >>> SHA224')
    elif int(len(the_hash)) == 64:
        print ("[+]HASH >> SHA256 ")
    elif int(len(the_hash)) == 96:
        print ("[+]HASH >> SHA384 HASH or sha384")
    elif int(len(the_hash))== 128:
        print ("[+]hash >> SHA512 or sha512")
    elif int(len(the_hash))== 130:
        print ('[*] hash >> whirlpool')
    elif int(len(the_hash))== 60:
        print ('[*] hash >> BCRYPT')
    elif int(len(the_hash))== 16:
        print ('[*] hash >> MySQL323')
    elif int(len(the_hash))== 110:
        print ('[*] hash >> Juniper IVE')
    elif int(len(the_hash))== 136:
        print ('[*] hash >> BLAKE2b-512')
    elif int(len(the_hash))== 19:
        print ('[*] hash >>  Cisco-ASA MD5')
    elif int(len(the_hash))== 27:
        print ('[*] hash >>  Oracle H: Type (Oracle 7+), DES(Oracle)')
    elif int(len(the_hash))== 174:
        print ('[*] hash >>  NetNTLMv2')
    elif int(len(the_hash))== 43:
        print ('[*] hash >>  Cisco-IOS type 4')
    elif int(len(the_hash))== 57:
        print ('[*] hash >>  Samsung Android Password/PIN')
    elif int(len(the_hash))== 47:
        print ('[*] hash >>  FortiGate (FortiOS)')
    elif int(len(the_hash))== 21:
        print ('[*] hash >>  SAP CODVN B (BCODE)')
    elif int(len(the_hash))== 55:
        print ('[*] hash >>  Drupal7')
    elif int(len(the_hash))== 321:
        print ('[*] hash >>  Windows Phone 8+ PIN/password')

    else:
        print ('[#]error >> 404 not found ')
        

