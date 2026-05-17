# 🛡️ Machine Learning-Based Phishing URL Detection System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.0-orange)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest-success)
![Accuracy](https://img.shields.io/badge/Accuracy-96%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

**A powerful machine learning web application that detects phishing websites with 96% accuracy by analyzing URL patterns and characteristics.**

[🌐 Live Demo](https://your-app.onrender.com) • 
[📖 Documentation](#) • 
[🐛 Report Bug](https://github.com/yourusername/phishing-url-detection/issues) • 
[✨ Request Feature](https://github.com/yourusername/phishing-url-detection/issues)

</div>

---

## 📋 Table of Contents

- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Tech Stack](#-tech-stack)
- [Dataset & Model](#-dataset--model)
- [Team & Contributions](#-team--contributions)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Performance Metrics](#-performance-metrics)
- [Deployment](#-deployment)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 About The Project

Phishing attacks are one of the most prevalent cybersecurity threats where attackers create deceptive websites mimicking legitimate ones to steal sensitive information such as passwords, banking credentials, and personal data.

This **Machine Learning Based Phishing URL Detection System** provides a robust solution by:
- Analyzing URL structures in real-time
- Extracting 23 critical features from each URL
- Using a trained Random Forest model with **96% accuracy**
- Providing instant feedback with confidence scores
- Educating users about potential cyber threats

### Purpose
Help users identify potentially malicious URLs before visiting them, making the internet a safer place.

### Scope
Users can enter any website URL and get an immediate classification (legitimate or phishing) from our machine learning model.

### Workflow
1. **User enters URL** in the web interface (UI by Kiran & Shriyanshi)
2. **Flask backend** receives the request (backend by Ayush & Pragati)
3. **Feature extraction** module analyzes URL (23 features) (ML by Ayush & Pragati)
4. **ML model** processes features and predicts (trained by Ayush & Pragati)
5. **Result displayed** with confidence score and recommendations (UI integration by all)
6. **History stored** in session for future reference

---

## 💻 Tech Stack

### Frontend 
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Font Awesome](https://img.shields.io/badge/Font_Awesome-339AF0?style=for-the-badge&logo=fontawesome&logoColor=white)

### Backend 
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)

### Machine Learning 
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

### Deployment 
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 📊 Dataset & Model

### Dataset Statistics
| Attribute | Value |
|-----------|-------|
| **Total URLs** | 11,430 |
| **Classes** | Balanced (50% phishing, 50% legitimate) |
| **Total Features** | 87 extracted features |
| **Selected Features** | 23 for final model |
| **Source** | Web Page Phishing Detection Dataset |

### Feature Categories

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔍 **Real-time Analysis** | Instant URL scanning and classification |
| 🤖 **ML-Powered** | Random Forest model with 96% accuracy |
| 📊 **23 Features** | Comprehensive URL characteristic analysis |
| 🎨 **Modern UI** | Clean, responsive, user-friendly interface (by Kiran & Shriyanshi) |
| 📜 **Search History** | Track and review past URL checks |
| 📱 **Mobile Ready** | Fully responsive across all devices |
| 🔒 **Secure** | Input validation and protection against injections |
| 📈 **Confidence Score** | Probability-based result confidence |
| 🌐 **REST API** | Programmatic access for developers |
| ⚡ **Fast Response** | Results within seconds |
| 🛡️ **Safety Tips** | Actionable recommendations for users |

---

## 🏗 System Architecture


The system follows a three-tier architecture:

### Model Specifications

| Parameter | Value |
|-----------|-------|
| *Algorithm* | Random Forest Classifier |
| *Accuracy* | 96.2% |
| *Precision* | 96.1% |
| *Recall* | 95.8% |
| *F1-Score* | 95.9% |
| *AUC-ROC* | 0.98 |
| *Training Features* | 23 selected features |
| *Cross-validation* | 5-fold |
| *Best Parameters* | max_depth: 20, n_estimators: 200 |

### Feature Importance
| Feature | Importance |
|---------|------------|
| google_index | 0.18 |
| page_rank | 0.15 |
| nb_www | 0.12 |
| ratio_digits_url | 0.10 |
| phish_hints | 0.09 |
| domain_age | 0.08 |

---

## 👥 Team & Contributions

| Member | Role | Contributions |
|--------|------|---------------|
| *Ayush Kumar* | ML Engineer | Model training, feature selection, testing, backend API, deployment (Render) |
| *Pragati* | ML Engineer | Model training, feature selection, testing, backend API, deployment (Render) |
| *Kiran* | Frontend Developer & Tech Writer | UI design (HTML/CSS/JS), responsive layout, user manual, documentation |
| *Shriyanshi* | Frontend Developer & Tech Writer | UI implementation (HTML/CSS/JS), API documentation, testing, final documentation |

All team members collaborated on integration, debugging, and project presentation.

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (optional)
- Virtual environment (recommended)
```bash
### Step-by-Step Setup
phishing-url-detection/
├── app.py                          # Main Flask app (Ayush & Pragati)
├── requirements.txt
├── phishing_model.pkl              # Trained ML model (Ayush & Pragati)
├── Procfile / runtime.txt          # Deployment configs (Ayush & Pragati)
├── utils/
│   ├── feature_extractor.py        # 23 features (Ayush & Pragati)
│   └── model_loader.py
├── templates/                      # HTML files (Kiran & Shriyanshi)
│   ├── index.html
│   ├── about.html
│   ├── result.html
│   ├── history.html
│   └── error.html
├── static/css/style.css            # Styling (Kiran & Shriyanshi)
└── notebooks/                      # Training notebook (Ayush & Pragati)

```bash
# Clone the repository
git clone https://github.com/yourusername/phishing-url-detection.git
cd phishing-url-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
#### Linux/Mac
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the Application

```bash
python app.py
```

---

## 5️⃣ Open in Browser

```bash
http://127.0.0.1:5000
```

---

# 📊 Machine Learning Workflow

1. Data Collection  
2. Data Preprocessing  
3. Feature Extraction  
4. Model Training  
5. Model Evaluation  
6. Flask Integration  
7. Deployment on Render  

---

# 📈 Algorithms Used

- Logistic Regression
- Random Forest
- Decision Tree
- Support Vector Machine (SVM)
- Naive Bayes

---

# 📷 Screenshots

## Home Page
_Add project screenshots here_

## Prediction Result
_Add result screenshots here_

---

# 🌐 Deployment

The project is deployed using **Render**.

### Live Demo
🔗 https://phishing-url-detection.onrender.com

---

# 📓 Jupyter Notebook

🔗 View on Kaggle

---

# 📚 Dataset

Dataset used for training:

- Web Page Phishing Detection Dataset

---

# 🤝 Contributing

Contributions are welcome!

## Steps to Contribute

1. Fork the repository  
2. Create a new branch  
3. Make your changes  
4. Commit your changes  
5. Push to your branch  
6. Create a Pull Request  

---

# 📄 License

MIT License

Copyright (c) 2026 Ayush Kumar, Pragati, Kiran, Shriyanshi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including, without limitation, the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

# 📞 Contact

## 👨‍💻 Team Members

| Name | Role | Roll No | Email | GitHub |
|------|------|----------|--------|---------|
| Ayush Kumar | ML Engineer | 2308390100018 | ayush95190@gmail.com |
| Pragati | ML Engineer | 2308390100046 | pragatitha950@gmail.com | 
| Kiran | Frontend & Documentation | 2308390100031 | kirangaur1507@gmail.com |
| Shriyanshi | Frontend & Documentation | 2308390100064 | shriyanshi1712@gmail.com |

> **Note:** Replace placeholder Roll Numbers and email addresses as needed.

---

# 🔗 Project Links

| Resource | Link |
|----------|------|
| 📦 GitHub Repository | [https://github.com/yourusername/phishing-url-detection](https://github.com/Ayush-Kumar-45/Phishing-URL-Detection) |
| 🌐 Live Demo |  |
| 📓 Jupyter Notebook | View on Kaggle |

---

# 🙏 Acknowledgments

## Resources

| Resource | Purpose |
|----------|----------|
| Web Page Phishing Detection Dataset | Training data for the model |
| Scikit-learn | Machine learning tools and algorithms |
| Flask | Web framework for the application |
| Font Awesome | Icons and UI elements |
| Render | Free hosting and deployment |
| GitHub | Code hosting and version control |

---

## Inspirations

- OWASP — For cybersecurity guidelines and best practices  
- Google Safe Browsing — For phishing detection inspiration  
- PhishTank — For community-driven phishing data  

---

## Special Thanks

- Department of Computer Science and Engineering — For academic support  
- Project Guide and Mentors — For guidance and feedback  
- Open Source Community — For tools and libraries  
- All Contributors and Supporters — For helping improve this project  

---

<div align="center">

# ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!

![Stars](https://img.shields.io/github/stars/yourusername/phishing-url-detection?style=social)
![Forks](https://img.shields.io/github/forks/yourusername/phishing-url-detection?style=social)
![Watchers](https://img.shields.io/github/watchers/yourusername/phishing-url-detection?style=social)

Made with by Ayush Kumar, Pragati, Kiran & Shriyanshi

© 2026 Machine Learning-Based Phishing URL Detection System. All Rights Reserved.

⬆ Back to Top

</div>
