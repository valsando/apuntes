//a PROBLEMAS CONDICIONALES

/*
1) Un hombre desea saber cuanto dinero se genera 
por concepto de intereses sobre la cantidad que tiene 
en inversión en el banco. El decidirá reinvertir los intereses 
siempre y cuando estos excedan a $7000, y 
en ese caso desea saber cuanto dinero tendrá finalmente en su cuenta.

*/

"use scrict"
function ej1(){
    var p_int=0.0;
    var cap=0;

    /** SE  DECIDIRA INVERTIR LOS INTERESES *** */
    document.writeln("SE  DECIDIRA INVERTIR LOS INTERESES")
    p_int= parseInt(prompt("digite la cantidad del interes"));
    cap= parseInt(prompt("digite la cantidad de la inversion en el banco"));
    int=(cap * p_int);
    document.writeln("el valor de "+cap+" * "+p_int+"es igual a:"+int);
    if (int>7000) {
    //verdad
    alert("se invierte");
    } else {
        //falso
        
    
    alert("no se invierte");
    }

    capif=cap*int
    document.writeln("el dinero que tendra finalmente en su cuenta"+cap+" * "+ int +"es iagual a:"+ capif);
}



/*2) Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara 
si su promedio de tres calificaciones es mayor o igual 
a 70; reprueba en caso contrario.
*/
function ej2(){
var calif1=0;
var calif2=0;
var calif3=0;
calif1= parseInt(prompt("digite la nota 1"));
calif2= parseInt(prompt("digite la nota 2"));
calif3= parseInt(prompt("digite la nota 3"));
prom= (calif1+calif2+calif3)/3
document.writeln("el valor de las calificaciones"+(calif1+"+"+calif2+"+"+calif3)+"/"+3+"esigual a:"+prom);
  
if (prom>=70) {
    alert("alumno aprobado");
    
} else {
    alert("alumno reprobado");
    
  
}
}



/*
3) En un almacén se hace un 20% de descuento
 a los clientes cuya compra supere los $1000 ¿ Cual será la cantidad que pagara una persona por su compra?

*/
function ej3(){
var compra=0;
var desc=0.20;
compra= parseInt(prompt("digite el valor de la compra"));


if (compra>1000) {
    alert("cantidad a pagar por su compra es igual a:"+(desc=compra*0.20+" aplica el descuento"));
} else {
    alert("cantidad a pagar por su compra es igual a:"+(tot_pag=compra-desc+"no aplica descuento"));
}
}


/*4) Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:
Si trabaja 40 horas o menos se le paga $16 por hora
Si trabaja mas de 40 horas se le paga $16 por cada una de las primeras 40 horas y
$20 por cada hora extra.
*/
function ej4(){
var horast=0;
horast= parseInt(prompt("digite el numero de horas trabajadas"));
he=horast-40;

if (horast>40) {
    alert("su salario semanal es igual a:"+(he*20+40*16));
} else {
    alert("su salario semanal es igual a:"+(horast*16));
}
}



/*
5) Un hombre desea saber cuanto dinero se genera por concepto de intereses 
sobre la cantidad que tiene en inversión en el banco. El decidirá reinvertir 
los intereses siempre y cuando estos excedan a $7000, y en ese caso desea saber 
cuanto dinero tendrá finalmente en su cuenta*/
//ejercicio repetido

/*6) Que lea dos números y los imprima en forma ascendente Inicio
*/
function ej6(){
var nun1=0;
var nun2=0;
num1= parseInt(prompt("digite el numero 1"));
num1= parseInt(prompt("digite el numero 2"));

if (num1<nun2) {
    alert(num1,nun2);
} else {
    alert(num1,nun2);
}
}

/*7) Una persona enferma, que pesa 70 kg, se encuentra en reposo y desea saber
 cuantas calorías consume su cuerpo durante todo el tiempo que realice una misma actividad. 
 Las actividades que tiene permitido realizar son únicamente dormir o estar sentado en reposo. 
 Los datos que tiene son que estando dormido consume 1.08 calorías por minuto y estando sentado 
 en reposo consume 1.66 calorías por minuto.*/
