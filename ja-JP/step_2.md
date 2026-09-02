## Raspberry PiにOllamaをインストールする

<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/OwuPZYmbYsg?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div>
</html>

\--- task ---

Raspberry Pi でターミナルウィンドウを開く

まず、ターミナルにアクセスする必要があります。 ターミナルアイコンをクリックするか、`Ctrl + Alt + T`を押すことで、この操作を行うことができます。

![灰色の背景と上部に青いタイトルバーがあり、中央に白いコマンドプロンプトのシンボルがあるターミナルウィンドウのアイコン。](images/terminal.png)

\--- /task ---

\--- task ---

Olamaをインストールします。

以下のシェルスクリプトを使用して、OllamaとWebUIインターフェースをインストールします。

```sh
curl -fsSL https://ollama.com/install.sh | sh
```

このインストールプロセスには時間がかかる場合があります。 ターミナルプロンプトが再び表示されたら、処理が完了したことがわかります。

\--- /task ---
