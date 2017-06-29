import sys

class User:
    def __init__ (self, name, id, connections):
        self.name = name
        self.id = id
        self.connections = connections
    def setName (self, new_name):
        self.name = new_name
    def getName (self):
        return self.name
    def setId (self, new_id):
        self.id = new_id
    def getID (self):
        return self.id
    def setConnections (self, new_connections):
        self.connections = new_connections
    def getConnections (self):
        return self.connections
    def addConnection (self, new_connection):
        self.connections.append(new_connection)
    def __str__ (self):
        return name + " " + id + " " + connections
    # Define the fields and methods for your object here.


class Network:
    def __init__ (self, users):
        self.users = users
    def setUsers(self, new_users):
        self.users = new_users
    def getUsers(self):
        return self.users
    def addUser(self, new_user):
        self.users.append(new_user)
    def printUsers(self):
        print (self.getUsers())
    # Define the fields and methods for your object here.


def main():
    #sys.argv[1] = name
    #sys.argv[2] =

    A = User('Abigail', 2, [])
    B = User('B', 3, [A])

    network = Network([A, B])

    network.printUsers()

    # Define the program flow for your user interface here.


# Runs your program.
if __name__ == '__main__':
    main()
