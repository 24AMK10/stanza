import React from 'react';
import Header from '../Header/Header'

export default function Navbar({heading}) {


    return (
        <nav className="navbar navbar-light bg-light">
            <span className="navbar-brand mb-0 h1">
                <Header heading={heading}/>
            </span>
        </nav>
    )
}