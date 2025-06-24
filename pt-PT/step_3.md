<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/LZFqptMrWPA?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div>
</html>

## Puxa e executa um modelo para o teu Ollama

Em poucas palavras, "puxar um modelo" significa descarregar um modelo específico de IA que o Ollama vai usar para executar tarefas.

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Existem vários modelos disponíveis em [ollama.com/library](https://ollama.com/library){:target="_blank"}. Nós recomendamos que comeces por `gemma:2b`, `phi`, ou `tinyllama`. Tem cuidado com modelos que tenham mais que 5 mil milhões parâmetros, pois podem ser demasiado exigentes para um Raspberry Pi padrão.
</p>

--- task ---

Executa o comando seguinte e substituí `[nome do modelo aqui]` pelo nome do modelo que pretendes utilizar:

```sh
ollama run [nome do modelo aqui]
```

Vais ver barras de progresso serem preenchidas e depois vai pedir-te para testares o modelo.

![Uma animação que mostra uma interface de linha de comandos com um prompt a exibir "pi@raspberrypi:~ $" seguido por um comando a ser digitado.](images/run_gemma2b.gif)

--- /task ---

--- task ---

Interage com o modelo fazendo perguntas, pedindo-lhe que escreva um poema ou uma história, ou que aja como suporte de estudos:

```
O Xiribiti, do sol e da terra,
Que vaga pelo céu, sem parar.
Um ritmo alegre, um tom soado,
Que inspira a gente, grande e pequena.

Ele dança no céu, livre e alto,
E a sua luz brilha, um sinal forte.
O Xiribiti, um símbolo de paz,
Que guia a gente, na noite.
```

Pressiona `Ctrl + D` para sair do processo de prompt do LLM quando terminares.

--- /task ---

--- collapse ---
---
title: Modelos e espaço recomendados
---

Existem muitos modelos disponíveis na biblioteca Ollama, mas os modelos maiores (com mais parâmetros) vão ocupar mais espaço no teu disco rígido, além de necessitarem de mais tempo para descarregar e mais memória para executar.

O número de parâmetros de um modelo pode ser considerado como o "tamanho" do conjunto de dados de treino do modelo: mais parâmetros geralmente significa que o modelo pode encontrar e representar padrões mais complexos nos dados.

Aqui está a lista de modelos, o número de parâmetros e o espaço necessário em GB no teu disco rígido:

| Nome do modelo                  | Parâmetros                       | Tamanho (GB) |
| ------------------------------- | -------------------------------- | ------------------------------- |
| oLLama-7B                       | 7 mil milhões                    | 13                              |
| oLLama-3B                       | 3 mil milhões                    | 6                               |
| oLLama-1B                       | 1 mil milhões                    | 2                               |
| oLLama-500M                     | 500 milhões                      | 1                               |
| oLLama-300M                     | 300 milhões                      | 0.6             |
| Llama2-7B                       | 7 mil milhões                    | 13                              |
| Llama2-13B                      | 13 mil milhões                   | 26                              |
| Phi-3 Mini                      | 3 mil milhões                    | 3.8             |
| Phi-3 Medium                    | 14 mil milhões                   | 15                              |
| Orca Mini                       | 7 mil milhões                    | 13                              |
| Solar                           | 10.7 mil milhões | 6.1-21          |
| Gemma-2B                        | 2 mil milhões                    | 3.5             |
| Gemma-7B                        | 7 mil milhões                    | 11.5            |
| LLaVA-7B                        | 7 mil milhões                    | 5.5             |
| LLaVA-13B                       | 13 mil milhões                   | 17                              |
| StarCoder-7B                    | 7 mil milhões                    | 15                              |
| CodeLlama-7B                    | 7 mil milhões                    | 13                              |
| Dolphin-2.2-70B | 70 mil milhões                   | 28                              |
| Magicoder-7B                    | 7 mil milhões                    | 10.5            |

Podes descarregar e executar qualquer destes modelos no teu Raspberry Pi ao abrir o terminal e escrever:

```bash
ollama run [nome do modelo aqui]
```

Por exemplo, para executar `gemma:2b`, escreve:

```bash
ollama run gemma:2b
```

--- /collapse ---
