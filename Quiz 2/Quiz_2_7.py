class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
 
def insert(atMe, newFrob):
    if newFrob.myName() < atMe.myName():
        if atMe.getBefore() == None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        elif atMe.getBefore().myName()<newFrob.myName():
            atMe.getBefore().setAfter(newFrob)
            newFrob.setBefore(atMe.getBefore())
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        else:
            insert(atMe.getBefore(),newFrob)

    elif newFrob.myName() > atMe.myName():
        if atMe.getAfter() == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif atMe.getAfter().myName()>newFrob.myName():
            atMe.getAfter().setBefore(newFrob)
            newFrob.setAfter(atMe.getAfter())
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            insert(atMe.getAfter(),newFrob)

    elif newFrob.myName()==atMe.myName():
        if atMe.getAfter() != None:
            newFrob.setAfter(atMe.getAfter())
        newFrob.setBefore(atMe)
        if atMe.getAfter() != None:
            atMe.getAfter().setBefore(newFrob)
        atMe.setAfter(newFrob)


def findFront(start):
    
    """
   start: a Frob that is part of a doubly linked list
   returns: the Frob at the beginning of the linked list
   """
    if start.getBefore() == None:
        return start
    else:
        return findFront(start.getBefore())

p = Frob('percival')
print findFront(p)
