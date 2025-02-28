<div align="center">
    <h1>Marxism and Leninism Chatbot</h1>
</div>

## **Introduction**
This is a chatbot designed to make learning Philosophy Marx-Lenin and Political Economics of Marxism and Leninism easier. It only provides answer in Vietnamese as well as answers to Marxism and Leninism related question. 
<p align="center">
    <img src="assets/web example 1.png" width="48%">
    <img src="assets/web example 2.jpg" width="48%">
</p>

## **Installation**

### **1. Clone the repository:**

```bash
git clone https://github.com/mbyhphat/Marxism-and-Leninism-ChatBot.git
cd Marxism-and-Leninism-ChatBot
```

### **2. Create and activate Conda environment (Recommended):**

    ```bash
    conda create -n ctribot python=3.10 -y
    conda activate ctribot
    ```
    Install the requirements :

    ```bash
    pip install -r requirements.txt
    ```
### **3. Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:**

    ```ini
    PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```
### **4. Run code**

#### If you run the repository for the first time, run the following command to store embeddings to pinecone

     ```bash
    python store_index.py
    ```

#### Run the following command to use the bot

    ```bash
    python app.py
    ```

## Techstack Used:
- Python
- LangChain
- Flask
- GPT
- Pinecone
