const  fs  = require("fs");
(()=>{

    for (let i = 11; i <= 28 ; i++) {
        // <i know  this is a bad way to create files in a loop the callback will add up to the event loop increasing memory usesage
        fs.open(`./${i}-answer.txt`, "w", ()=>{}) 
        
    }

})()