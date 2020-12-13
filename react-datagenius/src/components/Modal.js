import React, { Component } from "react";
    import {
      Button,
      Modal,
      ModalHeader,
      ModalBody,
      ModalFooter,
      Form,
      FormGroup,
      Input,
      Label
    } from "reactstrap";

    export default class CustomModal extends Component {
      constructor(props) {
        super(props);
        this.state = {
          activeItem: this.props.activeItem
        };
      }
      handleChange = e => {
        let { name, value } = e.target;
        const activeItem = { ...this.state.activeItem, [name]: value };
        this.setState({ activeItem });
      };
      render() {
        const { toggle, onSave } = this.props;
        return (
          <Modal isOpen={true} toggle={toggle}>
            <ModalHeader toggle={toggle}> creer panier </ModalHeader>
            <ModalBody>
              <Form>
                <FormGroup>
                  <Label for="nomprenom">nom</Label>
                  <Input
                    type="text"
                    name="nomprenom"
                    value={this.state.activeItem.nomprenom}
                    onChange={this.handleChange}
                    
                  />
                </FormGroup>
                <FormGroup>
                  <Label for="carte_fidelite">carte fidelite</Label>
                  <Input
                    type="text"
                    name="carte_fidelite"
                    value={this.state.activeItem.carte_fidelite}
                    onChange={this.handleChange}
                  />
                </FormGroup>
                
              </Form>
            </ModalBody>
            <ModalFooter>
              <Button color="success" onClick={() => onSave(this.state.activeItem)}>
                Save
              </Button>
            </ModalFooter>
          </Modal>
        );
      }
    }