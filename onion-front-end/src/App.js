import React from 'react';
import NavBar from './components/NavBar';
import MainGrid from  './components/MainGrid';
import './App.css';

function App() {
    return (
      <div className="App">
          <header className="App-header">
            <NavBar/>
            <MainGrid></MainGrid>

          </header>
      </div>
  );
}

export default App;
