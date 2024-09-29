import React from 'react';
import '../css/HomePage.css';
import logo from '../../assets/logo.png'; // Si tienes un logo
import { useNavigate } from 'react-router-dom';

const HomePage = () => {

  const navigate = useNavigate(); // Inicializa useNavigate para la navegación

  const handleRegisterClick = () => {
    navigate('/register'); // Redirige a la página de registro
  };

  const handleLoginClick = () => {
    navigate('/login'); // Redirige a la página de registro
  };
  
  return (
    <div className="homepage-container">
      <div className="homepage-header">
        <img src={logo} alt="LBT Logo" className="homepage-logo" />
        <h1 className="homepage-title">Local Bug Tracker</h1>
      </div>
      <div className="homepage-content">
        <button className="btn btn-register" onClick={handleRegisterClick}>Register</button>
        <button className="btn btn-login" onClick={handleLoginClick}>Login</button>
      </div>
    </div>
  );
};

export default HomePage;
