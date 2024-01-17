import React from 'react';


export default function SearchBar() {
    
    return(
        <>
            
            <input
                className="flex-1 px-4 py-2 m-5 border border-gray-400 rounded-md" 
                type="text" placeholder="locality / property / city"
                style={{color:"black"}}
            >           
            </input>
     
        </>
    )
}