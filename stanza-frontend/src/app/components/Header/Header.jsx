

import React from 'react';
import Logo from '../Logo/Logo';
import SearchBar from '../SearchBar/SearchBar';

const Header = () => {
  
  let userName = "Gojo";

  return (
    <header className="flex items-center justify-between p-4 ">
      <div className="flex items-center">
        <Logo/>
      </div>

      <SearchBar />

      {/* Some Text on the Right */}
      <p className="text-lg">Welcome, {userName}!</p>
    </header>
  );
};

export default Header;

