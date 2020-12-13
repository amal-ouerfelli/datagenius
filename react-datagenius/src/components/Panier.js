
    import React, { Component } from "react";
    
    import axios from "axios";
import ModalM from "./ModalM";


    class Panier extends Component {
      constructor(props) {
        super(props);
        this.state = {
          activeItem: {
          id_p : "",
   
          },
          paniers : []
        };
      }
      componentDidMount() {
        this.refreshList();
      }
      refreshList = () => {
        axios
          .get("http://127.0.0.1:8000/api/min_panier")
          .then(res => this.setState({ paniers: res.data }))
          .catch(err => console.log(err));
      };
     
      toggle = () => {
        this.setState({ modal: !this.state.modal });
      };
      createItem = () => {
        const item = { id_p:""
      };
      this.setState({ activeItem: item, modal: !this.state.modal });
      };

      render() {
        const {  paniers } = this.state;
        return (
          <section>
          <h2 > Ticket</h2>
              <ModalM
                paniers={paniers}
                
                
              />
              
            </section>
        );
      }
    }
    export default Panier;