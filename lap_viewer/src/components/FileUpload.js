import React from 'react';
import axios from 'axios'
import 'bulma/css/bulma.min.css';

class Upload extends React.Component {
    constructor(props) {
    super(props);
    
    this.handleUploadFile = this.handleUploadFile.bind(this);
    }

    handleUploadFile(ev) {

        ev.preventDefault();

        const data = new FormData();
        data.append('file', this.uploadInput.files[0]);
        
        const fileName = this.uploadInput.files.item(0).name

        axios.post('http://127.0.0.1:5000/upload', data, {
            data
          })
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });

        axios.post('http://127.0.0.1:5000/filename', {
            fileName
          })
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });

        window.location.reload()
    }
    
    render() {
        return (
    <form onSubmit={this.handleUploadFile}>
        <br />
        <div class="container">
            <h1 class="title">Add a file</h1>
            <div class="file">
            <label class="file-label">
                <input class="file-input" ref={(ref) => { this.uploadInput = ref; }} type="file"/>
                <span class="file-cta">
                    <span class="file-label">
                        Choose a file…
                    </span>
                </span>
            </label>
            </div>
                <button class="button is-light">Upload</button>
        </div>
        <br />
    </form>
        );
    }
}

export default Upload;