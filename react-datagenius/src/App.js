
    import React, { Component } from "react";
    import "./App.css"
    import Caddie from "./pages/Caddie"
    import Produits from "./pages/Produits"
    import Navbar from"./components/Navbar"
    import Bienvenu from "./components/Bienvenu"
    import { Route, Switch, BrowserRouter as Router} from 'react-router-dom';
import Panier from "./components/Panier";
    
    class App extends Component {
      
      render() {
        return (
          <Router>
    <Navbar/>
    <Switch>
    <Route exact path="/caddie" component={Caddie}/>
    <Route exact path="/produits" component={Produits}/>
    <Route exact path="/" component={Bienvenu}/>
    <Route exact path="/mon_panier" component={Panier}/>
    
    </Switch>
    </Router>
  
          

          
        );
      }
    }
    export default App;