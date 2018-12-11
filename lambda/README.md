# えもじっく Lambda

## Summary
OpenCVを使って画像から顔認識を行い、😇に変換するスクリプトです。

## Requirements
```bash
pip install -r requrirements.txt
```

## Test
```bash
python detect_face.py [INPUT_FILE]
```

変換後のファイルが同じディレクトリに出力されます。

## How to deploy
1. Serverless Frameworkを使ってデプロイを行います。以下のリンク先を参考に、AWSの秘密鍵の設定が必要です。

[https://serverless.com/framework/docs/providers/aws/guide/credentials/](https://serverless.com/framework/docs/providers/aws/guide/credentials/)

```
npm install -g serverless
npm install --save serverless-python-requirements serverless-prune-plugin
serverless deploy -v
```

2. バイナリを扱うためにAPI Gatewayの設定からバイナリサポートをONにします。
バイナリメディアタイプの追加から`image/jpeg`を追加してください。

3. curlからテスト
```bash
curl -v --request POST -H "Accept: image/jpeg" -H "Content-Type: image/jpeg" --data-binary "@input.jpg" [API_GATEWAY_ENDPINT] > output.jpg

```