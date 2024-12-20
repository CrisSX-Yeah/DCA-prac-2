import React, { useState } from 'react';
import '../css/RegisterPage.css';

const RegisterPage = () => {
  // Estados para controlar los valores de los campos del formulario
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  return (
    <div className="register-page">
      <h1 className="register-title">Register</h1>
      <form className="register-form">
        <div className="form-group">
          <label htmlFor="username" className='form-group-label'>Username</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="form-input"
            placeholder="Enter your username"
          />
        </div>
        <div className="form-group">
          <label htmlFor="email" className='form-group-label'>Email</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="form-input"
            placeholder="Enter your email"
          />
        </div>
        <div className="form-group">
          <label htmlFor="password" className='form-group-label'>Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="form-input"
            placeholder="Enter your password"
          />
        </div>
        <div className="form-group">
          <label htmlFor="confirm-password" className='form-group-label'>Repeat your password</label>
          <input
            type="password"
            id="confirm-password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            className="form-input"
            placeholder="Repeat your password"
          />
        </div>
        <button type="submit" className="btn-register">Confirm</button>
      </form>
    </div>
  );
};

export default RegisterPage;
