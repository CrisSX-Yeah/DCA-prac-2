import React, { useState } from 'react';
import './RegisterPage.css';

const RegisterPage = () => {
  // Estados para controlar los valores de los campos del formulario
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  return (
    <div className="register-page">
      <h1 className="register-title">Registrarse</h1>
      <form className="register-form">
        <div className="form-group">
          <label htmlFor="username">Nombre de Usuario</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="form-input"
            placeholder="Ingresa tu nombre de usuario"
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="form-input"
            placeholder="Ingresa tu email"
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Contraseña</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="form-input"
            placeholder="Ingresa tu contraseña"
          />
        </div>
        <div className="form-group">
          <label htmlFor="confirm-password">Repetir Contraseña</label>
          <input
            type="password"
            id="confirm-password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            className="form-input"
            placeholder="Repite tu contraseña"
          />
        </div>
        <button type="submit" className="btn-register">Registrarse</button>
      </form>
    </div>
  );
};

export default RegisterPage;
