# Forest Fire Prediction System

A web application that predicts the Fire Weather Index (FWI) based on weather parameters.

## Features

- Input weather parameters (temperature, humidity, wind speed, etc.)
- Predict Fire Weather Index (FWI)
- Visualize fire risk level

## Technologies Used

- Flask
- Scikit-learn
- NumPy
- HTML/CSS

## Deployment to Vercel

### Prerequisites

1. Create a [Vercel](https://vercel.com/) account
2. Install the Vercel CLI:
   ```
   npm install -g vercel
   ```

### Deployment Steps

1. Clone this repository:
   ```
   git clone <repository-url>
   cd Forest-Fire-Prediction-System
   ```

2. Login to Vercel:
   ```
   vercel login
   ```

3. Deploy to Vercel:
   ```
   vercel
   ```

4. Follow the prompts in the CLI:
   - Set up and deploy project? `Y`
   - Which scope to deploy to? `<your-username-or-team>`
   - Link to existing project? `N`
   - What's your project name? `forest-fire-prediction`
   - In which directory is your code located? `./`
   - Want to override settings? `N`

5. Your app will be deployed and a URL will be provided.

### Alternative: Deploy via GitHub

1. Push your code to GitHub
2. Go to [Vercel Dashboard](https://vercel.com/dashboard)
3. Click "New Project"
4. Import your GitHub repository
5. Configure the project:
   - Framework Preset: Other
   - Root Directory: ./
   - Build Command: None
   - Output Directory: None
6. Click "Deploy"

## Local Development

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your browser and go to `http://127.0.0.1:5000/` 