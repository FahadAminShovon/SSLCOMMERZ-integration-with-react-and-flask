import React, { useState } from 'react';
import Axios from 'axios';
import { useHistory } from 'react-router-dom';


const Payment = () => {

    const [name, setName] = useState("Fahad");
    const [credit, setCredit] = useState(1000);
    const history = useHistory()
  
    const handleSubmit = (e) => {
      e.preventDefault()
      const data = {
        name, credit
      }
      Axios.post('/get-ssl-session', data)
      .then(resp=>{
        window.location.replace(resp.data.gatewayPageUrl);
        // window.location.replace(resp.gatewayPageUrl);
      })
      .catch(err=>{
        console.log(err.response)
      })
    }

    return ( 
        <div className="payment">
        <form>
        <div className="form-group">
          <input type="text" value={name} placeholder={"Enter customer name"}
            onChange = {(e)=>setName(e.target.value)}
          />
        </div>

        <div className="form-group">
          <input type="number" value={credit} placeholder={"Enter Credit"}
            onChange = {e => setCredit(e.target.value)}
          />
        </div>

        <div className="BDT">
         <h3>Pay Tk {credit} BDT</h3>
        </div>

        <div className="form-group">
          <button onClick = {handleSubmit}>Checkout</button>
        </div>

        </form>
      </div>
     );
}
 
export {Payment};