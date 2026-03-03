# 🌤️ WeatherFit AI: Smart Clothing Recommender

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![API](https://img.shields.io/badge/API-WeatherAPI-green)

WeatherFit AI is a machine learning-powered command-line application that acts as your personal smart stylist. Instead of relying on static if-else rules, it utilizes a **Decision Tree Classifier** trained on synthetic weather-to-garment data to predict the most appropriate daily outfit based on real-time weather conditions.

---

## 🚀 Key Features

* **AI-Driven Logic:** Uses Scikit-Learn's classification algorithms to learn patterns between temperature, wind speed, precipitation, and human clothing choices.
* **Real-Time API Integration:** Fetches live and next-day forecast data globally using **WeatherAPI**.
* **Synthetic Data Generation:** Includes a custom script to automatically generate logical, randomized datasets for training the model.
* **Interactive CLI:** A user-friendly command-line interface that asks for the target city and timeframe (today/tomorrow).

---

## 🛠️ Tech Stack

* **Language:** Python
* **Machine Learning:** Scikit-Learn (Decision Tree Classifier / Random Forest)
* **Data Manipulation:** Pandas
* **Network Requests:** Requests library

---

## 📁 Project Structure
```text
WeatherClothesML/
│
├── ai_weather.py         # Main AI engine and CLI application
├── generate_data.py      # Script to generate the synthetic dataset
├── clothes_data.csv      # Generated dataset (ignored in version control ideally)
└── README.md             # Project documentation
```
  

## 📦 Installation & Setup
**1.Clone the repository**
```
git clone [https://github.com/Burakscheker/WeatherFit-AI.git](https://github.com/Burakscheker/WeatherFit-AI.git)
cd WeatherFit-AI
```
**2.Install the required dependencies:**
```
pip install pandas scikit-learn requests
```
**3.Get yout API key**
Get a free API key from WeatherAPI and replace the API_KEY variable in ai_weather.py.
**4.Run the AI:**
```
python ai_weather.py
```
## 💡 Future Improvements
* [ ] Integrate a real-world, industry-standard dataset (e.g., DeepFashion).

* [ ] Upgrade the CLI to a graphical Web UI using Streamlit.

* [ ] Add personalized user profiles (e.g., preferences for users who get cold easily).

# Developer : Ömür Burak Şeker
