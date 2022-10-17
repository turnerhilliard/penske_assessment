import React from 'react';
import 'bulma/css/bulma.min.css';

class Upload extends React.Component {
    constructor(props) {
    super(props);

    this.state = {
        newFile: '',
    };
    
    this.handleUploadImage = this.handleUploadImage.bind(this);
    }

    handleUploadImage(ev) {
        ev.preventDefault();
        const data = new FormData();
        data.append('file', this.uploadInput.files[0]);
        this.setState({newFile: this.uploadInput.files.item(0).name}) 
        
        const fileName = this.uploadInput.files.item(0).name

        fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: data
        }).then((response) => {
            response.json().then((body) => {
            });
        });
        fetch('http://127.0.0.1:5000/filename', {
            method: 'POST',
            body: JSON.stringify({ fileName })
        }).then((response) => {
            response.json().then((body) => {
            });
        });
        window.location.reload()
    }
    
    render() {
        return (
    <form onSubmit={this.handleUploadImage}>
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