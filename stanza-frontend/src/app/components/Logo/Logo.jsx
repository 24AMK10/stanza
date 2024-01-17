import React from 'react';
import './Logo.css';

export default function Logo() {
    return (
        <>
            <div className="imgTag">


                <img src="./wonder.png" alt="An SVG of an eye"
                    height={150} width={200}
                    style={{backgroundColor:"greenyellow", 
                        padding:"0.1rem",
                        borderRadius:"0.4rem"
                    }}
                />
            </div>
        </>
    )
}   