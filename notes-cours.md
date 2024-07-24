# Pytest :
* les Mocks : 
  - monkeypatch : 
                    Monkeypatch fournit un ensemble de méthodes pour mocker nos fonctionnalités : 

                    - monkeypatch.setattr(obj, name, value, raising=True): Modifier le comportement d’une fonction ou d’une classe.

                    -  monkeypatch.delattr(obj, name, raising=True): Supprimer la fonction du test.

                    monkeypatch.setitem(mapping, name, value): Modifier les éléments d’un dictionnaire.

                    - monkeypatch.delitem(obj, name, raising=True): Supprimer un élément d’un dictionnaire.

                    - monkeypatch.setenv(name, value, prepend=False): Définir une variable d’environnement.

                    - monkeypatch.delenv(name, raising=True): Supprimer une variable d’environnement.
  - pytest-mock : 
        * installation 
                
                pip install pytest-mock
            # Installer Python 3.9 via Homebrew (macOS)
                brew install python@3.9

            # Ajouter Python 3.9 à PATH (macOS)
                echo 'export PATH="/usr/local/opt/python@3.9/bin:$PATH"' >> ~/.zshrc
                source ~/.zshrc
                

        * En résumé
            # Les mocks permettent de simuler le comportement d’une méthode ou d’un objet.

            # Monkeypatch fournit la méthodemonkeypatch.setattr()qui permet de modifier le comportement de fonctions, de méthodes ou même d’objets.

            # La méthodemocker.patch.object()permet de mocker une constante.

            # La méthodemocker.patch()permet de mocker une fonction ou un objet.

 