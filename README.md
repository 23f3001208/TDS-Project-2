# Assignment Answering API

An API that automatically answers questions from the IIT Madras' Online Degree in Data Science course's graded assignments.

## Features

- Accepts questions via POST requests
- Handles file attachments like ZIP files and README.md
- Returns answers in JSON format
- Deployed to Vercel (or your preferred platform)

## API Usage

### Basic Question

```bash
curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Install and run Visual Studio Code. In your Terminal (or Command Prompt), type `code -s` and press Enter. Copy and paste the *entire output* below."
```

### Question with File Attachment

```bash
curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Let's make sure you know how to use `npx` and `prettier`. Download README.md. In the directory where you downloaded it, make sure it is called `README.md`, and run `npx -y prettier@3.4.2 README.md | sha256sum`. What is the output of the command?" \
  -F "file=@README.md"
```

### Question with ZIP File

```bash
curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the "answer" column of the CSV file?" \
  -F "file=@abcd.zip"
```

The API responds with:

```json
{
  "answer": "The answer to your question"
}
```

## Deployment

1. Fork this repository
2. Connect your fork to Vercel (or your preferred platform)
3. Deploy the application

## Requirements

- Python 3.9+
- Node.js and npm (for npx commands)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
