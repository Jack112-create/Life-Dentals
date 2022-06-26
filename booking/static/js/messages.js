document.addEventListener('DOMContentLoaded', () => {

   if(document.getElementsByClassName('messages')[0]) {
      const messages = document.getElementsByClassName('messages')[0];
      const messageItems = messages.children;
      console.log(messageItems.length);

      for (let i = 0; i < messageItems.length; i++) {
         setTimeout(() => {
            messageItems[i].style.display = 'none';
         }, 5000)
      }
   }
   })
