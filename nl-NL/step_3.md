<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/LZFqptMrWPA?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div>
</html>

## Haal een model op voor je Ollama en voer het uit

Simpel gezegd betekent 'een model ophalen' dat je een specifiek AI-model downloadt dat Ollama gebruikt om taken uit te voeren.

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Er zijn verschillende modellen beschikbaar op [ollama.com/library](https://ollama.com/library){:target="_blank"}. We raden aan om te beginnen met `gemma:2b`, `phi`, of `tinyllama`. Wees voorzichtig met modellen met meer dan 5 miljard parameters, omdat ze misschien te veel capaciteit vragen van een standaard Raspberry Pi.
</p>

\--- task ---

Voer de volgende opdracht uit en vervang `[model name here]` door de naam van het model dat je wilt gebruiken:

```sh
ollama run [model name here]
```

You will see some progress bars fill up and then you will be asked to prompt the model.

![Animation showing a command line interface with the prompt displaying "pi@raspberrypi:\~ $" followed by a command being typed.](images/run_gemma2b.gif)

\--- /task ---

\--- task ---

Interact with the model by asking it questions, requesting it to write a poem or story, or as a study aid.

![Screenshot of a black background with white text displaying a short, funny poem about skibidi. Whatever that is.](images/skibidi.png)

Press `Ctrl + D` to exit the LLM prompting process when you are done.

\--- /task ---

## --- collapse ---

## title: Recommended models and sizes

There are lots of models available in the Ollama library, but larger models (models with more parameters) will take more space on your hard disk, as well as needing more time to download and more memory to run.

The number of parameters of a model can be thought of as the "size" of the model's training data set: more parameters generally mean the model can find and represent more complex patterns and relationships in the data.

Here is a list of models, the number of parameters, and their required size in GB on your hard disk:

| Model name                      | Parameters                   | Size (GB) |
| ------------------------------- | ---------------------------- | ---------------------------- |
| oLLama-7B                       | 7 billion                    | 13                           |
| oLLama-3B                       | 3 billion                    | 6                            |
| oLLama-1B                       | 1 billion                    | 2                            |
| oLLama-500M                     | 500 million                  | 1                            |
| oLLama-300M                     | 300 million                  | 0.6          |
| Llama2-7B                       | 7 billion                    | 13                           |
| Llama2-13B                      | 13 billion                   | 26                           |
| Phi-3 Mini                      | 3 billion                    | 3.8          |
| Phi-3 Medium                    | 14 billion                   | 15                           |
| Orca Mini                       | 7 billion                    | 13                           |
| Solar                           | 10.7 billion | 6.1-21       |
| Gemma-2B                        | 2 billion                    | 3.5          |
| Gemma-7B                        | 7 billion                    | 11.5         |
| LLaVA-7B                        | 7 billion                    | 5.5          |
| LLaVA-13B                       | 13 billion                   | 17                           |
| StarCoder-7B                    | 7 billion                    | 15                           |
| CodeLlama-7B                    | 7 billion                    | 13                           |
| Dolphin-2.2-70B | 70 billion                   | 28                           |
| Magicoder-7B                    | 7 billion                    | 10.5         |

You can download and run any of these models on your Raspberry Pi by opening the terminal and entering:

```bash
ollama run [Model Name]
```

For example, to run `gemma:2b`, type:

```bash
ollama run gemma:2b
```

\--- /collapse ---
