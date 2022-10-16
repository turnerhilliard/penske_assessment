import React from 'react';
import DataViewer from './components/DataViewer';
import Header from './components/Header';
import 'bulma/css/bulma.min.css';
import Upload from './components/FileUpload';

function App() {
  return (
    <div>
      <Header />
      <Upload />
      <DataViewer/>
    </div>
  );
}

export default App;