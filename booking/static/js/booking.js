const datePicker = document.getElementById('id_booking_date');

let today = new Date();
let dd = today.getDate();
let mm = today.getMonth() + 1;
let yyyy = today.getFullYear();

if (dd < 10) {
   dd = '0' + dd;
}

if (mm < 10) {
   mm = '0' + mm;
} 
 
// Stops user from being able to choose a date in the past
today = yyyy + '-' + mm + '-' + dd;
datePicker.setAttribute("min", today);