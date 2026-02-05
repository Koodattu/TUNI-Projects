# TUNI-Projects

Tampere University course and work projects by [Juha Ala-Rantala](mailto:juha.ala-rantala@tuni.fi).

This monorepo contains coursework from a **Master's degree in Computer Science at Tampere University**, as well as research projects developed as part of [**GPT Lab**](https://gpt-lab.eu/) — an AI research lab founded at Tampere University by Prof. Pekka Abrahamsson, focused on generative AI in software engineering. The work projects fall under [**GPT Lab Seinäjoki**](https://www.tuni.fi/en/research/gpt-lab-seinajoki), a regional initiative bringing AI knowledge and technology to the South Ostrobothnia region, funded by the Regional Council of South Ostrobothnia (AKKE).

---

## Course Projects

| Directory                                                                     | Course      | Description                                                                                                                                                                                           |
| ----------------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [COMP.SE.140-Docker-Compose-exercise](COMP.SE.140-Docker-Compose-exercise/)   | COMP.SE.140 | Docker Compose exercise — multi-service application orchestrated with Docker Compose.                                                                                                                 |
| [COMP.SE.140-nginx-exercise](COMP.SE.140-nginx-exercise/)                     | COMP.SE.140 | Nginx reverse proxy exercise — microservices behind an Nginx gateway with authentication and shutdown services.                                                                                       |
| [COMP.SE.200-Assignment-Part-2](COMP.SE.200-Assignment-Part-2/)               | COMP.SE.200 | Software testing assignment — unit tests with Jest for a JavaScript utility library (lodash-style functions).                                                                                         |
| [ITC.CEE.300-VoiceGuidedImagingReport](ITC.CEE.300-VoiceGuidedImagingReport/) | ITC.CEE.300 | Academic report (LaTeX) — _"Voice-Guided Imaging: Implementation, Challenges, and Lessons Learned Building a Multi-Model AI-Powered Application Using Open-Source Self-Hosted Generative AI Models."_ |

## Work Projects — GPT Lab Seinäjoki

| Directory                                                                   | Description                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [bigcode-evaluation-harness](bigcode-evaluation-harness/)                   | Fork/extension of the [BigCode Evaluation Harness](https://github.com/bigcode-project/bigcode-evaluation-harness) for benchmarking code generation LLMs. Adds custom benchmarking scripts with GPU VRAM monitoring for evaluating models across tasks like HumanEval, MBPP, and MultiPL-E. |
| [gpt-lab-score-keeper](gpt-lab-score-keeper/)                               | Score-keeping web app (React + Material UI frontend, JSON Server backend) containerized with Docker Compose. Used internally at GPT Lab Seinäjoki.                                                                                                                                         |
| [timeless-ucs-code-generator-with-ui](timeless-ucs-code-generator-with-ui/) | AI-agent-powered code generator — uses LangChain/LangGraph agents with OpenAI models to automatically generate code, set up Docker environments, and produce documentation from natural language prompts. Part of the Timeless project.                                                    |
| [varjotimeless-sjk](varjotimeless-sjk/)                                     | Timeless Architecture — a modular AI meeting assistant with real-time voice transcription (Whisper), LLM-powered meeting management, dynamic requirements tracking, and a Next.js live dashboard. Multi-service architecture with Manager, Requirements, and Transcription services.       |
| [voice-ai-assistant-framework](voice-ai-assistant-framework/)               | Voice AI assistant framework — a multithreaded Python system integrating real-time speech-to-text (RealtimeSTT), text-to-speech (Piper/F5-TTS/RealtimeTTS), and LLM-based conversation orchestration for interactive voice agents.                                                         |
| [vision-parser-testing](vision-parser-testing/)                             | PDF-to-Markdown conversion experiments — compares three approaches: Ollama vision models, OCR (Tesseract), and direct PDF text extraction for converting documents to Markdown.                                                                                                            |
| [VAILLA-TUOTTAVUUTTA-JA-RAPORTTIA-V2](VAILLA-TUOTTAVUUTTA-JA-RAPORTTIA-V2/) | Research report (LaTeX, in Finnish) — _"Tekoäly pk-yritysten voimavarana Etelä-Pohjanmaalla"_ (AI as a resource for SMEs in South Ostrobothnia) — covers the current state, opportunities, and practical recommendations for adopting generative AI in the region.                         |

---

## License

Individual projects have their own licenses — see the `LICENSE` file in each directory.
