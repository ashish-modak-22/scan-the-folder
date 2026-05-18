# 📁 Folder Snapshot System

A Python-based file integrity monitoring tool that creates and compares folder snapshots using SHA-256 hashing.

This project helps detect changes inside a folder by generating unique cryptographic hashes for every file and comparing them over time.

It can identify:

- ✅ Modified files
- ➕ Newly added files
- ❌ Deleted files

---

# 🚀 Features

- SHA-256 file hashing
- Folder snapshot creation
- JSON-based snapshot storage
- File integrity comparison
- Detects:
  - Modified files
  - New files
  - Deleted files
- Efficient chunk-based file reading
- Lightweight and beginner-friendly

---

# 🛠 Technologies Used

- Python
- hashlib
- json
- os

---

# 📂 Project Structure

```bash
project/
│
├── main.py
├── snapshot.json
│
└── my_folder/
     ├── file1.txt
     ├── file2.txt
