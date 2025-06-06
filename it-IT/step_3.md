<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/LZFqptMrWPA?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div>
</html>

## Scarica ed esegui un modello con Ollama

In parole semplici, "scaricare un modello" significa ottenere un modello IA specifico che Ollama userà per svolgere dei compiti.

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Sono disponibili vari modelli su [ollama.com/library](https://ollama.com/library){:target="_blank"}. Ti consigliamo di iniziare con `gemma:2b`, `phi` o `tinyllama`. Fai attenzione ai modelli con più di 5 miliardi di parametri, perché potrebbero essere troppo pesanti per un Raspberry Pi standard.
</p>

\--- task ---

Esegui questo comando, sostituendo `[nome del modello]` con il nome del modello che vuoi usare:

```sh
ollama run [nome del modello]
```

Vedrai alcune barre di avanzamento riempirsi e poi ti verrà chiesto di dare un comando al modello.

![Animazione che mostra un'interfaccia a riga di comando con il prompt che visualizza "pi@raspberrypi:~ $" mentre viene digitato un comando.](images/run_gemma2b.gif)

\--- /task ---

\--- task ---

Interagisci con il modello facendo domande, chiedendogli di scrivere una poesia o una storia, oppure usandolo come supporto per lo studio:

```
>>> scrivi una breve poesia divertente su Pulcino

Oh Pulcino, che gioia vederti saltare,
Una piuma di sole, che sa di sognare.
La tua risata vola nell'aria serena,
Mentre corri felice tra festa e altalena.
Con un sorriso che illumina il prato,
Fai ridere tutti, anche chi è arrabbiato.
Pulcino, allegria che non puoi fermare,
Un soffio di gioco, che sa di sognare.
```

Premi `Ctrl + D` per uscire dalla sessione quando hai finito di usare il modello linguistico di grandi dimensioni.

\--- /task ---

## --- collapse ---

## title: Modelli consigliati e dimensioni

Ci sono molti modelli disponibili nella libreria Ollama, ma i modelli più grandi (quelli con più parametri) occuperanno più spazio sul disco fisso, richiederanno più tempo per essere scaricati e più memoria per funzionare.

Il numero di parametri di un modello può essere considerato come la "dimensione" del set di dati su cui è stato addestrato: un numero maggiore di parametri permette al modello di individuare e rappresentare schemi e relazioni più complessi nei dati.

Ecco un elenco di modelli, il numero di parametri e la dimensione richiesta in GB sul disco rigido:

| Nome modello                    | Parametri     | Dimensione (GB) |
| ------------------------------- | ------------- | ---------------------------------- |
| oLLama-7B                       | 7 miliardi    | 13                                 |
| oLLama-3B                       | 3 miliardi    | 6                                  |
| oLLama-1B                       | 1 miliardo    | 2                                  |
| oLLama-500M                     | 500 milioni   | 1                                  |
| oLLama-300M                     | 300 milioni   | 0,6                                |
| Llama2-7B                       | 7 miliardi    | 13                                 |
| Llama2-13B                      | 13 miliardi   | 26                                 |
| Phi-3 Mini                      | 3 miliardi    | 3,8                                |
| Phi-3 Medium                    | 14 miliardi   | 15                                 |
| Orca Mini                       | 7 miliardi    | 13                                 |
| Solar                           | 10,7 miliardi | 6,1-21                             |
| Gemma-2B                        | 2 miliardi    | 3,5                                |
| Gemma-7B                        | 7 miliardi    | 11,5                               |
| LLaVA-7B                        | 7 miliardi    | 5,5                                |
| LLaVA-13B                       | 13 miliardi   | 17                                 |
| StarCoder-7B                    | 7 miliardi    | 15                                 |
| CodeLlama-7B                    | 7 miliardi    | 13                                 |
| Dolphin-2.2-70B | 70 miliardi   | 28                                 |
| Magicoder-7B                    | 7 miliardi    | 10,5                               |

Puoi scaricare ed eseguire uno qualsiasi di questi modelli sul tuo Raspberry Pi aprendo il terminale e digitando:

```bash
ollama run [Nome modello]
```

Ad esempio, per eseguire `gemma:2b`, digita:

```bash
ollama run gemma:2b
```

\--- /collapse ---
