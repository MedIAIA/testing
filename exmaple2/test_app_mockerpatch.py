# fichier: test_app.py

import pytest
from unittest.mock import MagicMock
from app import process_user_data

def test_process_user_data(monkeypatch, mocker):
    # Configurer le mock pour get_user_by_id
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.name = "John Doe"
    
    mock_get_user_by_id = mocker.patch('app.get_user_by_id', return_value = mock_user)

    # Configurer le mock pour send_email_to_user
    mock_send_email_to_user = mocker.patch('app.send_email_to_user', return_value = None)

    # Appeler la fonction avec les mocks
    db_mock = MagicMock()
    user_id = 1
    email_content = "Welcome to our service!"

    result = process_user_data(db_mock, user_id, email_content)

    # Vérifier que les fonctions mockées ont été appelées correctement
    mock_get_user_by_id.assert_called_once_with(db_mock, user_id)
    mock_send_email_to_user.assert_called_once_with(mock_user, email_content)

    # Vérifier le résultat de la fonction
    assert result == mock_user
