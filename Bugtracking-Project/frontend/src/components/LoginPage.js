import React, { useState } from 'react';
import './LoginPage.css';

const LoginPage = () => {
    // Estados para controlar los valores de los campos del formulario
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
  
    return (
      <div className="register-page">
        <h1 className="register-title">Login</h1>
        <form className="register-form">
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
          <button type="submit" className="btn-register">Confirm</button>
        </form>
      </div>
    );
  };
  

export default LoginPage;
