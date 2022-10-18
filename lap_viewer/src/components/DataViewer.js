import '../App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../datatable.css';
import 'bulma/css/bulma.min.css';

function DataViewer() {
  const [message, setGetMessage] = useState({})
  const [fileName, setFileName] = useState({})
  const [sector, setSector] = useState({})
  const eventName = fileName.data?.event
  const sessionName = fileName.data?.session

  useEffect(()=>{
    axios.get('http://127.0.0.1:5000/upload').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })
    axios.get('http://127.0.0.1:5000/sector').then(response => {
      console.log("SUCCESS", response)
      setSector(response)
    }).catch(error => {
      console.log(error)
    })
    axios.get('http://127.0.0.1:5000/filename').then(response => {
      console.log("SUCCESS", response)
      setFileName(response)
    }).catch(error => {
      console.log(error)
    })
  }, [])

  const Pagenaud = ({ children }) => {
    const styleProps = {
      style: {
        background: 'orange',
        color: 'white'
      }
    };
    return children(styleProps);
  }

  const Newgarden = ({ children }) => {
    const styleProps = {
      style: {
        background: 'red',
        color: 'white'
      }
    };
    return children(styleProps);
  }

  const Castroneves = ({ children }) => {
    const styleProps = {
      style: {
        background: 'green',
        color: 'white'
      }
    };
    return children(styleProps);
  }

  const Power = ({ children }) => {
    const styleProps = {
      style: {
        background: 'blue',
        color: 'white'
      }
    };
    return children(styleProps);
  }

  const ifPenskeDriver = (input) => {
  
    if (input === 3) {
      return (
        <Pagenaud>
          {(props) => <td {...props}>{input}</td>}
        </Pagenaud>
      )
    } else if(input === 1) {
      return (
        <Newgarden>
          {(props) => <td {...props}>{input}</td>}
        </Newgarden>
      )
    } else if (input === 2) {
      return (
        <Castroneves>
          {(props) => <td {...props}>{input}</td>}
        </Castroneves>
      )
    } else if (input === 12) {
      return (
        <Power>
          {(props) => <td {...props}>{input}</td>}
        </Power>
      )
    }

    return <td>{input}</td>
  }

  // Conditionally render the data

  var isDataHereYet = ''
  if (eventName === undefined) {
    isDataHereYet = <br />
  }
  else {
    isDataHereYet = 
    <div>
    <div class="container">
        <div class="notification is-gray">
            <h1 class="title">{eventName}</h1>
            <h2 class="subtitle">{sessionName}</h2>
        </div>
      </div>
      <div class="container">
        <div class="level-item notification is-black">
            <table class="table notification is-primary">
                <thead>
                <tr>
                    <th>Position</th>
                    <th>CarNumber</th>
                    <th>LastName</th>
                    <th>Time</th>
                    <th>Lap</th>
                </tr>
                </thead>
                <tbody>
                {message.data?.map((data, i) => (
                        <tr key={i}>
                            <td>{i + 1}</td>
                            {ifPenskeDriver(data.CarNumber)}
                            <td>{data.LastName}</td>
                            <td>{data.Time}</td>
                            <td>{data.Lap}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            </div>
            </div>
            </div>
  }

  var sector_times = ''
  if (sector.data?.fastest === 0 || sector.data?.fastest === undefined) {
    sector_times = <br />
  }

  else {
    sector_times =
    <div>
    <div class="container">
              <div class="notification is-gray">
                <h1 class="title">Best Sector Times</h1>
                <h2 class="subtitle">Fastest Theoretical Time is: {sector.data?.fastest}</h2>
              </div>
            </div>
    <div class="container">
    <div class="notification is-black">
    <h1>{sector_times}</h1>
    <div class="level-item">
    <table class="table notification is-primary">
        <thead>
        <tr>
            <th>Sector</th>
            <th>CarNumber</th>
            <th>LastName</th>
            <th>Time</th>
            <th>Lap</th>
        </tr>
        </thead>
        <tbody>
        {sector.data?.times.map((data, i) => (
                <tr key={i}>
                    <td>{i + 1}</td>
                    {ifPenskeDriver(data.CarNumber)}
                    <td>{data.LastName}</td>
                    <td>{data.Time}</td>
                    <td>{data.Lap}</td>
                </tr>
            ))}
        </tbody>
    </table>
    </div>
  </div>
</div>
</div>
  }

  return (
  <>
    {isDataHereYet}
    {sector_times}
  </>
  );
}

export default DataViewer;