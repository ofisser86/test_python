/**
 * Created by greta on 13.07.17.
 */
var contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"]
    },
    {
        "firstName": "Harry",
        "lastName": "Potter",
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["Javascript", "Gaming", "Foxes"]
    }
];


function lookUpProfile(firstName, prop){
// Only change code below this line
for (var i =0; i < contacts.length; i++){
  for (var j=0; j< contacts[i].length; j++){
    if(contact.firstName[j] != firstName){
            return "No such contact";
    }
    else if(contact.likes[j] != prop){
      return contact.likes[j];
    }
    else{
      return contact.likes[j];

    }
    }

  }
// Only change code above this line
}

// Change these values to test your function
lookUpProfile("Akira", "likes");
