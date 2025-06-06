<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/xx0VQ0RJc8A?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div>
</html>

## Usa la WebUI

La WebUI funziona come qualsiasi altra interfaccia di chatbot. Puoi digitare i tuoi prompt e vedere le risposte generate dal modello.

![Uno screenshot di un'interfaccia IA con un design pulito e minimalista. Al centro è ben visibile il testo "Ciao, MrC". In basso è presente una barra di ricerca con la didascalia "Come posso aiutarti oggi?" e le icone di microfono e audio sulla destra.icona. Tra i prompt suggeriti troviamo "Raccontami una curiosità sull’Impero Romano", "Mostrami un esempio di codice per l'intestazione fissa di un sito web" e "Dammi idee su cosa fare con i disegni dei miei figli". Sul lato sinistro c'è un menu con le opzioni "Area di lavoro", "Cerca" e "Chat". In alto a destra si trova un’icona profilo circolare con la lettera "M".](images/webUI.png)

### Installa Docker e la WebUI

\--- task ---

Installa Docker immettendo il seguente comando nel terminale:

```bash
sudo apt install docker.io
```

Attendi che Docker venga installato. L'installazione sarà completata quando vedrai di nuovo il prompt del terminale.

\--- /task ---

\--- task ---

Installa la WebUI copiando e incollando il seguente comando nel terminale:

```bash
sudo docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

Attendi che la WebUI venga installata. L'installazione sarà completata quando vedrai di nuovo il prompt del terminale.

\--- /task ---

\--- task ---

Per accedere all'interfaccia WebUI, vai su `http://localhost:3000/` nel tuo browser.

![Una scheda del browser intitolata "Apri WebUI" mostra l'URL "localhost:3000" nella barra degli indirizzi.](images/localhostURL.png)

\--- /task ---