function ej7(){
var nombredelpaciente=0;
var actividad= 0;
var dormir= 1;
var sentado=2;
var tiemp=0;
nombredelpaciente=parseInt(prompt("ingrese el nombre  "));
actividad=parseInt(prompt("digite la actividad "));
tiemp=parseInt(prompt("digite el tiempo de la actividad "));
cg=1.08*tiemp;
cg2=1.66+tiemp;
if (actividad = 1) {
    alert("el numero de calorias es igual a:"+(cg=1.08*tiemp));
    
} else {
    alert=(actividad=2);
    alert("el numero de calorias es igual a:"+(cg2=1.66*tiemp));
}
}


/*8) Hacer un algoritmo que imprima el nombre de un articulo, clave, precio original 
y su precio con descuento. El descuento lo hace en base a la clave, si la clave es 01 el descuento
 es del 10% y si la clave es 02 el descuento en del 20% (solo existen dos claves).
*/
function ej8(){
var nombre=0;
var cve=0;
var prec_original=0;
nombre= parseInt(prompt("digite el nombre del articulo"));
cve= parseInt(prompt("digite la clave"));
prec_original= parseInt(prompt("digite el precio original"));
precio_desc=((prec_original*0.10)-prec_original);
precio_desc2=((prec_original*0.20)-prec_original);

if (cve=01) {
    alert("precio con descuento igual a:"+(precio_desc=(prec_original*0.10)-prec_original));
} else {
    alert(cve=02);
    alert("precio con descuento igual a:"+(precio_desc2=(prec_original*0.20)-prec_original));
}


document.writeln("el nombre del articulo es de:"+nombre);
document.writeln("la clave es igual a:"+cve);
document.writeln("el precio original del articulo es de:"+prec_original)
document.writeln("el precio con descuento es de: "+precio_desc+precio_desc2)

}

/*
9) Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o mas
 se aplica un descuento del 20% sobre el total de la compra y si son menos de tres
  camisas un descuento del 10%
  */
function ej9(){
  var num_camisas=0;
  var prec=0;
  camisas= parseInt(prompt("numero de camisas compradas"));
  prec=parseInt(prompt("precio  de  todas las camisas compradas"));
 

  if (num_camisas => 3) {
      alert((prec*0.20)-prec);
  } else {
      alert((prec*0.10)-prec);
  }
  
}




 /*

10) Una empresa quiere hacer una compra de varias piezas de la misma clase a una fabrica de refacciones.
 La empresa, dependiendo del monto total de la compra, decidirá que hacer para pagar al fabricante.
Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad 
de invertir de su propio dinero un 55% del monto de la compra, pedir prestado
 al banco un 30% y el resto lo pagara solicitando un crédito al fabricante.
Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad de invertir de su propio dinero un 70% 
y el restante 30% lo pagara solicitando crédito al fabricante.
El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.
*/
function ej10(){
var costopza=0;
var numpza=0;
var totcomp=0;
var credito=0;
costopza=parseInt(prompt("digite el  monto total de la compra"));
numpza=parseInt(prompt("digite el  numero de piezas compradas"));
alert(totcomp=(costopza*numpza));

if (totcomp>500000) {
    alert("cantidad invertida igual a:"+ (totcomp*0.55 ));
    alert("prestamo igual a:"+(totcomp*0.30));
    alert("credito igual a:"+(credito=(totcomp*0.15)));
} else {
    alert("cantidad invertida igual a:"+(totcomp *0.70));
    alert("credito igual a:"+(credito =(totcomp * 0.30)));
}
alert("interes igual a:"+((credito*0.20)));

}

/*
1) Calcular el total que una persona debe pagar en un llantera, 
si el precio de cada llanta es de $800 si se compran menos de 5 llantas y de $700 si se compran 5 o mas
.*/
function eje1(){
var numllantas=0;
numllantas=parseInt(prompt("digite el  numero de llantas"));
if (numllantas<5) {
    alert("el precio de la llanta es igual a:"+(800));
} else {
    alert("el precio de la llanta es igual a:"+(700));
}
}


