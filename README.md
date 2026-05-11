<<<<<<< HEAD
# ローカルAIアプリ プロジェクト

## ディレクトリ構成

```
local-ai-project/
├── 01_main/                    # メインシステム
│   ├── docker-compose.yml      # Docker全体構成
│   ├── .env                    # 環境変数
│   ├── fastapi/                # 制御サーバー
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── app/
│   │   │   ├── main.py         # エントリーポイント
│   │   │   ├── router.py       # ルーティング判定
│   │   │   ├── config.py       # 設定管理
│   │   │   └── models.py       # データモデル定義
│   │   └── routing_rules.json  # 振り分けルール
│   ├── phi3/                   # 会話AI（CPU）
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── app/
│   │       └── main.py
│   ├── qwen/                   # 生成AI（GPU）
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── app/
│   │       └── main.py
│   └── unity/                  # Unityプロジェクト（別途管理）
│       └── README.md
│
├── 02_logs/                    # ログ・会話履歴
│   ├── chroma_db/              # ChromaDB永続化データ
│   ├── conversations/          # 会話ログ（JSON）
│   └── system/                 # システムログ
│
└── 03_models/                  # AIモデル保存場所
    ├── phi3/                   # Phi3モデルファイル
    └── qwen/                   # Qwenモデルファイル
```

## セットアップ手順

1. `03_models/` にモデルファイルを配置
2. `01_main/.env` を自分の環境に合わせて編集
3. `cd 01_main && docker-compose up -d`
=======
# Project Overview

This project aims to create an AI system integrated with Unity, providing engaging and intelligent interactions in gameplay.

## Setup Instructions

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/kamisama0109/local-ai-unity-system.git
   cd local-ai-unity-system
   ```  

2. **Install Dependencies**:  
   Make sure to have Unity installed. Check the required version in the repository.
   
3. **Open the Project in Unity**:  
   Launch Unity Hub, click on 'Add', and navigate to the project folder.

4. **Configure Settings**:  
   Adjust settings under `Edit > Project Settings` to match your desired specifications.

5. **Run the Project**:  
   Click the Play button in the Unity editor to start using the AI system.

Feel free to contribute and make improvements!
>>>>>>> c295019a0cc828d6f5fb63c42f22af5732252b2e
