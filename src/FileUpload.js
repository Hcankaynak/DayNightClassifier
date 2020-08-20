import React, {Component, useEffect} from 'react';
import axios from 'axios';


class FileUpload extends Component{
    state ={
        selectedFile : null,
        fileType: null,
        response : ''
    }
    useEffect = (()=> {
        fetch("/api").then(res => {
            this.setState({response: res});
            console.log(res);
        })
    });
    fileSelectedHandler = event => {
        this.setState({
            selectedFile: event.target.files[0]
        })
    }
    fileUploadHandler = () => {
        
        const fd = new FormData();
        fd.append('image',this.state.selectedFile,"hck");
        axios.get('/api',fd)
        .then(res => {
            console.log(res);
            this.setState({response:res.data});
            // response is here and assign it to state 
        });
        

    }
    render()
    {
        return(
            <>
            <div>Day and Night Classifier</div>
            <div>
            <input type="file" onChange={this.fileSelectedHandler}></input>
            
            <button onClick={this.fileUploadHandler} > Upload </button>
            {this.state.fileType ? this.state.fileType === 1 ? <p>File Type is day</p> : <p>file type is night</p> : <p>file type is determining...</p>}
            <p> A {this.state.response.name}</p>
            </div>
            </>
        )
    }

}


export default FileUpload;