/*
2) En un supermercado se hace una promoción, 
mediante la cual el cliente obtiene un descuento dependiendo de un numero que se escoge al azar.
 Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra, 
 si es mayor o igual a 74 el descuento es del 20%. 
 Obtener cuanto dinero se le descuenta.
 */
function eje2(){
var valorcompra=0;
var numero=0;
valorcompra=parseInt(prompt("digite el valor de la compra"));
numero=parseInt(prompt("digite el  numero "));
dineodesc=valorcompra*0.15;
dinerodesc2=valorcompra*0.20;
if (numero<74) {
    alert("descuento igual a:"+(0.15));
    alert("dinero que se le descuenta igual a:"+(valorcompra*0.15));
} else {
    alert("descuento igual a:"+(0.20));
    alert("dinero que se le descuenta igual a:"+(valorcompra*0.20));
}
}
 /*
3) Calcular el numero de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aerobico;
 la formula que se aplica cuando el sexo es femenino es:
num. pulsaciones = (220 - edad)/10
 y si el sexo es masculino:
num. pulsaciones = (210 - edad)/10 
*/
function eje3(){
var sexo=0;
var edad=0;
var femenino=1.1
var masculino=2.2
edad=parseInt(prompt("digite la edad"));
sexo=parseInt(prompt("digite el sexo"));

if (sexo=1.1) {
    alert("numero de pulsaciones igual a:"+(2020-edad)/10)
} else {
    alert("numero de pulsaciones igual a:"+(2010-edad)/10)
}
}
/*
4) Una compañía de seguros esta abriendo un depto.
 de finanzas y estableció un programa para captar clientes,
  que consiste en lo siguiente: Si el monto por el que se efectúa la fianza es menor que $50 000
 la cuota a pagar será por el 3% del monto,
   y si el monto es mayor que $50 000 la cuota a pagar será el 2% del monto. 
   La afianzadora desea determinar cual será la cuota que debe pagar un cliente.*/
function eje4(){
   var monto=0;
   monto=parseInt(prompt("ingrese el monto efectuado"));
   
   if (monto<50000) {
       alert((monto*0.03)-monto);
   } else {
    alert((monto*0.02)-monto);
   }
   
}



   /*
5) En una escuela la colegiatura de los alumnos se determina según el numero de materias que cursan. 
El costo de todas las materias es el mismo.
Se ha establecido un programa para estimular a los alumnos,
 el cual consiste en lo siguiente: si el promedio obtenido por un alumno en el ultimo periodo es
  mayor o igual que 9,
  se le hará un descuento del 30% sobre la colegiatura y no se le cobrara IVA; 
  si el promedio obtenido es menor que 9 deberá pagar la colegiatura completa,
   la cual incluye el 10% de IVA.
Obtener cuanto debe pagar un alumno.*/
function eje5(){
var valorcolegiatura=0;
var promedioalum=0;
promedioalum=parseInt(prompt("ingrese el promeddio "));
valorcolegiatura=parseInt(prompt("ingrese el valor de la colegiatura "));
valorcolegiatura1=((valorcolegiatura*0.30)-valorcolegiatura)

if (promedioalum >= 9) {
    alert((valorcolegiatura*0.30)-(valorcolegiatura*0.10)-valorcolegiatura);
    
} else {
    alert("debe pagar la colegiatura completa igual a:"+(valorcolegiatura))
}

}
/*
6) Una empresa de bienes raíces ofrece casas de interés social,
 bajo las siguientes condiciones: Si los ingresos del comprador son menores de $8000 el enganche 
 será del 15% del costo de la casa y el resto se distribuirá en pagos mensuales, a pagar en diez
 años. S
 si los ingresos del comprador  mas de $8000  el enganche será del 30% del costo de la casa 
 y el resto se distribuirá en pagos mensuales a pagar en 7 años.
La empresa quiere obtener cuanto debe pagar un comprador por concepto de enganche
 y cuanto por cada pago parcial.

*/
function eje6(){
var vcasa=0;
var ingresos=0;
var enganche=0;
var tiempo=0;
var cuota=0;
ingresos=parseInt(prompt("digite el valor de los ingresos mensuales"));
if (ingresos < 8000) {
    alert("enganche sera igual a:"+( 0.15));
  tiempo=10*12
    alert("por concepto de enganche que paga es igual a:"+(ingresos*0.15)+ingresos);
} else {
    alert("enganche sera igual a:"+( 0.30));
    tiempo=7*12
    alert("por concepto de enganche que paga es igual a:"+(ingresos*0.30));
}

cuota=(vcasa-enganche)/tiempo;
}
 /*
 
 7) El gobierno ha establecido el programa SAR 
 (Sistema de Ahorro para el Retiro) 
 que consiste en que los dueños de la empresa deben obligatoriamente depositar en una cuenta bancaria 
 un porcentaje del salario de los trabajadores;
  adicionalmente los trabajadores pueden solicitar a la empresa 
  que deposite directamente una cuota fija o un porcentaje de su salario en la cuenta del SAR,
   la cual le será descontada de su pago.
Un trabajador que ha decidido aportar a su cuenta del SAR 
desea saber la cantidad total de dinero que estará depositado a esa cuenta cada mes,
 y el pago mensual que recibirá.*/
