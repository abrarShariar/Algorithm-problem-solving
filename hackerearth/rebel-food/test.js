function hack(){
       var myvar;
       console.log(myvar);
   }

   function hacker(){
       var myvar=2;
       console.log(myvar);
       hack();
   }
   var myvar=5;
   console.log(myvar);
   hacker();
   console.log(myvar);
