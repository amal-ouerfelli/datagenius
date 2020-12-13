import React, { Component } from "react";
import MonPanier from "./MonPanier";

export default function ModalM({paniers}) {
   
return(
    <section className="produitslist">
        <div className="produitslist-center">
            {paniers.map(item =>{
                return <MonPanier key={item.id_p} panier={item}/>;
            })}
            
        </div>
    </section>
)


    }