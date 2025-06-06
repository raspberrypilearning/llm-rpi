<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/3MlalSPu1gI?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div><br><br>
</html>

## Reconhecimento de imagem com WebUI

Para utilizar o Ollama, deves descarregar um modelo para usar. Anteriormente, usaste o modelo `gemma:2b` só de texto, mas nesta etapa vais utilizar o modelo de análise de imagem, chamado `LLaVa`.

\--- task ---

Para descarregar o modelo LLaVA, acede ao WebUI em `http://localhost:3000`.

\--- /task ---

\--- task ---

Regista-te no Ollama WebUI.

Ao utilizar o WebUI pela primeira vez, vai ser-te pedido que forneças um nome, e-mail e palavra-passe. Podes usar qualquer e-mail inventado para este efeito, é apenas para uso local no teu Raspberry Pi.

![Um formulário de cadastro para "Abrir WebUI" com campos para nome, e-mail, e palavra-passe. O campo do nome é preenchido com "Sr. C", o campo de e-mail com "teste@qualquercoisa.com" e o campo palavra-passe mostra uma série de pontos que indicam uma palavra-passe oculta. Debaixo destes campos, há um botão com um cursor apontado para ele e uma ligação para utilizadores que já tenham uma conta criada para entrar.](images/webUI_signup.png)

\--- /task ---

\--- task ---

Escolhe que modelo queres usar do menu suspenso no topo da WebUI. Também podes pesquisar e adicionar novos modelos desta forma — escreves `llava:latest` na pesquisa e escolhes `Pull llava:latest from Ollama.com`. O teu modelo começará a descarregar.

![Um menu suspenso com o título "Selecionar um modelo" mostra um campo de pesquisa com o texto "llava:latest" introduzido. Abaixo do campo de pesquisa, é apresentado o texto "Nenhum resultado encontrado", seguido de uma opção selecionável para "Pull 'llava:latest' do Ollama.com". Um cursor está em cima desta opção.](images/model_dropdown.png)

\--- /task ---

\--- task ---

Espera que o modelo descarregue e verifica-o. Isto pode demorar algum tempo.

\--- /task ---

### Usa LLaVa para analisar uma imagem

<html>
<br><br>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/ruU6KsVyxKA?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div><br><br>
</html>

\--- task ---

Assim que o modelo LLaVA descarregar, inicia uma nova sessão selecionando o modelo entre as opções disponíveis.

![Captura de ecrã que mostra o menu de seleção de modelos com "llava:latest 7B" destacado.](images/select_llava_model.png)

\--- /task ---

\--- task ---

Carrega uma imagem utilizando o botão "Carregar imagem".
![Um elemento da interface do utilizador com dois botões: "Carregar ficheiros" na parte superior com um ícone de documento e um botão "Enviar uma mensagem" por baixo, que está a cinzento e inclui um símbolo de mais. Um cursor aponta para o símbolo de mais no botão "Enviar uma mensagem".](images/upload_image.png)

\--- /task ---

\--- task ---

Após o carregamento, introduza um prompt ou uma pergunta sobre a imagem na caixa de chat. Pressiona <kbd>Enter</kbd>.

![Uma pequena imagem de um gato laranja felpudo com pelo branco no peito e um laço cor-de-rosa em torno do pescoço. O gato olha diretamente para a câmara com uma expressão curiosa. Ao lado da imagem, existe um símbolo de mais e o texto "descreva esta imagem".](images/cat_prompt.png)

\--- /task ---

\--- task ---

Revê a descrição ou análise gerada pelo modelo LLaVA. Podes fazer mais perguntas ou enviar imagens adicionais.

Utilizar esta imagem:
![A imagem mostra um grande plano de um gato doméstico de pelo curto com olhos grandes e marcantes, e uma expressão atenta. O gato tem uma pelagem felpuda, principalmente em tons de creme e branco, com manchas mais escuras na cara, orelhas e patas. Parece estar sentado ou deitado, com as patas da frente ligeiramente estendidas em direção ao espetador. O rabo do gato está enrolado no seu corpo. Atrás do gato está um ramo de flores de lavanda, acrescentando um toque de cor e textura à imagem. No lado esquerdo da foto, há um tom roxo, sugerindo uma parede azul ou um fundo. Em primeiro plano, uma superfície de madeira pode ser vista, possivelmente uma mesa ou um balcão, com algumas ervas colocadas num recipiente no canto superior direito. O estilo geral da imagem é realista com foco em detalhes e com uma reduzida profundidade de campo que destaca as características do gato. (images/cat.jpg)

LLaVa forneceu esta descrição:

`A imagem mostra um grande plano de um gato doméstico de pelo curto com olhos grandes e marcantes, e uma expressão atenta. O gato tem uma pelagem felpuda, principalmente em tons de creme e branco, com manchas mais escuras na cara, orelhas e patas. Parece estar sentado ou deitado, com as patas da frente ligeiramente estendidas em direção ao espetador. O rabo do gato está enrolado no seu corpo. Atrás do gato está um ramo de flores de lavanda, acrescentando um toque de cor e textura à imagem. No lado esquerdo da foto, há um tom roxo, sugerindo uma parede azul ou um fundo. Em primeiro plano, uma superfície de madeira pode ser vista, possivelmente uma mesa ou um balcão, com algumas ervas colocadas num recipiente no canto superior direito. O estilo geral da imagem é realista com foco em detalhes e com uma reduzida profundidade de campo que destaca as características do gato.`

\--- /task ---
