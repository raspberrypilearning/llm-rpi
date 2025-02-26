<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/3MlalSPu1gI?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div><br><br>
</html>

## Reconnaissance d'images avec WebUI

Pour utiliser Ollama, tu dois télécharger un modèle à utiliser. Précédemment, tu as utilisé le modèle `gemma:2b`, mais dans cette étape, tu utiliseras le modèle d'analyse d'image appelé `LLaVa`.

--- task ---

Pour télécharger le modèle LLaVA, accède à l'interface web via `http://localhost:3000`.

--- /task ---

--- task ---

Inscris-toi au WebUI Ollama.

Lors de l'utilisation de WebUI pour la première fois, il te sera demandé de fournir un nom, une adresse e-mail et un mot de passe. Tu peux utiliser n'importe quelle adresse e-mail créée pour cela, il est uniquement destiné à une utilisation locale sur ton Raspberry Pi.

![Un formulaire d'inscription à "Open WebUI" avec des champs pour le nom, l'adresse e-mail et le mot de passe. Le champ du nom est rempli par "Mr.C", le champ de l'adresse e-mail par "test@whatever.com", et le champ du mot de passe affiche une série de points indiquant un mot de passe caché. En dessous de ces champs, il y a un bouton "Create Account" (Créer un compte) avec un curseur pointant dessus, et un lien pour les utilisateurs qui ont déjà un compte pour se connecter.](images/webUI_signup.png)

--- /task ---

--- task ---

Choisis le modèle à utiliser dans le menu déroulant en haut du WebUI. Tu peux également rechercher et ajouter de nouveaux modèles de cette façon : tape `llava:latest` dans la recherche et choisis `Pull llava:latest from Ollama.com`. Ton modèle commencera à se télécharger.

![Un menu déroulant intitulé "Select a model" (Sélectionner un modèle) affiche un champ de recherche dans lequel le texte "llava:latest" a été saisi. Sous le champ de recherche, le texte "No results found" (Aucun résultat trouvé) est affiché, suivi d'une option sélectionnable pour "Pull 'llava:latest' from Ollama.com". Un curseur survole cette option.](images/model_dropdown.png)

--- /task ---

--- task ---

Attends que le modèle soit téléchargé et vérifié. Cela peut prendre du temps.

--- /task ---

### Utiliser LLaVa pour analyser une image

<html>
<br><br>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/ruU6KsVyxKA?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div><br><br>
</html>

--- task ---

Une fois le modèle LLaVA téléchargé, commence une nouvelle session de chat en sélectionnant le modèle parmi les options disponibles.

![Capture d'écran montrant le menu de sélection du modèle avec "llava:latest 7B" en surbrillance.](images/select_llava_model.png)

--- /task ---

--- task ---

Charge une image en utilisant le bouton "Upload Image.
![Un élément d'interface utilisateur comportant deux boutons : "Upload Files" (Charger des fichiers) en haut avec une icône de document, et un bouton "Send a Message" (Envoyer un message) en dessous, qui est grisé et comporte un symbole plus. Un curseur pointe vers le symbole plus sur le bouton "Send a Message" .](images/upload_image.png)

--- /task ---

--- task ---

Après le chargement, saisis un prompt ou une question à propos de l'image dans la fenêtre de discussion. Appuie sur <kbd>Entrée</kbd>.

![Une petite image d'un chat orange au poil long avec un poitrail blanc et un nœud rose autour du cou. Le chat regarde directement la caméra avec une expression curieuse. À côté de l'image, il y a un symbole plus et le texte "describe this picture".](images/cat_prompt.png)

--- /task ---

--- task ---

Examine la description ou l'analyse générée par le modèle LLaVA. Tu peux poser plus de questions ou charger des images supplémentaires.

En utilisant cette image :
![L'image montre un gros plan d'un chat domestique avec de grands yeux et une expression attentive. Le chat a un pelage soyeux, principalement dans des tons crème et blanc, avec des marques plus foncées sur son visage, ses oreilles et ses pattes. Il semble s'asseoir ou s'allonger, avec ses pattes avant légèrement étendues vers le spectateur. La queue du chat est enroulée contre son corps. Derrière le chat se trouve un bouquet de fleurs de lavande, ajoutant une touche de couleur et de texture à l'image. Sur le côté gauche de la photo, il y a une teinte violette, suggérant un mur ou un arrière-plan bleu. Au premier plan, on peut voir une surface en bois, peut-être une table ou un comptoir, avec quelques herbes placées dans un récipient dans le coin supérieur droit. Le style général de l'image est réaliste, l'accent étant mis sur les détails et sur une faible profondeur de champ qui met en valeur les traits du chat.](images/cat.jpg)

LLaVa a fourni cette description :

`L'image montre un gros plan d'un chat domestique avec de grands yeux et une expression attentive. Le chat a un pelage soyeux, principalement dans des tons crème et blanc, avec des marques plus foncées sur son visage, ses oreilles et ses pattes. Il semble s'asseoir ou s'allonger, avec ses pattes avant légèrement étendues vers le spectateur. La queue du chat est enroulée contre son corps. Derrière le chat se trouve un bouquet de fleurs de lavande, ajoutant une touche de couleur et de texture à l'image. Sur le côté gauche de la photo, il y a une teinte violette, suggérant un mur ou un arrière-plan bleu. Au premier plan, on peut voir une surface en bois, peut-être une table ou un comptoir, avec quelques herbes placées dans un récipient dans le coin supérieur droit. Le style général de l'image est réaliste, l'accent étant mis sur les détails et sur une faible profondeur de champ qui met en valeur les caractéristiques du chat.`

--- /task ---
