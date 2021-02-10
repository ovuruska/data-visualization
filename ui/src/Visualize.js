import React from "react"
import Graph3D from 'react-graph3d-vis'

class Visualize extends React.Component {



    render(){

        const {data} = this.props

        console.clear()
        console.table(data,)

        if(data.length === 0)
            return null
        else
            return <Graph3D  data={data.map(([x,y,z,e]) => ({x,y,z,style:e}))}/>
    }
}

export default Visualize