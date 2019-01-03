class Player():
    def __init__(self, name = "", position = None, substitute = False):
        self._name = name
        self._position = position
        self._substitute = substitute
        
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
        
    def getPosition(self):
        return self._position
    
    def setPosition(self, position):
        self._position = position

    def isSubstitute(self):
        return self._substitute
p = Player()
