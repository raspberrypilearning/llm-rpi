<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/xx0VQ0RJc8A?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div>
</html>

## Utiliser le WebUi

Le WebUI fonctionne comme n'importe quelle autre interface chatbot. Tu peux saisir tes prompts et voir les réponses générées par le modèle.

![Une capture d'écran d'une interface IA affichant un design épuré et minimaliste. Le texte « Bonjour, MrC » est bien visible au centre. Ci-dessous, il y a une barre de recherche intitulée « Comment puis-je vous aider aujourd'hui ? » avec un microphone et une icône audio à droite. Parmi les suggestions, citons : « Raconte-moi un fait amusant sur l'Empire romain », « Montre-moi un extrait de code d'un sticky header collant d'un site web » et « Donne-moi des idées sur ce qu'il faut faire avec les œuvres d'art de mes enfants ». Sur le côté gauche, un menu propose des options pour « Espace de travail », « Rechercher » et « Conversations ». Une icône de profil circulaire intitulée « M » se trouve dans le coin supérieur droit.](images/webUI.png)

### Installer Docker et WebUI

\--- task ---

Installe Docker en entrant la commande suivante dans le terminal :

```bash
sudo apt install docker.io
```

Attends que Docker s'installe. Tu sauras que l’installation est terminée lorsque l’invite du terminal reviendra.

\--- /task ---

\--- task ---

Installe WebUI en copiant et en collant la commande suivante dans le terminal :

```bash
sudo docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

Attends que WebUI s'installe. Tu sauras que l’installation est terminée lorsque l’invite du terminal reviendra.

\--- /task ---

\--- task ---

Accède à l'interface WebUI en naviguant vers `http://localhost:3000/` dans ton navigateur web.

![Un onglet du navigateur intitulé "Open WebUI" affiche l'URL "localhost:3000" dans la barre d'adresse.](images/localhostURL.png)

\--- /task ---
