import React from 'react';
import { Link } from 'react-router-dom';
import AuthButton from './AuthButton'

function Nav() {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/chat">Chat</Link>
      <Link to="/chat-history" >Chat History</Link>
      <Link to="/add-todo">Add Todo</Link>
      <AuthButton />
      <Link to="/register">Register</Link>
      <Link to="/user-profile">User Profile</Link>
      {/* More navigation links as needed */}
    </nav>
  );
}

export default Nav;
