import PropTypes from "prop-types"
import React, { Component } from "react";


export default function Produit({produit}) {
    const{name, price, id_offre} = produit;
    
    
   
    return (
        <article className="produit">
            <div className="img-container">
                
                <div >
                   
            <h2 className="produit-info">{name}</h2>
            <h2 className="price-top">${price}</h2></div>
            <div>
  <button  className="btn-primary">Acheter</button>


</div>

            
            </div>
        </article>
        
    )
}
Produit.propTypes={
    produit:PropTypes.shape({
    name:PropTypes.string.isRequired,
    price:PropTypes.string.isRequired,
    id_offre:PropTypes.object.isRequired,
    })
}