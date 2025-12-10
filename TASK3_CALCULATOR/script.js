let input = document.getElementById("first");
let buttons = document.querySelectorAll("button");

let expression = "";

buttons.forEach(btn =>{
    btn.addEventListener('click',() =>{
       let value = btn.textContent;
        if(value==="AC")
        {
         expression = "";
         input.value = "";
        }
        else if(value==="DEL"){
            expression=expression.slice(0,-1);
            input.value=expression;
        }
        else if(value==="="){
            try{
                expression=eval(expression);
                input.value=expression;
            }
            catch{
                input.value = "error";
                expression = " ";
            }

        }
        else{
            expression += value;
            input.value = expression;
        }
    });
});