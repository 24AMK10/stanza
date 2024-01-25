"use client";
import React, {useState} from 'react';
import axios from 'axios';

export default function SearchBar() {
   
    // const [searchPattern, setSearchPattern] = useState('');
    const [results, setResults] = useState([]);

    const handleInputToSearch = async (event) => {
        try{

            const response = await axios.get(`http://127.0.0.1:5005/search-pg/get/${event.target.value}`, {
                timeout: 1000,
            });

            console.log(response);
     
        }catch (error){
            console.log("There was an error", error);
     
        }
    }

    return(

        <>
            
            <input
                className="flex-1 px-4 py-2 m-5 border-0" 
                onChange={handleInputToSearch}
                type="text" placeholder="locality / property / city"
                style={{color:"black"}}
            >           
            </input>
       
        </>  
        
    )
}

