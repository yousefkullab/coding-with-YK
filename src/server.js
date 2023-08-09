const express = require("express");

const app = express();
const port = 3000;
const bodyParser = require("body-parser");
const People = require('./client/index')

app.use(bodyParser.json());

// Test Your API use Postman ( https://www.postman.com )
// nodemon >>> use to rest the server auto use this command ( npx nodemon fileName.js )
// GET, POST, PUT, DELETE

app.get('/', (req, res)=>{
    res.send("Welcome to Express");
});

app.get('/people', (req, res)=>{
    res.send(People.findAll());
});

app.get('/people/:personId', (req, res)=>{
    const personId = parseInt(req.params.personId, 10);
    const person = People.findOne(personId);

    if (!person){
        res.status(404).send({
            message: "Can not find this person with this"
        });
        return;    
    }
    res.send(person);
});

app.post('/people',(req, res)=>{
    // middleware >>> body-parser
    res.send(People.create(req.body));
});

app.put('/people/:personId', (req, res)=>{
    const personId = parseInt(req.params.personId, 10);
    const updatedPerson = People.update(personId, req.body);
    if (!updatedPerson){
        return res.status(404).send({
            message: "The book you want to update does not exist"
        });
    }
    res.send(updatedPerson);
});

app.delete('/people/:personId', (req, res) =>{
    const personId = parseInt(req.params.personId, 10);
    const person = People.findOne(personId);

    if(!person){
        return res.status(404).send({
            message: "The person you want delete does not exist"
        });
    }

    const deletedPerson = People.destroy(personId);
    if (deletedPerson !== null){
        return res.sendStatus(204);
    }
    res.status(500).send({
        message: 'Could not delete the person'
    });
});

app.listen(port, () => {
    console.log(`Express server is now listening on port ${port}`)
});


