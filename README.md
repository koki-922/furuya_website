# Furuya Website

Flask-based book store management web application.

## 📚 プロジェクト概要

古代書店管理アプリケーション。書籍の入荷情報を管理し、一覧表示・登録ができるシンプルなWebアプリケーションです。

## ✨ 機能

- 📖 入荷書籍の一覧表示
- ➕ 新刊情報の登録
- 💾 SQLite3を使用したデータベース管理

## 🛠️ 技術スタック

- **Framework**: Flask（Python）
- **Database**: SQLite3
- **Template Engine**: Jinja2
- **Frontend**: HTML

## 📂 ファイル構成

```
flaskr/
├── __init__.py           # Flask アプリケーション初期化
├── main.py              # ルート定義とビューロジック
├── db.py                # データベース初期化
└── templates/
    ├── index.html       # 入荷情報表示ページ
    └── form.html        # 情報登録フォーム
```

## 🚀 実行方法

### 環境構築

```bash
pip install flask
```

### アプリケーション実行

```bash
export FLASK_APP=flaskr
flask run
```

その後、ブラウザで `http://localhost:5000` にアクセスしてください。

## 📖 使い方

1. **入荷情報確認**: トップページで登録済みの書籍一覧を確認
2. **新刊登録**: 「編集」リンクをクリックしてフォームから新刊情報を登録
   - 入荷日: 書籍の入荷予定日
   - タイトル: 書籍のタイトル
   - 金額: 書籍の販売価格

## 📝 License

MIT License

---

Created by koki-922