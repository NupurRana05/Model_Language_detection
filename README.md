# Model_Language_detection

# 🌍 Language Detection NLP Project

## 📌 Project Overview

The Language Detection NLP Project is a machine learning application that predicts the language of a given text.

It uses Natural Language Processing (NLP), TF-IDF character n-gram features, and Logistic Regression to classify text into one of 20 supported languages.

The project includes a simple and interactive web interface built using Streamlit.






<img width="840" height="545" alt="image" src="https://github.com/user-attachments/assets/6a244098-66e9-4320-bea2-62276143b133" />





























## ✨ Features

- Detects languages from user-input text.
  
- Supports 20 different languages.
  
- Uses a trained machine learning model.
  
- Provides an interactive Streamlit web interface.
  
- Displays the predicted language and language code.
  
- Includes a greeting lookup for selected common words, such as "Hello", "Ciao", and "Bonjour".
 
- Handles empty input with a warning message.
  

## 🛠️ Tech Stack

- Programming Language: Python
  
- Machine Learning: Scikit-learn
  
- Natural Language Processing:TF-IDF Vectorization
  
- Algorithm: Logistic Regression
  
- Web Framework: Streamlit
  
- Model Serialization: Joblib
  
- Dataset: Hugging Face – `papluca/language-identification`


## 🌐 Supported Languages

The application supports the following 20 languages:

1. Arabic (`ar`)
2. Bulgarian (`bg`)
3. German (`de`)
4. Greek (`el`)
5. English (`en`)
6. Spanish (`es`)
7. French (`fr`)
8. Hindi (`hi`)
9. Italian (`it`)
10. Japanese (`ja`)
11. Dutch (`nl`)
12. Polish (`pl`)
13. Portuguese (`pt`)
14. Russian (`ru`)
15. Swahili (`sw`)
16. Thai (`th`)
17. Turkish (`tr`)
18. Urdu (`ur`)
19. Vietnamese (`vi`)
20. Chinese (`zh`)

## 📂 Project Structure

```text
language_detection_model/
│
├── app.py
├── requirements.txt
├── language_detection_model.pkl
└── README.md
```

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Open the Project Folder

```bash
cd language_detection_model
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 🚀 How to Use

1. Run the Streamlit application.
 
2. Enter a word or sentence in the text input area.
   
3. Click the **Detect Language** button.
  
4. View the predicted language and its language code.


### Example Predictions

| Input Text | Expected Language |
|---|---|
| Hello | English |
| Bonjour | French |
| Ciao | Italian |
| Hola | Spanish |
| नमस्ते | Hindi |
| Hallo | German |

*Note: These examples represent expected results. The greeting lookup handles selected words, while other inputs are classified by the trained model. Predictions are not guaranteed to be correct for every text.*

## 🧠 Model Details

The project uses a Scikit-learn machine learning pipeline with two main components:

1. TF-IDF Vectorizer**

- Extracts character-level n-gram features from text.
- Uses character sequences of lengths 2 to 5.
- Converts text into numerical features suitable for machine learning.

2. Logistic Regression**

- Learns patterns associated with different languages.
- Predicts the language label for new text.
- Uses the trained model saved in a `.pkl` file.

## 📊 Model Evaluation

The model was evaluated using a held-out test dataset.

The initial evaluation reported approximately **99% test accuracy** after duplicate samples were removed from the test data.

This result should be treated as a preliminary benchmark. A final evaluation should use the original, untouched test split to obtain a more reliable performance estimate.

## ⚠️ Limitations

- Very short words may produce incorrect predictions.
  
- Roman Hindi and Hinglish are not separately supported language classes.
  
- Mixed-language text may be classified incorrectly.
  
- The greeting lookup only covers selected words.
  
- Model predictions depend on the training data and text provided.
  

## 🔮 Future Improvements

- Improve predictions for short text.
 
- Add better handling for Roman Hindi and Hinglish.
  
- Evaluate performance on an untouched test dataset.
  
- Add a language prediction confidence score.
  
- Deploy the application online using Streamlit Community Cloud.
  
- Improve the user interface and add multilingual examples.
  

## 👩‍💻 Author

Nupur Rana

B.Tech – Artificial Intelligence and Data Science

## 📄 License

This project is intended for educational and portfolio purposes. Add a suitable open-source license if you plan to distribute the project publicly.
