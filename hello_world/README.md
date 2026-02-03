# 設定例
claude_desktop_config.jsonにいかを追加。
```
   "postgres-mcp": {
      "command": "wsl.exe",
      "args": [
        "/usr/bin/docker",
        "run",
        "-i",
        "--rm",
        "-e",
        "DATABASE_URI=postgresql://postgres:postgres@localhost:5432/gis_db",
        "crystaldba/postgres-mcp",
        "--access-mode=unrestricted"
      ],
      "env": {
        "DATABASE_URI": "postgresql://postgres:postgres@localhost:5432/gis_db"
      }
    },
```