"use client";
import React, {useState} from 'react';
import axios from 'axios';


export default function SearchBar() {
   
    // const [searchPattern, setSearchPattern] = useState('');
    const [results, setResults] = useState([]);

    const handleInputToSearch = async (event) => {
        let searchVal = event.target.value;
        if (searchVal === "" || searchVal === " "){
            setResults([])
        }
        else{
            try{
                const response = await axios.get(`http://127.0.0.1:5005/search-pg/get-pgs/${searchVal}`, {
            timeout: 1000,
            });
            let data = response?.data;
            console.log(data);
            data = data.length > 5 ? data.slice(0, 5) : data;
            setResults(data);
            }
            catch (error){
                console.log("There was an error", error);
        
            }
        }
    }

    return(

    
        <>
            
            <input
                className="w-full h-30 text-black" 
                onChange={handleInputToSearch}
                type="text" 
                
                placeholder="locality / property / city"
               
            >           
            </input>
            <ul>
                {results.map((result, key) => (
                    // console.log(key, result)
                    <li key={key}>{result?.locality}</li>
                ))}
            </ul>
       
        </>  
        
    )
}

