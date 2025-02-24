# Assignment #1 Development of a RAG App

Arnav Joshi's submission for Assignment #1 of INFO 5940.

---

## 🛠️ Prerequisites

Before starting, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started) (Ensure Docker Desktop is running)
- [VS Code](https://code.visualstudio.com/)
- [VS Code Remote - Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Git](https://git-scm.com/)
- OpenAI API Key

---

## 🚀 Setup Guide

The installation for this assignment should be nearly identical to cloning and setting up the repository straight from GitHub. However, due to minor issues in the setup that currently exist in the repository (and some inefficiencies), the instructions are in a different order and slightly modified.

---

### 1️⃣ Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/joshiarnav/INFO5940-A1.git
cd INFO5940-A1
```

### 2️⃣ Configure OpenAI API Key

Since `docker-compose.yml` expects environment variables, follow these steps:

#### ➤ Option 1: Set the API Key in `.env` (Recommended)

1. Inside the project folder, create a `.env` file:

   ```pwsh
   ni .env
   ```

   or for Mac:

   ```bash
   touch .env
   ```

2. Add your API key and base URL:

   ```plaintext
   OPENAI_API_KEY=your-api-key-here
   OPENAI_BASE_URL=https://api.ai.it.cornell.edu/
   TZ=America/New_York
   ```

Now, your API key will be automatically loaded inside the container.

### 3️⃣ Open in VS Code with Docker

1. Open **VS Code**, navigate to the `INFO5940-A1` folder.
2. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and search for:
   ```
   Dev Containers: Rebuild and Reopen in Container
   ```
3. Select this option. VS Code will build and open the project inside the container.

📌 **Note:** If you don’t see this option, ensure that the **Dev Containers** extension is installed.

### 4️⃣ Run Streamlit App

1. Navigate to the `INFO5940-A1` folder.
2. Run:
   ```bash
   streamlit run advanced_chat.py
   ```
3. Open a browser and navigate to `http://localhost:8501` (or the port number shown in the terminal if different).
4. Upload and chat! Supports PDFs and text files (plural) and utilizes FAISS for vectorization, vector store, and vector similarity search. Utilizes OpenAI's Embeddings (to create vector embeddings) and LLMs (for chat).

---

## 📌 Changes Made

- Deleted old poetry.lock file (there was a dependency error on all tested machines in the existing `poetry.lock` file in the [lecture-05 branch of INFO-5940](https://github.com/AyhamB/INFO-5940/tree/lecture-05)).
- Added faiss-cpu package to the poetry packages (`poetry add faiss-cpu`).
- Added PyPDF2 package to the poetry packages (`poetry add PyPDF2`).
- Deleted any extraneous folders/files for the assignment:
  - `/notebooks`
  - `/data`
  - `chat_with_pdf.py`
  - `chat_with_rag.py`
  - `Chatbot.py`
  - `poetry.lock` (explained above)
  - Old `README.md`
  - `summary.py`
  - `tokens.py`
- Modified `README.md`:
  - Modified name of the extension for **Dev Containers** (`Dev Containers: Rebuild and Reopen in Container`). The original instructions in the [lecture-05 branch of INFO-5940](https://github.com/AyhamB/INFO-5940/tree/lecture-05) were for **Remote - Containers** which is deprecated.
  - Moved API key setup before starting the container (this avoids rebuilding the container to add the API key).

---

## 📄 Sources

- Course Material ([lecture-05 branch of INFO-5940](https://github.com/AyhamB/INFO-5940/tree/lecture-05))
- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [OpenAI Platform Page](https://platform.openai.com/docs/guides/embeddings)

---

## 🛠️ Troubleshooting

### **Container Fails to Start?**

- Ensure **Docker Desktop is running**.
- Run `docker-compose up --build` again.
- If errors persist, delete existing containers with:

  ```bash
  docker-compose down
  ```

  Then restart:

  ```bash
  docker-compose up --build
  ```

### **Cannot Access Jupyter Notebook from outside VS Code?**

- Ensure you’re using the correct port (`8888`).
- Run `docker ps` to check if the container is running.

### **OpenAI API Key Not Recognized?**

- Check if `.env` is correctly created.
- Ensure `docker-compose.yml` includes `env_file: - .env`.
- Restart the container after making changes (`docker-compose up --build`).

---
