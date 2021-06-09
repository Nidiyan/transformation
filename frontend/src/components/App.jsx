import React from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import Form from './Form';

const styles = {
    position: 'absolute', 
    left: '50%', top: '50%',
    transform: 'translate(-50%, -50%)',
    backgroundColor: "aliceblue",
};

function App() {
    const res = axios.get('http://localhost:8000/getScripts/');

    return (
        <div style={ styles }>
            <h1>
                Transformation
            </h1>
            <Form />
        </div>
    );
}

export default App;