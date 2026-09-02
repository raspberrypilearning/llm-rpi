<iframe width="560" height="315" src="https://www.youtube.com/embed/xx0VQ0RJc8A?si=MeRR763nVpucx5d8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Usando a WebUI

A WebUI funciona como qualquer outra interface de chatbot. Você pode digitar os seus prompts e ver as respostas geradas pelo modelo.

![Uma captura de tela de uma interface de IA exibindo um design limpo e minimalista.] O texto "Olá, Sr. C" aparece em destaque no centro. Abaixo, há uma barra de pesquisa rotulada "Como posso ajudá-lo hoje?", com um ícone de microfone e áudio à direita. Os prompts sugeridos incluem "Conte-me uma curiosidade sobre o Império Romano", "Mostre-me um trecho de código do cabeçalho de um site" e "Dê-me ideias do que fazer com os desenhos dos meus filhos". No lado esquerdo, há um menu com opções para "Área de Trabalho", "Busca" e "Chats." Um ícone de perfil circular rotulado "M" está no canto superior direito.](images/webUI.png)

### Instalar o Docker e a WebUI

\--- task ---

Instale o Docker digitando o seguinte comando no terminal:

```bash
sudo apt install docker.io
```

Aguarde a instalação do Docker. Você saberá que a instalação foi concluída quando o prompt do terminal retornar.

\--- /task ---

\--- task ---

Instale a WebUI copiando e colando o seguinte comando no terminal:

```bash
sudo docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

Aguarde a instalação da WebUI. Você saberá que a instalação foi concluída quando o prompt do terminal retornar.

\--- /task ---

\--- task ---

Acesse a interface WebUI navegando para `http://localhost:3000/` em seu navegador.

![Uma aba do navegador intitulada "Abrir WebUI" mostra o URL "localhost:3000" na barra de endereços.](images/localhostURL.png)

\--- /task ---
