import React from 'react';
import '../css/Navbar.css'; // Import custom CSS
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <div className="navbar">
      <div className="navbar-content">
        <Link to="/" className="navbar-link">Home</Link>
        <Link to="/information" className="navbar-link">Information</Link>
      </div>
    </div>
  );
};

export default Navbar;
