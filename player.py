
class Player:
    def __init__(self,name,level):
        self.name = name
        self.level = level 

    def get_info(self): # la fonction à mocker 
        info = {
            "name" : self.name,
            "level" : self.level
        }
        return info
    
def create_player():
    player = Player("ronaldo",100)
    info = player.get_info()
    return info
    

