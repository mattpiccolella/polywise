import React from 'react';
import Nav from './components/Nav';
import Chat from   './components/Chat';
import HomePage from './components/HomePage';
import Login from   './components/Login';
import Register from   './components/Register';
import UserProfile from   './components/UserProfile';
import FileManager from './components/FileManager';
import { AuthProvider } from './contexts/AuthContext';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {

  return (
      <div class="flex flex-col h-screen">
        <AuthProvider>
          <Router>
            <Nav />
            <Routes>
              <Route exact path="/" element={<HomePage />}/>
              <Route exact path="/chat" element={<Chat />}/>
              <Route path="/chat/:id" element={<Chat />}/>
              <Route path="/login" element={<Login />}/>
              <Route path='/register' element={<Register />}/>
              <Route path="/user-profile" element={<UserProfile />}/>
              <Route path="/documents" element={<FileManager />}/>
              {/* Add more routes as needed */}
            </Routes>
          </Router>
          </AuthProvider>
        </div>
  );
}

export default App;