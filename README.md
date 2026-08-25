#  Adaptive TradeGuard

### AI-Based Autonomous Trading Risk & Permission System

Adaptive TradeGuard is an AI-based trading risk management system designed to prevent autonomous trading agents from executing trades during **uncertain, volatile, or unfavorable market conditions**.

The system introduces a **Trade Permission Gate** between an AI trading agent and the final trade execution decision. Instead of allowing an AI agent to trade whenever it generates a BUY or SELL signal, TradeGuard evaluates market conditions, technical indicators, signal confidence, volatility, and market regime before deciding whether the trade should be permitted.

---

## 📌 Problem Statement

Autonomous AI trading agents can generate trading decisions based on historical patterns and market signals. However, financial markets are dynamic and uncertain.

An AI agent may generate a BUY or SELL signal during:

* High-volatility periods
* Unstable market regimes
* Weak or conflicting technical signals
* Uncertain market conditions
* Situations with insufficient historical evidence

Executing every generated signal can increase unnecessary trading risk.

### 💡 Proposed Solution

Adaptive TradeGuard acts as a **risk-aware permission layer**.

Instead of:

```text
AI Agent → Trade Execution
```

the system uses:

```text
Market Data
     ↓
Data Preprocessing
     ↓
Feature Engineering
     ↓
Feature Preparation
     ↓
Market Regime Detection
     ↓
AI Trading Signal
     ↓
Trade Permission Gate
     ↓
┌─────────────────────────┐
│   Trade Permitted?      │
│                         │
│ YES → Execute Trade     │
│ NO  → Reject / HOLD     │
└─────────────────────────┘
```

---

# 🎯 Project Objectives

The main objectives of Adaptive TradeGuard are:

* Detect different market conditions and regimes.
* Generate meaningful technical features from market data.
* Prepare reliable ML-ready feature matrices.
* Evaluate trading signal quality.
* Measure market volatility and stability.
* Prevent low-confidence trades.
* Introduce an adaptive trade permission mechanism.
* Reduce unnecessary or high-risk trades.
* Evaluate the strategy using historical backtesting and paper trading.

---

# 📊 Dataset

The project uses historical **NIFTY 50 market data**.

The raw market dataset contains standard OHLCV information:

* Date
* Open
* High
* Low
* Close
* Volume

Historical market data is processed before being used for feature engineering and machine learning.

---

# ⚙️ Feature Engineering

The project currently generates the following technical features:

| Feature        | Description                             |
| -------------- | --------------------------------------- |
| Return         | Percentage change in closing price      |
| Log Return     | Logarithmic price return                |
| Volatility     | Rolling 20-day market volatility        |
| RSI-14         | Relative Strength Index over 14 periods |
| MACD           | Moving Average Convergence Divergence   |
| MACD Signal    | MACD signal line                        |
| MACD Histogram | Difference between MACD and signal      |
| ATR-14         | Average True Range over 14 periods      |
| Volume Change  | Change in trading volume                |
| Volume MA-20   | 20-day moving average of volume         |

These features help the system understand **price movement, momentum, volatility, and trading activity**.

---

# 🧠 Market Regime Detection

Financial markets can behave differently under different conditions.

For example:

```text
Bull Market
     ↓
High Positive Returns
     ↓
Stable / Trending Market
```

or:

```text
Bear Market
     ↓
Negative Returns
     ↓
High Risk
```

or:

```text
Sideways Market
     ↓
Low Directional Movement
     ↓
Uncertain Signals
```

Adaptive TradeGuard uses market-regime analysis as an important component of the permission system.

The current project includes a market-regime module under:

```text
src/models/market_regime.py
```

---

# 🛡️ Trade Permission Gate

The central idea of Adaptive TradeGuard is the **Trade Permission Gate**.

A trading agent may generate:

```text
BUY
SELL
HOLD
```

However, the signal does not automatically become a trade.

The permission layer evaluates multiple factors such as:

* Signal confidence
* Technical indicator agreement
* Market volatility
* Market regime
* Regime stability
* Historical evidence
* Risk conditions

Conceptually:

```text
                 AI Trading Signal
                        │
                        ▼
              ┌───────────────────┐
              │ Trade Permission   │
              │      Gate          │
              └─────────┬─────────┘
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
      PERMITTED                    REJECTED
          │                           │
          ▼                           ▼
    Execute Trade                  HOLD
```

The goal is not simply to generate more trades, but to allow trades only when the surrounding market conditions provide sufficient evidence.

---

# 🔄 Project Workflow

The planned machine-learning workflow is:

```text
Historical Market Data
          ↓
Data Preprocessing
          ↓
Exploratory Data Analysis
          ↓
Feature Engineering
          ↓
Feature Validation
          ↓
Feature Preparation
          ↓
Market Regime Detection
          ↓
Model Training
          ↓
Model Evaluation
          ↓
Trade Permission Gate
          ↓
Backtesting
          ↓
Paper Trading
```

