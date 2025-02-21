<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/xx0VQ0RJc8A?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div>
</html>

## Utiliser le WebUi

Le WebUI fonctionne comme n'importe quelle autre interface chatbot. Tu peux saisir tes prompts et voir les réponses générées par le modèle.

![A screenshot of an AI interface displaying a clean, minimalist design. The text "Hello, MrC" is prominently shown in the center. Below, there is a search bar labeled "How can I help you today?" with a microphone and audio icon to the right. Suggested prompts include "Tell me a fun fact about the Roman Empire," "Show me a code snippet of a website's sticky header," and "Give me ideas for what to do with my kids' art." On the left side, there is a menu with options for "Workspace," "Search," and "Chats." A circular profile icon labeled "M" is in the top right corner.](images/webUI.png)

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
