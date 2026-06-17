function changeSize(size){

    localStorage.setItem("mobileSize", size);

    document.getElementById("a").style.width = size;
}

/* maximize */

function big(){

    document.getElementById("a").style.width = "95vw";
}

/* minimize */

function small(){

    document.getElementById("a").style.width = "320px";
}

/* keyboard support */

let keyinput = document.querySelector("#display");

keyinput.addEventListener("keydown", (event) => {

    console.log(event.key);

    if(event.key === "Enter"){
        event.preventDefault();

        document.getElementById("b").click();

        /* allow form submission */
    }
    if(event.key === "c"){
        event.preventDefault();
        document.getElementById("delall").click();
    }

});

/* page load */

window.onload = function(){

    /* restore selected mobile size */

    let savedSize = localStorage.getItem("mobileSize");

    if(savedSize){

        document.getElementById("a").style.width = savedSize;

        document.querySelector("select").value = savedSize;
    }
}

    /* restore cursor focus */
   window.onload = function(){

    let input = document.getElementById("display");

    if(input){

        input.focus();

        let len = input.value.length;

        input.setSelectionRange(len, len);
    }
   }
   let light ="white";
   let changebag= document.querySelector(".cal");
    changebag.addEventListener("click",()=>{
        
      if(light=="white"){
        light="black";
        document.querySelector("body").style.backgroundColor="black";
      }
      else if(light=="black"){
        light="white";
        document.querySelector("body").style.backgroundColor="white";
      }
    });
 let formulasheet = document.getElementById("formulasheet");
 formulasheet.addEventListener("change",function(){
    if(this.value){
       window.location.href = this.value
    }
 });

    
