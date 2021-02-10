import React from "react"
import "./App.css"
import Visualize from "./Visualize"
import {Fab} from "@material-ui/core";
import {NavigateNext} from "@material-ui/icons";


class App extends React.Component {


  constructor(props){
    super(props)
    this.state = {
      index:-1,
      particles:[]
    }
  }

  fetchData = () => {
    fetch("http://localhost:8080/api/data",{
      mode:"cors",
    })
        .then(result => result.json())
        .then(resultJson => this.setState(resultJson))
  }

  componentDidMount(){

    this.fetchData()
  }

  render(){

    const {index,particles} = this.state
    return <div className={"App-container"}>
        <header className="App-header">
          <h2>{index}</h2>
          <Fab onClick={this.fetchData} color="primary" aria-label="add">
            <NavigateNext />
          </Fab>
        </header>
        <Visualize data={particles}></Visualize>
    </div>
  }

}



export default App;
