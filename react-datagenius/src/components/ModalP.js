import React, { Component } from "react";
import Produit from "./Produit";

export default function ModalP({produits}) {

return(
        <div className="produitslist-center">
            {produits.map(item =>{
                return <Produit key={item.id} produit={item}/>;
            })}
        </div>
   
)

    }