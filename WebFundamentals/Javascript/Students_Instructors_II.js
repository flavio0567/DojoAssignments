var users = {
 'Students': [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 };

// Printing Students information

console.log("Students");
var item=1;
var i = 0;
    
 for (var Player in users.Students) {
  player_first_name = users.Students[i].first_name;
  player_last_name = users.Students[i].last_name;
  
   console.log(item + " - " + player_first_name + " " +
             player_last_name + " - " +
             (users.Students[i].first_name.length +
              users.Students[i].last_name.length));
  item++;
  i++;
 }

// Printing Instructors information

console.log("Instructors");
var item=1;
var i = 0;
 
 for (var Instructors in users.Instructors) {
  instructor_first_name = users.Instructors[i].first_name;
  instructor_last_name = users.Instructors[i].last_name;
  
   console.log(item + " - " + instructor_first_name + " " +
             instructor_last_name + " - " +
             (users.Instructors[i].first_name.length +
              users.Instructors[i].last_name.length));
  item++;
  i++;
 }

// end coding