function eje7(){
var salariom=0;
var SAR =0;
var opcion=0;
var opcioncuotafija= 1;
var opcionporcentaje= 2;
salariom=parseInt(prompt(" ingrese su salario"));
opcion=parseInt(prompt(" ingrese cual opcion es de su preferencia"));


if (opcion=1) {
    alert(opcioncuotafija=parseInt(prompt(" ingrese la cuota fija para el SAR")));
     alert( "pago mensual es igual a:"+(salariom-opcioncuotafija));
} else {
    alert(opcion=2)
    alert(opcionporcentaje=parseInt(prompt(" ingrese el porcentaje para el SAR" )));
    alert(SAR=(salariom * opcionporcentaje)/100);
    alert("la cantidad de dinero que deposita cada mes para SAR es igual a:"+SAR);
alert("su pago mensul es igual a:"+(salariom -opcionporcentaje));

}
}
 /*

8) Una persona desea iniciar un negocio, 
para lo cual piensa verificar cuanto dinero le prestara el banco por hipotecar su casa. 
Tiene una cuenta bancaria,
 pero no quiere disponer de ella a menos que el monto por hipotecar su casa sea muy pequeño.
  Si el monto de la hipoteca es menor que $1 000 000 entonces invertirá el 50% de la inversión total
   y un socio invertirá el otro 50%. Si el monto de la hipoteca es de $ 1 000 000 o mas,
   entonces invertirá el monto total de la hipoteca y el resto del dinero que 
   se necesite para cubrir la inversión total se repartirá a partes iguales entre el socio y el.
 
 
 */
