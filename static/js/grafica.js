function Opcion(){
    var opciones = document.getElementById("opcion");
    var num = opcion.options[opcion.selectedIndex].value;
    console.log(num);        
    alert(num)     
    }
$(select[name="opcion"]).on('change', function(){
  alert('x');
})