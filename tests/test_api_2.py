import requests

# Test VS Code question
def test_vscode_question():
    url = "http://127.0.0.1:8000/api"
    question = "Install and run Visual Studio Code. In your Terminal (or Command Prompt), type `code -s` and press Enter. Copy and paste the *entire output* below."
    
    response = requests.post(
        url,
        data={"question": question}
    )
    
    print("VS Code Question Response:")
    print(response.json())

# Test uv question
def test_uv_question():
    url = "http://127.0.0.1:8000/api/"
    question = "Send a HTTPS request to `https://httpbin.org/get` with the URL encoded parameter `email` set to `23f3001208@ds.study.iitm.ac.in`\nWhat is the JSON output of the command? (Paste only the JSON body, not the headers)"
    
    response = requests.post(
        url,
        data={"question": question}
    )
    
    print("UV Question Response:")
    print(response.json())

# Test npx prettier question
def test_npx_prettier_question():
    url = "http://127.0.0.1:8000/api/"
    question = "Download README.md. In the directory where you downloaded it, make sure it is called README.md, and run npx -y prettier@3.4.2 README.md | sha256sum. What is the output of the command?"
    
    # Send the file from the current working directory as multipart form-data
    with open("README.md", "rb") as file:
        response = requests.post(
            url,
            data={"question": question},
            files={"file": ("README.md", file, "text/markdown")}
        )
    
    print("NPX Prettier Question Response:")
    print(response.json())

if __name__ == "__main__":
    test_vscode_question()
    test_uv_question()
    test_npx_prettier_question()