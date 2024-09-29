import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Importa React Router
import HomePage from './components/js/HomePage';
import RegisterPage from './components/js/RegisterPage';
import LoginPage from './components/js/LoginPage';
import Navbar from './components/js/Navbar';
import InformationPage from './components/js/InformationPage';

function App() {
  return (
    <Router>
      <div className="app-container">
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/information" element={<InformationPage />} /> {/* New route for information */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
