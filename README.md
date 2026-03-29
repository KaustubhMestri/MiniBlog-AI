# 🚀 MiniBlog AI
**MiniBlog AI** is an AI-powered content generation system built using **CrewAI**. It takes a user-provided topic and automatically generates a short, simple, and well-structured blog post using a multi-agent workflow.

## Overview
MiniBlog AI demonstrates how multiple AI agents can collaborate to transform raw user input into meaningful, beginner-friendly content. A Report Generator Agent first analyzes the topic, then a Blog Writer Agent converts it into a clean, readable blog — all fully automated using CrewAI's agentic framework.

## Key Features
- Multi-agent architecture using CrewAI for structured content generation
- Converts any user-provided topic into a beginner-friendly blog post
- Automated end-to-end content creation pipeline
- Agent roles and tasks defined via clean YAML configuration
- Output saved directly to `blogs/blog.md`

## Tech Stack
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/CrewAI-F55036?style=for-the-badge&logo=crewai&logoColor=white" alt="CrewAI"/>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI"/>
  <img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge&logo=groq&logoColor=white" alt="Groq"/>
  <img src="https://img.shields.io/badge/LiteLLM-000000?style=for-the-badge&logo=literalai&logoColor=white" alt="LiteLLM"/>
  <img src="https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white" alt="YAML"/>
</p>

## Installation

Install:
- **Git**: [Download](https://git-scm.com/download/win)
- **Python 3.10–3.13**: [Download](https://www.python.org/downloads/)
- **UV** (dependency manager):
  ```bash
  pip install uv
  ```

### Clone Repository
1. Open CLI.
2. Run:
   ```bash
   git clone https://github.com/KaustubhMestri/MiniBlog-AI
   cd MiniBlog-AI
   ```

### Install Dependencies
```bash
crewai install
```

### Set Up `.env`
Create a `.env` file in the root directory and add your API key:
```env
MODEL = your_model_name
GORQAI_API_KEY=your_api_key_here
```

> Supports OpenAI or Groq (via LiteLLM). Replace the key accordingly.

### Run the Project
```bash
crewai run
```

The generated blog will be saved at:
```
blogs/blog.md
```

## How It Works
1. User provides a topic as input
2. **Report Generator Agent** analyzes the topic and generates structured information
3. **Blog Writer Agent** converts the report into a simple, readable blog post
4. Final output is saved to `blogs/blog.md`

## Contributing
1. Create an [issue](https://github.com/KaustubhMestri/MiniBlog-AI/issues).
2. Branch: `feature/<n>` or `bugfix/<n>`
   ```bash
   git checkout -b feature/<n>
   ```
3. Commit:
   ```bash
   git add .
   git commit -m "#<issue> message"
   ```
4. Push:
   ```bash
   git push origin feature/<n>
   ```
5. Submit PR to `main`.

## Resources
- CrewAI Docs: https://docs.crewai.com
- CrewAI GitHub: https://github.com/joaomdmoura/crewai

## License
MIT License. See [LICENSE](LICENSE).
