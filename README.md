# News Text-to-Speech Discord Bot

A discord bot that automatically generates news videos with text-to-speech narration using Remotion and cloud services.

https://github.com/user-attachments/assets/338ca59c-379b-45be-a809-8761e85857c7


This project fetches news articles, generates concise summaries using GPT-3.5, and converts them to speech using Google Cloud Text-to-Speech. The output includes both text summaries and audio files stored in Google Cloud Storage.

## Features

- Fetches news articles from URLs using NewsPlease
- Generates concise summaries using OpenAI's GPT-3.5
- Converts summaries to speech using Google Cloud Text-to-Speech
- Stores audio files in Google Cloud Storage
- Generates a JSON file containing summaries, emojis, and audio URLs

## Project Structure

- `demo-v/` - Demo video project using Remotion with TTS integration
- `my-video/` - Base video template project using Remotion
- `*.py` - Python scripts for news processing and TTS generation


## Prerequisites

- Node.js & npm
- Python 3.8+
- Google Cloud account with Text-to-Speech API enabled
- AWS account with S3 bucket configured
- Azure account with Speech Services

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install google-cloud-texttospeech
pip install google-cloud-storage
pip install news-please
pip install openai
pip install requests
cd demo-v
npm install
cd ../my-video
npm install
```

4. Set up environment variables:
- Copy `.env.example` to `.env` in demo-v directory
- Add your cloud service credentials:
  - Azure TTS credentials
  - AWS S3 credentials
  - Google Cloud credentials


## Usage

1. To process news articles and generate audio files:
```bash
python DataGenerator.py
```

2. The script will:
   - Fetch and analyze the news articles
   - Generate summaries using GPT-3.5
   - Convert summaries to speech
   - Store audio files in Google Cloud Storage
   - Generate a JSON file with all the data

3. Preview video:
```
bash
cd demo-v
npm start
```

4. Render video:
```
bash
npm run build
```


## Architecture

- `NewsAbstractor.py` - Extracts news summaries using OpenAI GPT
- `TextToSpeech.py` - Converts text to speech using Google Cloud TTS
- `DataGenerator.py` - Orchestrates the news processing pipeline
- `demo-v/` - Remotion video project with TTS integration
- `my-video/` - Base Remotion video template

## License

Notice that for some entities a company license is needed. Read [the Remotion license terms](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md).
