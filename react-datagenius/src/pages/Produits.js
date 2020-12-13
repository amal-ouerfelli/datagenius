
    import React, { Component } from "react";
    
    import axios from "axios";
import ModalP from "../components/ModalP";
    

    class Produits extends Component {
      constructor(props) {
        super(props);
        this.state = {
          activeItem: {
          name : "",
          price : "",
          id_offre:'',
         

          },
          produits : []
        };
      }
      componentDidMount() {
        this.refreshList();
      }
      refreshList = () => {
        axios
          .get("http://127.0.0.1:8000/api/list_produits")
          .then(res => this.setState({ produits: res.data }))
          .catch(err => console.log(err));
      };
      
      toggle = () => {
        this.setState({ modal: !this.state.modal });
      };
      createItem = () => {
        const item = { name : "",
        price : "",
      };
      this.setState({ activeItem: item, modal: !this.state.modal });
      };

      render() {
        const {  produits } = this.state;
        return (
          
              <ModalP
                produits={produits}
                
              />
            
        );
      }
    }
    export default Produits;