<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/LZFqptMrWPA?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div>
</html>

## Puxe e execute um modelo para o seu Ollama

Em poucas palavras, "puxar um modelo" significa baixar um modelo de IA específico que Ollama usará para executar tarefas.

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Há vários modelos disponíveis em [ollama.com/library](https://ollama.com/library){:target="_blank"}. Recomendamos começar com `gemma:2b`, `phi` ou `tinyllama`. Tenha cuidado com modelos que tenham mais de 5 bilhões de parâmetros, pois eles podem ser muito exigentes para um Raspberry Pi padrão.
</p>

\--- task ---

Execute o seguinte comando e substitua `[nome do modelo aqui]` pelo nome do modelo que você deseja usar:

```sh
ollama run [nome do modelo aqui]
```

Você verá algumas barras de progresso se preencherem e, em seguida, será solicitado que você dê instruções ao modelo.

![Animação mostrando uma interface de linha de comando com o prompt exibindo "pi@raspberrypi:~ $" seguido por um comando sendo digitado.](images/run_gemma2b.gif)

\--- /task ---

\--- task ---

Interaja com o modelo fazendo perguntas, solicitando que escreva um poema ou uma história, ou que aja como um suporte de estudos:

```
>>> Escreva um poema curto e engraçado sobre Skibidi

Oh, Skibidi, você é uma visão para se contemplar,
Uma vela feita de nuvens, tão leve e
ousada.
Seu riso ecoa pelo ar,
Enquanto você dança pela feira estrelada.
Com um sorriso tão largo, você preenche o céu,
Um brilho que faz todos suspirarem.
Skibidi, uma alegria que não podemos negar,
Um Skibidi, um suspiro brincalhão.
```

Pressione `Ctrl + D` para sair do processo de solicitação de LLM quando você terminar.

\--- /task ---

## --- collapse ---

## title: Modelos e tamanhos recomendados

Há muitos modelos disponíveis na biblioteca Ollama, mas modelos maiores (modelos com mais parâmetros) vão tomar mais espaço em seu disco rígido, Além de precisar de mais tempo para baixar e mais memória para executar.

O número de parâmetros de um modelo pode ser considerado como o "tamanho" do conjunto de dados de treinamento do modelo: mais parâmetros geralmente significam que o modelo pode encontrar e representar padrões e relações mais complexas nos dados.

Aqui está uma lista de modelos, o número de parâmetros e seu tamanho necessário em GB no seu disco rígido:

| Nome do modelo                  | Parâmetros   | Tamanho (GB) |
| ------------------------------- | ------------ | ------------------------------- |
| oLLama-7B                       | 7 bilhões    | 13                              |
| oLLama-3B                       | 3 bilhões    | 6                               |
| oLLama-1B                       | 1 bilhão     | 2                               |
| oLLama-500M                     | 500 milhões  | 1                               |
| oLLama-300M                     | 300 milhões  | 0,6                             |
| Llama2-7B                       | 7 bilhões    | 13                              |
| Llama2-13B                      | 13 bilhões   | 26                              |
| Phi-3 Mini                      | 3 bilhões    | 3.8             |
| Phi-3 Medium                    | 14 bilhões   | 15                              |
| Orca Mini                       | 7 bilhões    | 13                              |
| Solar                           | 10,7 bilhões | 6,1-21                          |
| Gemma-2B                        | 2 bilhões    | 3.5             |
| Gemma-7B                        | 7 bilhões    | 11.5            |
| LLaVA-7B                        | 7 bilhões    | 5.5             |
| LLaVA-13B                       | 13 bilhões   | 17                              |
| StarCoder-7B                    | 7 bilhões    | 15                              |
| CodeLlama-7B                    | 7 bilhões    | 13                              |
| Dolphin-2.2-70B | 70 bilhões   | 28                              |
| Magicoder-7B                    | 7 bilhões    | 10.5            |

Você pode baixar e executar qualquer um desses modelos no seu Raspberry Pi abrindo o terminal e digitando:

```bash
ollama run [nome do modelo]
```

Por exemplo, para executar `gemma:2b`, digite:

```bash
ollama run gemma:2b
```

\--- /collapse ---
