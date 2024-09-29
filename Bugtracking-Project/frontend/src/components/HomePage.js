import React from 'react';
import './HomePage.css';
import logo from '../assets/logo.png'; // Si tienes un logo

const HomePage = () => {
  return (
    <div className="homepage-container">
      <div className="homepage-header">
        <img src={logo} alt="LBT Logo" className="homepage-logo" />
        <h1 className="homepage-title">Local Bug Tracker</h1>
      </div>
      <div className="homepage-content">
        <button className="btn btn-register">Registrarse</button>
        <button className="btn btn-login">Iniciar Sesión</button>
      </div>
    </div>
  );
};

export default HomePage;
