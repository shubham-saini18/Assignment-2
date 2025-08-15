# 🐍 Python Basics for DevOps Engineers

> **Author:** Shubham Saini  
> **Date:** August 15, 2025

Welcome to the **Python Basics for DevOps Engineers** repository!  
This collection features four beginner-friendly Python scripts designed to introduce essential programming concepts for DevOps automation, configuration management, and file handling.

---

## 📑 Table of Contents

1. [Scripts Overview](#scripts-overview)
2. [How to Run](#how-to-run)
3. [Example Usage](#example-usage)
4. [DevOps Relevance](#devops-relevance)
5. [License](#license)

---

## 📂 Scripts Overview

| Script                  | Description                                                                 | Key Concepts                |
|-------------------------|-----------------------------------------------------------------------------|-----------------------------|
| `grade_checker.py`      | Calculates grade based on numeric score.                                    | Conditional logic           |
| `student_grades.py`     | Menu-driven student grades manager.                                         | Dictionaries, CRUD, loops   |
| `write_file.py`         | Writes sample content to a file.                                            | File handling, context mgr. |
| `read_file.py`          | Reads and prints file content with error handling.                          | Exception handling          |

---

### 1️⃣ Grade Checker (`grade_checker.py`)
- **Input:** Numeric score (0–100)
- **Output:** Prints grade (`A`, `B`, `C`, `D`, `F`)
- **Logic:** Uses `if-elif-else` conditions for grading.

---

### 2️⃣ Student Grades Manager (`student_grades.py`)
- **Features:**  
  - Add new student  
  - Update grades  
  - Display all records  
  - Exit program
- **Concepts:** CRUD operations, dictionaries, loops, menu-driven interface.

---

### 3️⃣ Write to a File (`write_file.py`)
- **Action:** Creates a file and writes sample content.
- **Concepts:** File handling (`open()`), context managers.

---

### 4️⃣ Read from a File (`read_file.py`)
- **Action:** Reads content from file, handles missing file errors.
- **Concepts:** File reading, exception handling (`try-except`).

---

## 🚀 How to Run

### Prerequisites
- **Python 3.x** installed
- Terminal (Linux/Mac) or Command Prompt/PowerShell (Windows)

### Steps
1. **Clone or download** this repository.
2. **Navigate** to the directory:
    ```bash
    cd python-devops-basics
    ```
3. **Run any script:**
    - Linux/Mac:
      ```bash
      python3 script_name.py
      ```
    - Windows:
      ```powershell
      python script_name.py
      ```

---

## 💡 Example Usage

**Run Grade Checker**
```bash
python3 grade_checker.py
```
**Output:**
```
Enter the score (0-100): 85
Grade: B
```

**Run Student Grades Manager**
```bash
python3 student_grades.py
```
**Output:**
```
Options:
1. Add new student
2. Update student grade
3. Display all grades
4. Exit
```

---

## 🛠 DevOps Relevance

These scripts map directly to common DevOps tasks:

- **Grade Checker:**  
  - Demonstrates conditional logic used in CI/CD validation scripts.
- **Student Grades Manager:**  
  - Shows dictionary operations, similar to managing config maps or inventory data.
- **Write to File / Read from File:**  
  - Essential for log management, configuration generation, and automation tasks.

---

**Feel free to fork, contribute, or use these scripts as building blocks for your DevOps journey!**
