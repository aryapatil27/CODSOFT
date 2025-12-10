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
document.addEventListener('keydown', (e) => {
    const key = e.key;
    if((key >= '0' && key <= '9') || key === '.' || key === '%' || key === '+' || key === '-' || key === '*' || key === '/'){
        expression += key;
        input.value = expression;
    }
    else if(key === 'Enter'){
        try{
            expression = eval(expression);
            input.value = expression;
        }
        catch{
            input.value = "error";
            expression = "";
        }
    }
    else if(key === 'Backspace'){
        expression = expression.slice(0,-1);
        input.value = expression;
    }
    else if(key.toLowerCase() === 'c'){ // clear on pressing C
        expression = "";
        input.value = "";
    }
});