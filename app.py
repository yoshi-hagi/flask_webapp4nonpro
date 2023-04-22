from flask import Flask, render_template, request
from flask_qrcode import QRcode
import os

# Flaskとflask_qrcodeのインスタンス化
app = Flask(__name__)
qrcode = QRcode(app)

# URIとエンドポイント(URIと紐づけられた関数)を設定
@app.route('/')
def index():
    return render_template('index.html')
    # render_templateでtemplates内で指定されたファイルをテンプレートとして利用できる

@app.route('/qrcode', methods=["GET"])
def get_qrcode():
    data = request.args.get('data', '')
    img = qrcode(data, mode="raw") # 入力した値でQRコードを生成
    # 出力したQRコードを静的ファイルとして利用するためstaticフォルダにpngで保存。
    # Flaskではstaticフォルダに保存する事で、デフォルトで静的ファイルとして利用できる
    file_path = os.path.join('static', 'qrcode.png')
    with open(file_path, 'wb') as f:
        f.write(img.getvalue())
    return render_template('index.html', data=data)
# render_templateでは引数に変数を渡すだけでテンプレート上で変数を使うことが出来る

if __name__ == '__main__':
    app.run(debug=True)