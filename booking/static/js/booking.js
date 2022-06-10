document.addEventListener('DOMContentLoaded', () => {

   if(document.getElementById('id_booking_date')) {
      const datePicker = document.getElementById('id_booking_date');

      // Setup date calender
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
   }

   if(document.getElementsByClassName('messages')[0]) {
      const messages = document.getElementsByClassName('messages')[0];
      const messageItems = messages.children;
      console.log(messageItems.length);

      for (let i = 0; i < messageItems.length; i++) {
         if (messageItems[i].innerHTML == 'Booking Successful!') {
            setTimeout(() => {
               messageItems[i].style.display = 'none';
            }, 5000)
         }
      }
   }
   })
