const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

// Abrir el sockett
io.on('connection', (socket) => {
    console.log('a user connected');
    socket.on('rv', (msg) => {
        console.log('message: ', msg);
    });
});
//Conectar servidor
app.get('/', (req, res) => {
    res.send('Hello world');
});
app.get('/conectar', (req, res) => {
    res.send('Hello world');
});

//Desconectar servidor
app.get('/desconectar', (req, res) => {
    socket.on('disconnect', () => {
        console.log('user disconnected');
    });
    res.send('Desconectado');
});

//Escuchando
server.listen(3000, () => {
    console.log('listening on *:3000');
});

// https://github.com/miguelgrinberg/python-socketio/blob/main/examples/client/asyncio/fiddle_client.py