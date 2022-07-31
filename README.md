# Thermo-hygrometer

## 構成

```uml
esp32 -> spreadsheet: 室温と湿度と気圧をPOST

SlackBot <- User: 何度を含む文字列の書き込み
SlackBot -> spreadsheet: 室温等要求

spreadsheet --> SlackBot: データが存在する最終行を返却
SlackBot --> User: 室温と湿度と気圧の書き込み
```

## How to
### esp32
esp32ブランチからArduinoIDEなどからコンパイルして書き込み

### spreadsheet
空白のシートを作成して，拡張機能のAppからエディタを開く
それぞれをウェブアプリとしてデプロイ

### SlackBot
ボットを作成してチャンネルに追加してコードを実行

### User
対象のチャンネルで"何度"を含む文字列を書き込み