function eje8(){
var nombrep=0;
var  valorhptc=0;
var val=0;
valorhptc=parseInt(prompt("digite el valor de la hipoteca"));
if (valorhptc<=1000000) {
alert(val=(+valorhptc*0.50));
} else {
alert(val=(+valorhptc*0.10));
}
alert("el dinero que tiene para la empresa igual a:"+(val))

}
  /* 9) El gobierno del estado de México desea reforestar un bosque que mide determinado numero de hectáreas. 
  Si la superficie del terreno excede a 1 millón de metros cuadrados,
 entonces decidirá sembrar de la sig. manera: Porcentaje de la superficie del bosque
70% 20% 10%
Tipo de 
árbol pino
oyamel 
cedro
Si la superficie del terreno es menor o igual a un millón de metros cuadrados,
entonces decidirá sembrar de la sig. manera: Porcentaje de la superficie del bosque
50% 30% 20%
Tipo de árbol pino
oyamel 
cedro
El gobierno desea saber el numero de pinos, 
oyameles y cedros que tendrá que sembrar en el bosque,
 si se sabe que en 10 metros cuadrados caben 8 pinos, 
 en 15 metros cuadrados caben 15 oyameles y en 18 metros cuadrados caben 10 cedros. 
 También se sabe que una hectárea equivale a 10 mil metros cuadrados.*/
 function eje9(){
var hectariaterreno=0;
var pino1=0.7;
var oyamel1=0.2;
var cedro1=0.1;
var pino2=0.5;
var oyemal2=0.3;
var cedro=0.2;
metros=hectariaterreno*10000
hectariaterreno=parseInt(prompt("ingrese el numero  de hectareas de la superficie del terreno"));
alert(metros=(hectariaterreno*10000));
if (hectariaterreno>1000000) {
    alert("numero de  pino sera igual a:"+(metros * pino1));
    alert("numero  de oyemal sera igual a:"+(metros * oyamel1 ));
    alert("numero de cedro sera igual a:"+(cedro1 * cedro1));
} else {
    alert("numero de  pino sera igual a:"+( metros* pino2));
    alert("numero de  oyemal sera igual a:"+(metros * oyemal2 ));
    alert("numero de  cedro sera igual a:"+(metros * cedro));
}
 }
/*
10) Una fabrica ha sido sometida a un programa de control de contaminación para lo cual se efectúa una revisión
 de los puntos IMECA generados por la fabrica. 
 El programa de control de contaminación consiste en medir los puntos IMECA 
 que emite la fabrica en cinco días de una semana y si el promedio es superior a los 170 puntos entonces
 tendrá la sanción de parar su producción por una semana y una multa del 50%
de las ganancias diarias cuando no se detiene la producción.
Si el promedio obtenido de puntos IMECA es de 170 o menor entonces no tendrá ni sanción ni multa.
 El dueño de la fabrica desea saber cuanto dinero perderá después de ser sometido a la revisión.
 */
 function eje10(){
var nomfabrica=0;
var puntosIMECA=0;
var ganaciasd=0;
nomfabrica=parseInt(prompt("ingrese el nombre de la fabrica"));
puntosIMECA=parseInt(prompt("ingrese los puntos IMECA generados por la fabrica"));

if (puntosIMECA>170) {
    alert("tendra sancion de parar su produccion por una semana");
    alert("se le descontara 0.50 de las ganancias diarias")
    alert(ganaciasd=parseInt(prompt("ingrese sus ganancias diarias")));
    alert("dinero que perdera es igual a:"+ganaciasd*0.50)
} else {
    alert("no tendra ni sancion ni multa");
}
 }




/*
11) Una persona se encuentra con un problema de comprar un automóvil o un terreno,
 los cuales cuestan exactamente lo mismo. 
 Sabe que mientras el automóvil se devalúa,
  con el terreno sucede lo contrario.
 Esta persona comprara el automóvil si al cabo 
 de tres años la devaluación de este no es mayor que la mitad del incremento del valor del terreno. 
 Ayúdale a esta persona a determinar si debe o no comprar el automóvil.
 */

function eje11(){
 var precioterreno=0;
 var precioautomovil=0;
 var incrementoAT=0;
 var devaluacionAa=0;
 var incremento=0;
 var decremento00;
precioterreno=parseInt(prompt("ingrese el precio del terreno"));
precioautomovil=parseInt(prompt("ingrese el precio del automovil"));
incrementoAT=parseInt(prompt("ingrese el incremento anual del terreno"));
devaluacionAa=parseInt(prompt("ingrese la devaluacion anual del automovil"));

alert(((incremento=(precioterreno *incrementoAT)/100)*3)/2);
alert((decremento=(precioautomovil*devaluacionAa)/100)*3)
alert("la mitad del incremento de la casa en 3 años es igual a:"+incremento);
alert("la devaluacion del automovil e4n 3 años es igual a:"+decremento);


if (decremento<incremento) {
    alert("te convine comprar el automovil")
} else {
    alert("te conviene comprar el terreno")
}}