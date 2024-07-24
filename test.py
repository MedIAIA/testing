import pytest

from source import reverse_str 

def test_should_reverse_string():
    assert reverse_str("abc") == 'cba'

######################################### monkeypatch #######################################################
import source
from source import main_function
 
def test_main_function_1(monkeypatch):
    """
        
    Test the main function

    """
    # 
    def mockreturn(): # il faut definir une  fonction pour return le valeur à mettre sur la fonction mockeé
        return 100
 
    monkeypatch.setattr(source, 'request', mockreturn) # la fonction à mocker est dans le module source,  nom de fonction est request et le return 

 
    expected_value = 100
    assert main_function() == expected_value



######################################### monkeypatch #######################################################
import player



class MockResponse:  # on mokcer toute la classe 
    @staticmethod
    def get_info(): # la fonction mockés avec le nouveau comportement 
        return {"name": "test", "level":200}
    

def test_create_player(monkeypatch): # on tester la fonction create_player on mocke la fonction exeterne à create_player


    def mock_get(*args,**kwargs):
        return MockResponse()
    
    monkeypatch.setattr('player.Player',mock_get) # 

    excepted_value = {"name": "test", "level":200}

    assert player.create_player() == excepted_value

############################################ mocker ####################################################



# test_circle.py

import circle
from circle import perimeter

def test_perimeter(mocker):
    # Patching the PI variable in the circle module
    mocker.patch.object(circle, 'PI', 3.14)
    expected_value = 12.56
    assert perimeter(2) == expected_value

########################################## mocker ######################################################

import source

def test_main_function_2(mocker):
    mocker.patch('source.request',return_value=100) # modifie le comportement de la fonction request()
    expected_value = 100 
    assert source.main_function() == expected_value

############################################### Mocker Player2 #################################################

from player_class.player import Player
from player_class.weapon import Weapon


def test_player_attck(mocker):
    weapon_player_1 = Weapon(10)
    weapon_player_2 = Weapon(5)
    player_1 = Player("Player 1", weapon_player_1)
    player_2 = Player("Player 2", weapon_player_2)

    mocker.patch("player_class.weapon.Weapon.damage", return_value = 20)

    player_1.attack(player_2)
    except_value = 80   
    assert player_2.get_life_point() == except_value

######################################### Mocker Player1 #######################################################
import player



class MockResponse:  # on mokcer toute la classe 
    @staticmethod
    def get_info(): # la fonction mockés avec le nouveau comportement 
        return {"name": "test", "level":200}
    

def test_create_player(mocker): # on tester la fonction create_player on mocke la fonction exeterne à create_player

    
    mocker.patch('player.Player',return_value = MockResponse()) # 

    excepted_value = {"name": "test", "level":200}

    assert player.create_player() == excepted_value