import PropTypes from "prop-types"
import React, { Component } from "react";


export default function MonPanier({panier}) {
    const{id_p} = panier ;

    return (
            <table>
                
                <tr><th>
                    id produit:
                    </th>
                
                <th>{id_p}</th></tr>
                
                </table>  

    )
}
MonPanier.propTypes={
    panier:PropTypes.shape({
    id_p:PropTypes.object.isRequired,
    })
}

