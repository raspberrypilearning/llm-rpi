<iframe width="560" height="315" src="https://www.youtube.com/embed/xx0VQ0RJc8A?si=MeRR763nVpucx5d8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## WebUIを使用する

WebUIは他のチャットボットインターフェースと同じように動作します。 プロンプトを入力すると、モデルが生成した応答を確認できます。

![クリーンでミニマルなデザインを表示するAIインターフェースのスクリーンショット。 「Hello, MrC」というテキストが中央に大きく表示されている。 その下には「今日はどのようなご用件でしょうか？」と表示された検索バーがあり、右側にはマイクと音声アイコンが表示されている。 「ローマ帝国に関する面白い事実を教えてください」「ウェブサイトの固定ヘッダーのコードスニペットを見せてください」「子供たちの絵をどう活用すればいいかアイデアを教えてください」というプロンプトが提案されている。 左側には、「ワークスペース」「検索」「チャット」のオプションを含むメニューが表示されている。 右上隅に「M」と表示された円形のプロフィールアイコンがある。](images/webUI.png)

### DockerとWebUIをインストールする

\--- task ---

ターミナルに以下のコマンドを入力してDockerをインストールしてください。

```bash
sudo apt install docker.io
```

Dockerがインストールされるのを待ちます。 ターミナルプロンプトが再び表示されたら、インストールが完了したことがわかります。

\--- /task ---

\--- task ---

ターミナルに以下のコマンドをコピーペーストしてWebUIをインストールしてください。

```bash
sudo docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

WebUIがインストールされるのを待ちます。 ターミナルプロンプトが再び表示されたら、インストールが完了したことがわかります。

\--- /task ---

\--- task ---

ウェブブラウザで`http://localhost:3000/`にアクセスして、WebUIインターフェースを開きます。

![「WebUIを開く」というタイトルのブラウザタブのアドレスバーに「localhost:3000」というURLが表示されている。](images/localhostURL.png)

\--- /task ---
