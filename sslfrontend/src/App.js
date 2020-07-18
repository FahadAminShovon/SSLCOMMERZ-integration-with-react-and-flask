import React from 'react';
import './App.css';
import { Payment, Ipn, Success, Fail, Cancel } from './components';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="App">
          <Switch>
            <Route exact path="/">
              <Payment />
            </Route>
            <Route path="/ipn">
              <Ipn />
            </Route>
            <Route path="/success">
              <Success/>
            </Route>
            <Route path="/fail">
              <Fail/>
            </Route>
            <Route path="/cancel">
              <Cancel/>
            </Route>
          </Switch>
      </div>
    </Router>
  );
}

export default App;
