import React from 'react';
import 'bulma/css/bulma.min.css';

class Upload extends React.Component {
    constructor(props) {
    super(props);

    this.state = {
        imageURL: '',
        swag: ''
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
    }

    handleUploadImage(ev) {
        ev.preventDefault();
        const data = new FormData();
        data.append('file', this.uploadInput.files[0]);
        this.setState({swag: this.uploadInput.files.item(0).name}) 
        
        const eventName = this.state.swag
        
        
        console.log(eventName)

        fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: data
        }).then((response) => {
            response.json().then((body) => {
                this.setState({ imageURL: response });
            });
        });

        // window.location.reload()
    }
    
    render() {
        return (
    <form onSubmit={this.handleUploadImage}>
        <br />
        <div class="container">
            

            
            <h1 class="title">Start by adding a file</h1>
           
            
            <div class="file">
            <label class="file-label">
                <input class="file-input" ref={(ref) => { this.uploadInput = ref; }} type="file"/>
                <span class="file-cta">
                    <span class="file-label">
                        Choose a file…
                    </span>
                </span>
            </label>
            <div>
                {this.state.swag}
            </div>
            </div>
            
                <button class="button is-light">Upload</button>

            
        </div>
        <br />
    </form>
        );
    }
}

export default Upload;