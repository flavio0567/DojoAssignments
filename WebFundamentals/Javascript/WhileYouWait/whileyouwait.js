function daysUntilMyBirthday(days) {
  for (var num = days; num >=0; num--) { 
 
    if (num === 0) {
      console.log('♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*');
      console.log('♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪');
      console.log(' *•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«');
      break;
    }
  
    if (num > 30) {
        console.log(num + 'days until my birthday. Such a long time... :(')
    } else {
        console.log(num + 'DAYS UNTIL MY BIRTHDAY!!!');
    }  
  }
}
var days = 60;
daysUntilMyBirthday(days);
