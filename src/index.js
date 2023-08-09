let people = [
    {
        id: 1, 
        name: "Yousef"
    },
    {
        id: 2, 
        name: "Joseph"
    },
    {
        id: 3, 
        name: "Joba"
    },
]

let lastId = 3;

module.exports = {
    findAll(){
        return people;
    },
    findOne(id){
        return people.find(person => person.id === id);
    },
    create(person){
        const id = ++lastId;
        const newPerson = {
            id: id,
            name: person.name
        };
        people.push(newPerson);
        return newPerson
        lastId = newPerson.id;
    },
    update(id, person){
        const existPerson = people.find(person => person.id === id);

        if(!existPerson){
            return null
        }
        const updatedPerson = {
            id: existPerson.id,
            name: person.name
        }

        people= people.map(person =>{
            if (person.id === id){
                return updatedPerson;
            }
            return person;
        });

        return updatedPerson;
    },
    destroy(id){
        people = people.filter(person => person.id !== id);
        return id;
    }
};
