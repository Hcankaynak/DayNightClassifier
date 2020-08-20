import React, {Component, Text,StyleSheet} from 'react';
import "./App.css"
import axios from 'axios';


class FileUpload extends Component{
    state ={
        selectedFile : null,
        fileType: null,
        response : '',
        spinner : 0,
    }
    useEffect = (()=> {
        fetch("/api").then(res => {
            this.setState({response: res});
            console.log(res);
        })
    });
    fileSelectedHandler = event => {
        this.setState({
            selectedFile: event.target.files[0],
        })
    }
    fileUploadHandler = () => {
        this.setState({response: 5,spinner: 1})
        if(this.state.selectedFile){
            const fd = new FormData();
        fd.append('image',this.state.selectedFile,"hck");
        axios.post('/api',fd)
        .then(res => {
            console.log(res);
            this.setState({response:res.data.type});
            // response is here and assign it to state 
        }).catch(err => console.log(err));
        }

    }
    render()
    {
        return(
            <>
            <div className="Header" >
                <h1 className="HeaderText" >
                Day and Night Classifier
                </h1>
            </div>
            <div className="Body" >
            <input type="file" onChange={this.fileSelectedHandler}></input>
            
            <button onClick={this.fileUploadHandler} > Upload </button>
            <p> {this.state.response === 0 ? <p> Night </p> : <p> {this.state.response === 1 ? <p> Day </p> : <p> {this.state.spinner ? <p> Determining ..</p> : <p></p>} </p> } </p>} </p>
            </div>
            </>
        )
    }

}

export default FileUpload;