import '../App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../datatable.css';
import 'bulma/css/bulma.min.css';

function DataViewer() {
  const [message, setGetMessage] = useState({})
  const [fileName, setFileName] = useState({})
  const eventName = fileName.data?.event
  const sessionName = fileName.data?.session

  useEffect(()=>{
    // axios.get('http://127.0.0.1:5000/flask/hello').then(response => {
    axios.get('http://127.0.0.1:5000/upload').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
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

  const ConditionallyDecoratedContainerData = (input) => {
  
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

  return (
    <>
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
                    <th>CarNumber</th>
                    <th>LastName</th>
                    <th>Time</th>
                    <th>Flag</th>
                </tr>
                </thead>
                <tbody>
                {message.data?.map((data, i) => (
                        <tr key={i}>
                            {ConditionallyDecoratedContainerData(data.CarNumber)}
                            <td>{data.LastName}</td>
                            <td>{data.Time}</td>
                            <td>{data.Flag}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
      </div>
</>
  );
}

export default DataViewer;