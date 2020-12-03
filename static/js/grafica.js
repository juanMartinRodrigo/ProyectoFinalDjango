function Opcion(){
    var opciones = document.getElementByName("id");
    var num = opcion.options[opcion.selectedIndex].value;
    console.log(num);        
    alert(num)     
    }
$(select[name="id"]).on('change', function(){
  alert('x');
})