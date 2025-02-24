# Assignment #1 Development of a RAG App

Arnav Joshi's submission for Assignment #1 of INFO 5940.

---

## Installation:

The installation for this assignment should be identical to cloning and setting up the repository straight from GitHub. Note that the `poetry.lock` file has been modified (explained below), so the run itself will not be identical to the repository, but the setup steps should be.

## 🛠️ Prerequisites  

Before starting, ensure you have the following installed on your system:  

- [Docker](https://www.docker.com/get-started) (Ensure Docker Desktop is running)  
- [VS Code](https://code.visualstudio.com/)  
- [VS Code Remote - Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)  
- [Git](https://git-scm.com/)  
- OpenAI API Key

---

## Changes Made:

- Deleted old poetry.lock file (there was a dependency error on all tested machines in the existing poetry.lock file in the [lecture-05 branch of INFO-5940](https://github.com/AyhamB/INFO-5940/tree/lecture-05)).
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
