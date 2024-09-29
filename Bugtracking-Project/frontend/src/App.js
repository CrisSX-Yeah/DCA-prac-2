import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Importa React Router
import HomePage from './components/HomePage';
import RegisterPage from './components/RegisterPage';
import LoginPage from './components/LoginPage';

function App() {
  return (
    <Router>
      <div className="app-container">
        {/* Define las rutas de la aplicación */}
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
