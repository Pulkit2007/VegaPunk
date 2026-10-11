import './App.css'
import Header from './components/Header'
import FileUpload from './components/FileUpload'


export default function App(){
  return <main>
    <Header></Header>
    <div className='search-container'>
          <input className='search-input' type='text' placeholder='Ask Anything'></input>
          <button>Go</button>
    </div>
    <FileUpload onclick/>
  </main>
}