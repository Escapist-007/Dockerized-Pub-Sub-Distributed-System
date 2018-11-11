import sys
import socket

def Main():
    
    host = 'server002' # localhost # alias of server 02 in docker network
    port =  5030
    
    subscriberName = str(sys.argv[1])
    print("Subscriber is :",subscriberName)
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))  # Connect to server
    
    flag = True
    
    while True:
       
        if flag:
            s.send(subscriberName.encode())
            flag = False
        
        data = s.recv(2048).decode()
        print(data)


if __name__ == '__main__':
    Main() 
