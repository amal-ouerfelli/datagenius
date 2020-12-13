
    import React, { Component } from "react";
    import Modal from "../components/Modal";
    import axios from "axios";
    
    
    class Caddie extends Component {
      constructor(props) {
        super(props);
        this.state = {
          activeItem: {
          nomprenom : "",
          carte_fidelite : "",
         

          },
          client : []
        };
      }
      
      refreshList = () => {
        axios
          .get("http://127.0.0.1:8000/api/list_produits")
          .then(res => this.setState({ produits: res.data }))
          .catch(err => console.log(err));
      };
      componentDidMount() {
        this.refreshList();
      }

      
      toggle = () => {
        this.setState({ modal: !this.state.modal });
      };
      handleSubmit = item => {
        this.toggle();
        
        axios
          .post("http://localhost:8000/api/panier/", item)
          .then(res => this.refreshList());
      };
      createItem = () => {
        const item = { nomprenom : "",
        carte_fidelite : "",
      };
        this.setState({ activeItem: item, modal: !this.state.modal });
      };
      render() {
        return (
          
          
              <Modal
                activeItem={this.state.activeItem}
                toggle={this.toggle}
                onSave={this.handleSubmit}
              />
          
            
              
          
          

          
        );
      }
    }
    export default Caddie;