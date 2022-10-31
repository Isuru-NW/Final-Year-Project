import React, { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import "./App.css";
import axios from 'axios'
import "../src/"
import { useForm } from "react-hook-form";

function App() {
  const [name, setName] = useState(0);
  const [startDate, setStartDate] = useState(new Date());
  const [price, setPrice] = useState(null);

  function GetUsers() {
    axios.post('http://127.0.0.1:5000/prediction', {
      "deaths" : name,
      "timestamp" : Math.floor(startDate/1000) 
    },)
    .then(function (response) {
      const price = response.data;
      setPrice(price)
      console.log(price);
    })
    .catch(error => {
      if (!error.response) {
          // network error
          console.log('Error: Network Error');
      } else {
          console.log("err",error.response.data);
      }
    })
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(name);
    console.log(startDate)  ;
    console.log(Math.floor(startDate/1000));
    console.log(price);
  }  

  return (
    <div className="App-header">
    <form onSubmit={handleSubmit}>
      <center><h1>BITSCAPE</h1></center>
      <center>
      <label>Enter number of Deaths:<br/>
        <input 
          type="text" 
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      </center>
       <center> 
        Select Date:
          <DatePicker selected={startDate} onChange={(date) => setStartDate(date)}/>
      </center> 
      
      <center><input type="submit" value="Predict" onClick={GetUsers}/></center>
      <center>
          <div id ="PricePredictor"> {price} USD</div>
      </center>
    </form>
    </div>
  )
}

export default App;
