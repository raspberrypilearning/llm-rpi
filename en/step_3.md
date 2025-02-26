<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/LZFqptMrWPA?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div>
</html>

## Pull and run a model for your Ollama

In simple terms, "pulling a model" means downloading a specific AI model that Ollama will use to perform tasks. 

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
There are various models available at [ollama.com/library](https://ollama.com/library){:target="_blank"}. We recommend starting with `gemma:2b`, `phi`, or `tinyllama`. Be cautious with models larger than 5 billion parameters, as they might be too demanding for a standard Raspberry Pi.
</p>

--- task ---

Run the following command, replacing `[model name here]` with the name of the model you want to use:

```sh
ollama run [model name here]
```
You will see some progress bars fill up and then you will be asked to prompt the model.

![Animation showing a command line interface with the prompt displaying "pi@raspberrypi:~ $" followed by a command being typed.](images/run_gemma2b.gif)

--- /task ---

--- task ---

Interact with the model by asking it questions, requesting it to write a poem or story, or act as a study aid:

```
>>> write a short funny poem about skibidi

Oh Skibidi, you're a sight to behold,
A sail that's made of clouds, so light and
bold.
Your laughter echoes through the air,
As you dance across the starry fair.
With a grin so wide, you fill the sky,
A twinkle that makes everyone sigh.
Skibidi, a joy we cannot deny,
A skibidi, a playful sigh.
```

Press `Ctrl + D` to exit the LLM prompting process when you are done.

--- /task ---

--- collapse ---
---
title: Recommended models and sizes
---

There are lots of models available in the Ollama library, but larger models (models with more parameters) will take more space on your hard disk, as well as needing more time to download and more memory to run. 

The number of parameters of a model can be thought of as the "size" of the model's training data set: more parameters generally mean the model can find and represent more complex patterns and relationships in the data.

Here is a list of models, the number of parameters, and their required size in GB on your hard disk: 

| Model name       | Parameters    | Size (GB) |
| ---------------- | ------------- | --------- |
| oLLama-7B        | 7 billion     | 13        |
| oLLama-3B        | 3 billion     | 6         |
| oLLama-1B        | 1 billion     | 2         |
| oLLama-500M      | 500 million   | 1         |
| oLLama-300M      | 300 million   | 0.6       |
| Llama2-7B        | 7 billion     | 13        |
| Llama2-13B       | 13 billion    | 26        |
| Phi-3 Mini       | 3 billion     | 3.8       |
| Phi-3 Medium     | 14 billion    | 15        |
| Orca Mini        | 7 billion     | 13        |
| Solar            | 10.7 billion  | 6.1-21    |
| Gemma-2B         | 2 billion     | 3.5       |
| Gemma-7B         | 7 billion     | 11.5      |
| LLaVA-7B         | 7 billion     | 5.5       |
| LLaVA-13B        | 13 billion    | 17        |
| StarCoder-7B     | 7 billion     | 15        |
| CodeLlama-7B     | 7 billion     | 13        |
| Dolphin-2.2-70B  | 70 billion    | 28        |
| Magicoder-7B     | 7 billion     | 10.5      |

You can download and run any of these models on your Raspberry Pi by opening the terminal and entering:

```bash
ollama run [Model Name]
```

For example, to run `gemma:2b`, type:

```bash
ollama run gemma:2b
```

--- /collapse ---
