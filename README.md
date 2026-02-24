# 017_TodoManager

## 属性

title(str)
deadline(detetime)
completed(bool)


## ReactPython と連携する
- React（フロント）
- FastAPI / Flask（バックエンド）
- fetch で通信

## React起動手順
- backend 起動
cd backend
uvicorn main:app --reload

- frontend 起動
cd ../frontend
npm run dev