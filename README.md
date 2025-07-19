# 🛉 File Organizer 

This simple Python script automatically organizes the files in a specified folder (like your **Downloads** folder) into categorized subfolders based on file types — such as Images, Documents, Videos, and more.

## 📂 What It Does

The script:

* Scans all files in a given folder.
* Detects each file's extension (e.g., `.jpg`, `.pdf`, `.mp4`).
* Moves each file into a new subfolder based on its type:

  * `Images` → `.jpg`, `.png`, etc.
  * `Documents` → `.pdf`, `.txt`, etc.
  * `Videos`, `Audio`, `Archives`, `Scripts`
* Puts unrecognized file types into a folder called `Others`.

### Example Output Folder Structure

```
/Downloads
  ├— Images
  │     └— photo.jpg
  ├— Documents
  │     └— resume.pdf
  └— Others
        └— unknownfile.xyz
```

---

## ▶️ How to Run

### 1. 🐍 Requirements

* Python 3.x
* No additional packages required (uses built-in `os` and `shutil`)

### 2. 📁 Navigate to the Project Folder

Open your terminal or command prompt and navigate to the folder where the script file is located:

```bash
cd path/to/your/project-folder
```

> 💡 Replace `path/to/your/project-folder` with the actual path to the folder containing `organize_folder.py`.

### 3. 🔧 Set the Folder You Want to Organize

Open the script and update this line:

```python
FOLDER_TO_ORGANIZE = "/Users/yourusername/Downloads"
```

Replace it with the absolute path of the folder you want to organize.

### 4. 🚀 Run the Script

Once inside the project folder, run:

```bash
python organize_folder.py
```

The script will sort your files into subfolders like `Images`, `Documents`, `Others`, etc., based on file type.

---

## ✮ Customization

Want to support more file types?
Just update the `FILE_TYPES` dictionary in the script:

```python
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx"],
    # Add your own here!
}
```

---

## 📌 License

This script is free to use and modify for personal or educational purposes.
