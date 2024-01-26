

import React from 'react';
import Logo from '../Logo/Logo';
import SearchBar from '../SearchBar/SearchBar';

const Header = () => {
  
  let userName = "Gojo";

  return (


      <div className="grid grid-rows-2 grid-flow-col">
          <div className="row-span-2 pl-2 py-2 ">
            <Logo/>
          </div>    
          <div className="row-span-2 col-span-10 py-2 pl-0 overflow-visible ">
              <SearchBar/>
          </div>
          <div className="row-span-2 col-span-2 py-2 right-0">
            <h3>
              {`hi ${userName}!`} 
            </h3>
          </div>
      </div>
   
  );
};

export default Header;

