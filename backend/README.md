
1. **Clone the GitHub Repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>/backend
   ```

2. **Set Up the Virtual Environment:**
   - **For macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **For Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Required Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Preprocessing (Optional if data is already prepared):**
   ```bash
   python data_preparation.py
   ```

5. **Train the Model (Optional if model is already trained):**
   ```bash
   python train_model.py
   ```

6. **Start the Backend Server:**
   ```bash
   python app.py
   ```

Once the server is running, the backend will be available at `http://localhost:5000`.
