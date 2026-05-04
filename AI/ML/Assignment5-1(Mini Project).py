# Lets create a chat room system using OOP concepts. 
# We have to create classes :
# User
# Message
# ChatRoom
# And we have to implement functions 
# sending message
# viewing chat history
# user joining and leaving the chat room

class User:
    def __init__(self,user_name):
        self.user_name = user_name
        self.chatroom=None

    def joins_chatroom(self,chatroom):
        if self.chatroom:
            print(f"{self.user_name} is already in the chatroom")
        else:
            chatroom.adduser(self)
            self.chatroom=chatroom
            print(f"{self.user_name} has joined the {chatroom.name}")
        
    def leave_chatroom(self,):
        if not self.chatroom:
            print(f"{self.user_name} is not in the chatroom")
        else:
            self.chatroom.removeuser(self)
            print(f"{self.user_name} has left the chatroom")
            self.chatroom=None
    
    def send_message(self,content):
        if not self.chatroom:
            print(f"{self.user_name} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self,content)

class Message:
    message_counter =1
    def __init__(self,content,sender):
        self.content=content
        self.sender=sender
        self.id = Message.message_counter
        Message.message_counter+=1

    def __str__(self):
        return f"({self.id}) {self.sender.user_name}: {self.content}"
    

class Chatroom:
    def __init__(self,name):
        self.name=name
        self.message=[]
        self.user=[]

    def adduser(self,user):
        self.user.append(user)

    def removeuser(self,user):
        self.user.remove(user)
    
    def broadcast(self,content,sender):
        message=Message(sender,content)
        self.message.append(message)
        print(message)
    
    def history(self):
         print(f"Chat history of {self.name}: ")
         for msg in self.message:
             print(msg)
         print()

if __name__ == "__main__":
    room=Chatroom("Python tutorial")

u1=User("Saurabh")
u2=User("Priya")
u3=User("Swara")

u1.joins_chatroom(room)
u2.joins_chatroom(room)
u1.send_message("Hello Everyone")
u2.send_message("hey all")
u3.joins_chatroom(room)
u3.send_message("Hey guys, what's up?")
room.history()
u1.leave_chatroom()
u2.leave_chatroom()
u3.leave_chatroom()
    





