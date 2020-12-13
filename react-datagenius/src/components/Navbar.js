import React, { Component } from 'react';

import {Link} from "react-router-dom";

export default class Navbar extends Component {
    render() {
        return (
            <nav className="navbar">
            <div className="nav-center">
            
            <ul className="nav-links">
                
                <li >
                    <Link to="/produits">Produits</Link>
                </li>

                <li>
                    <Link to="/caddie">Creer Caddie</Link>
                </li>
                <li>
                    <Link to="/mon_panier">mon Caddie</Link>
                </li>
            
            </ul>
            </div>
            </nav>
        )
    }
}
