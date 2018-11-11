import socket
import sys
import random

from _thread import *
from threading import Timer


# Topic based pub-sub -- Multithreading and Socket is needed for implementation

# Global variables

clientList = []

all_topics = ['weather','politics','sports','ub','cse586']

topics = ['weather','politics','sports'] # server1's responsibility is generate events of these topics

subscriptions = {}

events = {'weather' : ['There will be rain today!', 'Sunny weather', 'Extreme cold is coming'],
    'politics' : ['Today is election', 'Who will win: democrate or republic?','Democracy is not for dumb people'],
    'sports' : ['Bangladesh is one of the best cricket team','Messi strikes again!','TT is the best indoor game']
}

# { subscriberName : [msg1, msg2,, ] , ... }
generatedEvents = dict()

flags = dict()

# Handle any client's connection

def threadedClient(connection, data):
    while True:
        flags[data] = 0
        subscribe(data) # Generate subscription for the connected subscriber
        subscriptionInfo = 'Your subscriptions are : ' + str(subscriptions[data])
        connection.send(subscriptionInfo.encode())

        while True:
            if flags[data]==1:
                notify(connection,data)
    connection.close()



# Handle other server's connection

def threadedServerSender(connection, data):
    while True:
        flags[data] = 0
        subscriptions[data] = topics  # Other server's  are subscribed to the all topics of this server
        subscriptionInfo = 'Your subscriptions are : ' + str(subscriptions[data])
        connection.send(subscriptionInfo.encode())
        
        while True:
            if flags[data]==1:
                notify(connection,data)
    connection.close()


def threadedServerReceiver(connection, data):
    while True:
        serverData = connection.recv(2048).decode()
        m = serverData.split('-')
        if len(m)==2:
            topic = m[0]
            event = m[1]
            publish(topic,event,0)
    connection.close()



## SUBSCRIBE()


def subscribe(name):
    subscriptions[name] = randomSubscriptionGenerator()


def randomSubscriptionGenerator():
    subscribedTopicsList = random.sample(all_topics,random.choice(list(range(1,len(all_topics)+1))))
    return subscribedTopicsList



## PUBLISH() and ADVERTIZE()

def eventGenerator():
    
    topic = random.choice(topics)
    msgList = events[topic]
    event = msgList[random.choice(list(range(1,len(msgList))))]
    
    publish(topic,event,1) # call publish() for publishing the new event


def publish(topic,event,indicator):
    
    event = topic + '-' + event  # Concatenate topic and event
    print(event)  # print the event in server console
    
    # publishing generated events to interested subscriber (subscribers + other servers)
    if indicator == 1:
        for name, topics in subscriptions.items() :
            if topic in topics:
                if name in generatedEvents.keys():
                    generatedEvents[name].append(event)
                else:
                    generatedEvents.setdefault(name, []).append(event)
                flags[name] = 1

    # publishing received events to interested subscriber (only subscribers)
    else:
        for name, topics in subscriptions.items() :
            if name in clientList: # only for clients
                if topic in topics:
                    if name in generatedEvents.keys():
                        generatedEvents[name].append(event)
                    else:
                        generatedEvents.setdefault(name, []).append(event)
                    flags[name] = 1

    t = Timer(random.choice(list(range(20,26))), eventGenerator)
    t.start()

                 
def notify(connection,name):
    if name in generatedEvents.keys():
        for msg in generatedEvents[name]:
            msg = msg  # + str("\n")
            connection.send(msg.encode())
        del generatedEvents[name]
        flags[name] = 0



def Main():
    
    host = ""     # Server will accept connections on all available IPv4 interfaces
    port = 5029   # Port to listen on (non-privileged ports are > 1023)
    
    # API orders : socket() -> bind() -> listen() -> accept()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating a socket object with TCP protocol. AF_INET is the Internet address family for IPv4.
    
    s.bind((host,port))  # Binding the socket object to a port


    print("Socket is bind to the port :", port)

    s.listen(5)  # Socket is now listening to the port for new connection with 'backlog' parameter value 5. It defines the length of queue for pending connections

    print("Socket is now listening for new connection ...")
    
    # eventGenerator() will be called in a new thread after 10 to 15 seconds
    t = Timer(random.choice(list(range(20,26))), eventGenerator)
    t.start()
    
    # An infinity loop - server will be up for infinity and beyond
    while True:
        
        connection, addr = s.accept()  # Waiting for new connection to be accepted
        print('Connected to :', addr[0], ':', addr[1])
        print("Connection string is",connection)
        
        # Receive data (c-name or s-name) from new connection and determine if it is a client or other server
        # c means client and name is the name of the client
        # s maens server and name is the name of the server
        data = connection.recv(2048).decode()

        if data:
            print("Welcome ",data)
        
        l = data.split('-')
        
        if l[0]=='c':
            clientList.append(l[1])
            start_new_thread(threadedClient, (connection,l[1]))
        if l[0]=='s':
            start_new_thread(threadedServerSender, (connection,l[1]))
            start_new_thread(threadedServerReceiver, (connection,l[1]))

    s.close()


if __name__ == '__main__':
    Main() 
