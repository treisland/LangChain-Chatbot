# LangChain - ChatBot

## Description
The purpose of this project is to create a chatbot that can be used to communicate with the user in a natural language

## Requirements
- Python 3.12.0 or higher
- pip 23.2.1 or higher

## (Optional) Python Virtual Environment
It is recommended to use a virtual environment to manage the dependencies of the project.

This will allow you to install the dependencies without affecting the global python installation.

To create a virtual environment, run the following command:

 ```
 python -m pip install virtualenv
 python -m venv .env
 ```

## Ollama Installation
This repository uses the Ollama library to create the chatbot.

1. Install based on your OS https://ollama.com/
2. Install a language model and automatically run it
   ```
   #syntax: ollama run <model name>
   
   ollama run llama2
   ```

## (Optional) WSL changes needed for external access
If you are using WSL, you will need to make some changes to the Ollama installation to make accessible outside the WSL environment.

1. Open the Ollama service file
   ```
   sudo vim /etc/systemd/system/ollama.service
   ``` 
2. Locate the **[Service]** section and then **Environment**.

   At the end of the line set the **OLLAMA_HOST** variable to listen on all interfaces. 

   ```
   Environment=<...> "OLLAMA_HOST=0.0.0.0"
   ```

3. Reload the system services
   ```
   sudo systemctl daemon-reload
   ```
4. Restart the Ollama service
   ```
    sudo systemctl restart ollama
    ```

5. Get your WSL ip address
   ```
   ip addr show eth0
   ```

6. Open powershell in administrator mode and run the following command to open the port
   ```
   netsh interface portproxy add v4tov4 listenport=11434 connectport=11434 connectaddress=<WSL_IP>
   ```
   
## Verify Ollama Service is Running
Open a web browser and navigate one of the following URLs:

- http://localhost:11434

- http://<WSL_IP>:11434
--- 

## Project Setup
1. Clone the repository.
2. Install dependencies using requirements.txt
   ```
   pip install -r requirements.txt
   ```
3. In the root of the project, create a file called **.env** and add the following environment variables:

   *Note: replace <IP> with the IP address of the Ollama service*

   ```
   OLLAMA_URL=http://<IP>:11434
   ```

4. Run the test file to verify your code can communicate with the Ollama service
   ```
   python hello_ollama.py
   ```