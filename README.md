# 🎓 SkillSaarthi – Your Personalized AI Skilling Twin

**SkillSaarthi** is an open-source, mobile-first GenAI solution that provides a **personalized AI mentor (Skill Twin)** to guide underserved youth in India through adaptive skill development, career planning, and learning—entirely in their own language and context.

---

## 🚀 Problem Statement

Millions of youth from rural and underserved communities lack access to practical, personalized, and goal-aligned skilling opportunities. Existing platforms are rigid, not contextual, and often inaccessible due to language, device, or internet limitations. SkillSaarthi bridges this gap through an offline-capable, voice-driven AI assistant that evolves with each learner.

---

## 📱 Solution Overview

- 🌐 **Offline-First Android App**
- 🧠 **GenAI-Powered AI Twin** that mentors each learner
- 🗣️ **Voice + Text Interface in Regional Languages**
- 🎯 **Goal-to-Skill Mapping** with personalized microlearning
- 🕹️ **Gamified Skill Simulations** via open-source game engine
- 🎓 **Micro-Certification, Resume Building & Job Discovery**
- 🤝 **Mentor Network & Community Learning**

---

## 🧠 Core Features

| Feature                          | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| 🎯 Personalized Skilling Roadmap | AI maps user goals to skill paths, milestones, and content                 |
| 🧑‍🏫 AI Mentor Chatbot            | Conversational, multilingual voice/text assistant                         |
| 🧩 Offline Learning Modules       | Downloadable learning packs, exercises, and quizzes                        |
| 🕹️ Skill Simulations             | Interactive practice via Godot-based micro-games                           |
| 📈 Progress Tracker               | Dashboard with badges, feedback, and daily/weekly insights                 |
| 🧾 Scheme & Job Matching          | Maps users to relevant gov schemes and local jobs                          |

---

## 🛠️ Tech Stack

| Layer         | Tools/Tech Used                                                  |
|---------------|------------------------------------------------------------------|
| Frontend      | Kotlin + Jetpack Compose, Android Room, EncryptedPreferences    |
| Backend       | Node.js + Express, Firebase / Supabase (optional)               |
| AI/ML Engine  | HuggingFace Transformers, Scikit-learn, Haystack, XGBoost       |
| Voice & Lang  | Vosk (STT), Coqui TTS, Indic NLP Toolkit                        |
| Simulation    | Godot Engine + TensorFlow Lite                                  |
| Model Deploy  | ONNX Runtime, Flower (Federated Learning)                       |

---

## 🌐 Architecture Diagram
![image](https://github.com/user-attachments/assets/d950f370-1e92-42e6-93bc-2302b5404d20)

---

## 📂 Repository Structure

```bash
skillsaarthi/
├── app/                   # Android app code (Kotlin)
├── app-engine/             # AI twin logic and model integration
├── mockups/               # Diagrams, wireframes
├── docs/                  # Tech stack, datasets, architecture
├── README.md

```

## 📊 Datasets Used

- **NSDC Skill Role Data** *(Public)*  
- **NCS Job Role Listings** *(Public)*  
- **Government Schemes Mapping** *(Public + Scraped)*  
- **Synthetic Q&A + Simulated User Logs** *(Synthetic)*  
- **On-device Learning History & Preferences** *(User-generated)*

---

## 🔐 Ethical & Inclusive by Design

✅ Works fully offline – no internet dependency  
✅ Federated learning – user data stays on-device  
✅ Transparent and explainable AI decisions  
✅ UI designed for low-literacy and low-bandwidth users  

---

## 📜 License

Licensed under the **MIT License** – open for personal, academic, and commercial use with attribution.

---
