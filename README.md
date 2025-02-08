# 💡 AI Decision Maker

🚀 **AI Decision Maker** is a **Streamlit-based web application** that helps users make informed decisions using the **DeepSeek-R1:7B AI model**.  
The app allows users to input a question and receive **AI-generated recommendations** instantly.

---

## 🎯 **Features**
✅ **User-Friendly UI** - Simple and clean interface  
✅ **Powered by AI** - Uses **DeepSeek-R1:7B** for intelligent responses  
✅ **Real-Time Decision Making** - Get instant AI-generated insights  
✅ **Streamlit-Based** - Lightweight and easy to deploy  
✅ **Interactive UI** - Styled with custom CSS for a better experience  

---

## 🛠️ **Installation & Setup**

### **1️⃣ Install Python (If Not Installed)**
Make sure you have **Python 3.8+** installed.  
[Download Python](https://www.python.org/downloads/)

### **2️⃣ Clone or Download the Project**
```bash
git clone https://github.com/your-username/ai-decision-maker.git
cd ai-decision-maker
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Install and Pull DeepSeek-R1:7B Model**
Before running the app, install **Ollama** and pull the AI model:
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download DeepSeek-R1:7B
ollama pull deepseek-r1:7b
```

---

## 🚀 **How to Run the App**
```bash
streamlit run app.py
```
The app will run on **localhost:**
```
http://localhost:8501
```

---

## 🌍 **Access the App Over a Network (LAN)**
To allow other users on your local network to access the app, run:
```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```
Users can access it via:
```
http://YOUR_LOCAL_IP:8501
```
Find your local IP using:
```bash
ipconfig  # Windows
hostname -I  # macOS/Linux
```

---

## 🔐 **Security & Public Access**
If you want to **expose the app publicly**, use **ngrok**:
```bash
pip install ngrok
ngrok http 8501
```
It will provide a **public URL** like:
```
https://your-random-url.ngrok.io
```

---

## 🖥️ **How to Use**
1. **Enter a question** (e.g., "Should I invest in AI stocks?")
2. Click on **🔮 Get AI Decision**
3. Wait for **AI-generated advice**
4. View the **response inside a styled box**
5. Repeat the process for new queries 🎯

---

## 🎨 **Screenshots**
| Home Page  | AI Response |
|------------|------------|
| ![Home](https://via.placeholder.com/600x300?text=Home+Page) | ![Response](https://via.placeholder.com/600x300?text=AI+Response) |

---

## 💡 **Customization**
You can **customize the UI** by editing:
- **Colors & Styling:** Inside `app.py` (CSS section)
- **Change AI Model:** Modify the `ollama.chat` function to use another model
- **Add More Features:** Enhance the UI with **buttons, charts, or interactive elements**

---

## 🛠️ **Troubleshooting**
**1️⃣ "ModuleNotFoundError: No module named 'streamlit'"**  
👉 Run:
```bash
pip install streamlit
```

**2️⃣ "Ollama is not recognized"**  
👉 Ensure Ollama is installed:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**3️⃣ AI Model Not Downloaded?**  
👉 Run:
```bash
ollama pull deepseek-r1:7b
```

**4️⃣ Streamlit Not Opening in Browser?**  
👉 Manually open:
```
http://localhost:8501
```

---

## 📜 **License**
This project is **open-source** under the **MIT License**.  
Feel free to **modify, use, and distribute** it! 🚀

---

## 🙌 **Contributing**
We welcome contributions! If you find a bug or have suggestions:
1. **Fork the repo**
2. **Make changes**
3. **Submit a pull request**

---

## 📞 **Contact**
For any queries or feedback:  
📧 Email: `your-email@example.com`  
🐦 Twitter: `@your_twitter_handle`

