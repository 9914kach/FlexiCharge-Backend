const WebSocket = require('ws')
const connectedChargers = []

module.exports = function({clientHandler}) {

    exports.startServer = function() {
        console.log("Starting OCPP server")
        const wss = new WebSocket.Server({ port: 1337 })
        
        wss.on('connection', function connection(ws, req) {
            
            // Get the charger's serial number:
            let origin = req.url
            let originArray = origin.split("/")
            let chargerSerial = originArray[originArray.length - 1]          

            // Validate and handle connecting charger:
            clientHandler.handleConnection(ws, chargerSerial, connectedChargers)
            
            ws.on('close', function disconnection(){
                connectedChargers.splice(ws)
                console.log("Disconnected from charger with ID: " + chargerSerial)
                console.log("Number of connected chargers: " + connectedChargers.length)
            })
        })
    }
    return exports
}

function getKeyByValue(object, value) {
    return Object.keys(object).find(key => object[key] === value);
  }