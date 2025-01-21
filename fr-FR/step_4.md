<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/xx0VQ0RJc8A?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div>
</html>

## Utiliser le WebUi

Le WebUI fonctionne comme n'importe quelle autre interface chatbot. Tu peux saisir tes prompts et voir les réponses générées par le modèle.

![Interface utilisateur d'une application web montrant un message d'accueil "Bonjour, Monsieur C" et la question "Comment puis-je vous aider aujourd'hui ?". Il y a quatre suggestions ci-dessous : "Grammar check" (vérification grammaticale), "Show me a code snippet" (Montre-moi un extrait de code), "Give me ideas" (Donne-moi des idées), et une partie d'un autre prompt. La barre latérale gauche inclut des options pour "New Chat" (Nouveau Chat), "Workspace" (Espace de travail) et "Search" (Rechercher). Le coin en haut à droite montre une icône utilisateur circulaire avec des initiales "MC".](images/webUI.png)

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
