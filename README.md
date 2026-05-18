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
```

------------------------------


# 📦 Installation & Setup

 1️⃣ Clone Repository

```bash
git clone https://github.com/ashish-modak-22/Folder_SnapShot_System.git
```

---

## 2️⃣ Move Into Project Folder

```bash
cd <project-folder>
```

---

## 3️⃣ Create Virtual Environment (Optional but Recommended)

### Windows

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### CMD

```bash
venv\Scripts\activate
```

### PowerShell

```bash
.\venv\Scripts\Activate.ps1
```

---

## 5️⃣ No External Libraries Required

This project only uses Python built-in modules:

- os
- json
- hashlib

So no additional `pip install` commands are needed.

---

# ▶️ Run The Program

```bash
python main.py
```