---

# 📁 Project Structure

```text
adaptive-tradeguard/
│
├── data/
│   ├── raw/
│   │   └── yahoo_data.csv
│   │
│   └── processed/
│       ├── cleaned_data.csv
│       ├── feature_matrix.csv
│       └── prepared_features.csv
│
├── notebooks/
│   └── feature_analysis.ipynb
│
├── src/
│   ├── data/
│   │   ├── preprocessing.py
│   │   └── feature_preparation.py
│   │
│   ├── features/
│   │   ├── feature_engineering.py
│   │   └── validate_features.py
│   │
│   ├── models/
│   │   └── market_regime.py
│   │
│   └── data_visualization.py
│
├── results/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 🛠️ Technologies Used

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Matplotlib

### Machine Learning

* Scikit-learn

### Development

* Jupyter Notebook
* VS Code
* Git
* GitHub

### Planned / Extended Components

The complete system is intended to integrate additional components such as:

* Hidden Markov Models
* K-Means
* Sentence Transformers
* ChromaDB
* LangGraph
* VectorBT
* Streamlit

These components will be incorporated as the project progresses.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/Asha-Deepika/adaptive-tradeguard.git
```

## 2. Navigate to the project

```bash
cd adaptive-tradeguard
```

## 3. Create a virtual environment

### Windows

```bash
python -m venv .venv
```

## 4. Activate the virtual environment

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

The project can be developed and executed through the individual pipeline stages.

### Data preprocessing

```bash
python src/data/preprocessing.py
```

### Feature engineering

```bash
python src/features/feature_engineering.py
```

### Feature validation

```bash
python src/features/validate_features.py
```

### Feature preparation

```bash
python src/data/feature_preparation.py
```

The generated datasets are stored inside:

```text
data/processed/
```

---

# 📈 Current Project Status

### Completed

* [x] Project structure
* [x] Historical market data collection
* [x] Data preprocessing
* [x] Data cleaning
* [x] Exploratory feature analysis
* [x] Technical feature engineering
* [x] Feature validation
* [x] Feature matrix generation
* [x] ML feature preparation
* [x] Initial market-regime module
* [x] Git/GitHub project setup

### In Progress / Planned

* [ ] Market regime model refinement
* [ ] ML model training
* [ ] Model evaluation
* [ ] Trading signal generation
* [ ] Trade Permission Gate
* [ ] Risk scoring
* [ ] Backtesting
* [ ] Paper trading
* [ ] Streamlit dashboard
* [ ] Complete autonomous trading workflow

---

# 📊 Expected Evaluation Metrics

The system can be evaluated using both machine-learning and trading-specific metrics.

### Machine Learning

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC-AUC

### Trading

* Total Return
* Annualized Return
* Sharpe Ratio
* Maximum Drawdown
* Win Rate
* Number of Trades
* Risk-Adjusted Performance

The final evaluation will compare trading performance **with and without the Trade Permission Gate**.

---

# 🔬 Research Idea

The key research idea behind Adaptive TradeGuard is:

> **An AI trading signal should not automatically result in a trade.**

The system introduces an additional decision layer that evaluates whether the market conditions are suitable for executing the generated signal.

This creates a more risk-aware architecture:

```text
Prediction ≠ Permission

AI Signal
   ↓
Risk Evaluation
   ↓
Trade Permission
   ↓
Execution
```

This separation between **prediction and permission** is the core concept of Adaptive TradeGuard.

---

# 🔮 Future Scope

Future development may include:

* Adaptive risk thresholds
* Real-time market data
* Advanced market-regime detection
* LLM-based trading agents
* Semantic market-event analysis
* Vector database integration
* Autonomous agent workflows
* Real-time monitoring dashboard
* Advanced portfolio-level risk management
* Paper trading integration
* Continuous model evaluation
* Adaptive threshold optimization

---

# ⚠️ Disclaimer

This project is intended for **educational, research, and experimental purposes only**.

It does not provide financial advice and should not be used to make real-money trading decisions without appropriate validation, risk controls, and professional oversight.

---

# 👩‍💻 Author

**Asha-Deepika**

GitHub:

https://github.com/Asha-Deepika

Project:

https://github.com/Asha-Deepika/adaptive-tradeguard

---

# ⭐ Project Goal

Adaptive TradeGuard aims to build a **risk-aware autonomous trading architecture** where an AI system does not blindly execute every prediction.

Instead:

```text
Understand the Market
        ↓
Generate Signals
        ↓
Evaluate Risk
        ↓
Grant Trade Permission
        ↓
Execute Only When Conditions Are Favorable
```

**Adaptive TradeGuard — Making Autonomous Trading More Risk-Aware. 🛡️📈**
