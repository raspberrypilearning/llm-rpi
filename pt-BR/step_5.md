<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/3MlalSPu1gI?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div><br><br>
</html>

## Reconhecimento de imagem com WebUI

Para usar o Ollama, você deve baixar um modelo para usar. Anteriormente, você usou o modelo apenas de texto `gema:2b`, mas nesta etapa você usará o modelo de análise de imagem chamado `LLaVa`.

\--- task ---

Para baixar o modelo LLaVA, acesse a interface web em `http://localhost:3000`.

\--- /task ---

\--- task ---

Cadastre-se no Ollama WebUI.

Ao usar WebUI pela primeira vez, você será solicitado a fornecer um nome, e-mail e senha. Você pode usar qualquer endereço de e-mail fictício para isso; é apenas para uso local no seu Raspberry Pi.

![Um formulário de inscrição para "Open WebUI" com campos para nome, e-mail e senha. O campo de nome está preenchido com "Sr. C", o campo de e-mail com "teste@qualquercoisa.com" e o campo de senha exibe uma série de pontos indicando uma senha oculta. Abaixo desses campos, há um botão "Criar conta" com um cursor apontando para ele e um link para usuários que já possuem uma conta fazerem login.](images/webUI_signup.png)

\--- /task ---

\--- task ---

Escolha qual modelo usar no menu colapsante na parte superior da interface do site. Você também pode pesquisar e adicionar novos modelos desta forma — digite `llava:latest` na pesquisa e escolha `Obter llava:latest de Ollama.com`. Seu modelo começará a ser baixado.

![Um menu colapsante com o título "Selecionar um modelo" mostra um campo de busca com o texto "llava:latest" inserido. Abaixo do campo de pesquisa, é exibido o texto "Nenhum resultado encontrado", seguido por uma opção selecionável para "Obter 'llava:latest' de Ollama.com". Um cursor está sobre esta opção.](images/model_dropdown.png)

\--- /task ---

\--- task ---

Espere o modelo instalar e verifique. Isto pode demorar um pouco.

\--- /task ---

### Use LLaVa para analisar uma imagem

<html>
<br><br>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/ruU6KsVyxKA?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div><br><br>
</html>

\--- task ---

Assim que o modelo LLaVA for baixado, inicie uma nova sessão selecionando o modelo entre as opções disponíveis.

![Captura de tela mostrando o menu de seleção de modelo com "llava:latest 7B" realçado.](images/select_llava_model.png)

\--- /task ---

\--- task ---

Envie uma imagem usando o botão "Enviar Imagem".
![Um elemento de interface de usuário com dois botões: "Enviar Arquivos" no topo com um ícone de documento, e um botão "Enviar uma mensagem" abaixo dela, que é cinza e inclui um símbolo de mais. Um cursor está apontando para o símbolo de mais no botão "Enviar uma mensagem".](images/upload_image.png)

\--- /task ---

\--- task ---

Após o envio, insira um prompt ou pergunta sobre a imagem na caixa de bate-papo. Pressione <kbd>Enter</kbd>.

![Uma pequena imagem de um gato laranja fofo com um peito branco e um arco rosa em torno do pescoço. O gato está olhando diretamente para a câmera com uma expressão de curiosidade. Ao lado da imagem, há um símbolo de adição e o texto "Descreva esta imagem".](images/cat_prompt.png)

\--- /task ---

\--- task ---

Revise a descrição ou análise gerada pelo modelo LLaVA. Você pode fazer mais perguntas ou fazer o envio de imagens adicionais.

Usando esta imagem:
![A imagem mostra um close-up de um gato doméstico de pelo curto com olhos grandes e marcantes e uma expressão atenta. O gato tem uma pelagem macia, predominantemente em tons de creme e branco, com manchas mais escuras no rosto, orelhas e patas. Parece estar sentado ou deitado, com as patas da frente ligeiramente estendidas em direção ao espectador. O rabo do gato está enrolado junto ao corpo. Atrás do gato, há um buquê de flores de lavanda, que adiciona um toque de cor e textura à imagem. No lado esquerdo da foto, há um tom roxo, sugerindo uma parede ou fundo azul. Em primeiro plano, pode-se ver uma superfície de madeira, possivelmente uma mesa ou um balcão, com algumas ervas colocadas em um recipiente no canto superior direito. O estilo geral da imagem é realista, com foco nos detalhes e uma profundidade de campo rasa que destaca as características do gato.](images/cat.jpg)

LLaVa forneceu esta descrição:

`A imagem mostra um close-up de um gato doméstico de pelo curto com olhos grandes e marcantes e uma expressão atenta. O gato tem uma pelagem macia, predominantemente em tons de creme e branco, com manchas mais escuras no rosto, orelhas e patas. Parece estar sentado ou deitado, com as patas da frente ligeiramente estendidas em direção ao espectador. O rabo do gato está enrolado junto ao corpo. Atrás do gato, há um buquê de flores de lavanda, que adiciona um toque de cor e textura à imagem. No lado esquerdo da foto, há um tom roxo, sugerindo uma parede ou fundo azul. Em primeiro plano, pode-se ver uma superfície de madeira, possivelmente uma mesa ou um balcão, com algumas ervas colocadas em um recipiente no canto superior direito. O estilo geral da imagem é realista, com foco nos detalhes e uma profundidade de campo rasa que destaca as características do gato.`

\--- /task ---
