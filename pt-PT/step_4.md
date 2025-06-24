<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/xx0VQ0RJc8A?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div>
</html>

## Usar a WebUI

A WebUI funciona como qualquer outra interface de chatbot. Podes escrever os teus prompts e ver as respostas gerados pelo modelo.

![Uma captura de tela de uma interface de IA a exibir um design limpo e minimalista. O texto "Olá, Sr. C" é apresentado com destaque no centro. Abaixo, há uma barra de pesquisa rotulada "Como posso ajudá-lo hoje?" com um ícone de microfone e áudio à direita. Os prompts sugeridos incluem "Conta-me um facto divertido sobre o Império Romano", "Mostra-me um trecho de um código do cabeçalho fixo de um site" e "Dá-me ideias sobre o que fazer com a arte dos meus filhos". No lado esquerdo, há um menu de opções para "Área de Trabalho", "Pesquisa" e "Chats". Um ícone circular rotulado com "M" que está no canto superior direito.](images/webUI.png)

### Instalar o Docker e a WebUI

--- task ---

Instalas o Docker ao inserir o seguinte comando no terminal:

```bash
sudo apt install docker.io
```

Espera que o Docker instale. Saberás que a instalação foi concluída quando o prompt do terminal retornar.

--- /task ---

--- task ---

Instala WebUI ao copiar e colar o seguinte comando no terminal:

```bash
sudo docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

Espera que o WebUI instale. Saberás que a instalação foi concluída quando o prompt do terminal retornar.

--- /task ---

--- task ---

Acede à interface WebUI ao navegar para `http://localhost:3000/` no teu navegador.

![Um separador do navegador intitulado "Abrir WebUI" mostra o URL "localhost:3000" na barra de endereço.](images/localhostURL.png)

--- /task ---
