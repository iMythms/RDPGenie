# RDPGenie

**RDPGenie** is a lightweight Streamlit web app that converts PAM-generated `.sh` session files (which contain `rdesktop` commands) into compatible `.rdp` configuration files for use with **Microsoft Remote Desktop** on macOS.

---

## 🧠 Why?

In some organizations, remote desktop sessions are delivered through auto-generated `.sh` scripts that launch `rdesktop` — a tool that's not natively supported on macOS. RDPGenie solves this by parsing the shell script and generating a `.rdp` file that you can use directly with the official Microsoft Remote Desktop app.

---

## ✅ Features

- Drag and drop `.sh` file upload
- Automatic parsing of `rdesktop` commands
- Converts to clean `.rdp` config
- Automatically names the output file using session metadata
- Downloadable `.rdp` file in one click
- Fully runs in browser via Streamlit

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/RDPGenie.git
cd RDPGenie
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 📄 Example Input

A typical `.sh` file might contain:

```sh
#!/bin/sh
rdesktop -u 'john.doe@domain:RDP_1:Project_Session:john.doe' '10.0.0.5:3389' -N -f -a 32 -x 0x80 -r clipboard:CLIPBOARD
```

**RDPGenie** will convert this to:

```ini
full address:s:10.0.0.5:3389
username:s:john.doe@domain:RDP_1:Project_Session:john.doe
prompt for credentials:i:1
authentication level:i:2
redirectclipboard:i:1
screen mode id:i:2
desktopwidth:i:1920
desktopheight:i:1080
session bpp:i:32
```

---

## 📦 Folder Structure

```
RDPGenie/
├── app.py
├── requirements.txt
└── README.md
```

---

## 🪄 Credit

Built with ❤️ by Maitham Jasim  
Feel free to use, modify, or contribute.

---

## 📘 License

This project is open-source and available under the MIT License.
