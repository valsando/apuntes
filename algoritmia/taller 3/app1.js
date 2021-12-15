const ej1 = () => {
    let a = parseInt(document.getElementById("ej1").value)
    let c = a * 11000
    let b = 0
    if (a<5) {
        b = c *0.1
    } else if(a<10){
        b = c * 0.2
    } else{
        b = c * 0.4
        }
    alert("tu compra es de "+ c +" menos el descuento de "+ b +" es de "+ (c-b))
};
function ej2() {
    let a = parseInt(document.getElementById("ej2").value)
    let b = 0
    if (a<0){alert("nada")}
    else if (a<4) {b=300}
    else if (a<11) {b=250}
    else {b=200}
    alert("el precio de tus llantas es de " + b + " y el valor de tu compra es de " + (a*b))
}
function ej3() {
    let a = prompt("1. Colon descubrió América?")
    let b = prompt("2. La independencia de México fue en el año 1810?")
    let c = prompt("3. The Doors fue un grupo de rock Americano?")
    if ((a=="si")&&(b=="si")&&(c=="si")) {
        alert("felicidades, Has acertado correctamente las 3 preguntas")}
    else{alert("ups... sigue intentando hahahahah >:)")}
}
function ej4() {
    let a = parseInt(document.getElementById("1ej4").value)
    let b = document.getElementById("2ej4").value
    let descuento = 0
    let mensaje = ""
    if (a>2000) {descuento = a *0.1, mensaje = "descuento de precio\n"}
    if (b=="NOSY") {descuento = a*0.05, mensaje += "descuento de marca\n"}
    alert(mensaje + "el total a pagar por este estereo es de " + (a-descuento)*1.19)
}
function ej5() {
    let a = parseFloat(document.getElementById("1ej5").value);
    let b = parseFloat(document.getElementById("2ej5").value);
    descuento = 0
    if (a>10) {
        descuento= 0.2
    } else if (a>5) {
        descuento= 0.15
    } else if (a>2) {
        descuento= 0.1
    } 
    alert("con el descuento del " + (descuento*100)+"% " + "el precio para "+ a +" kilos es de " + b*(a*(1-descuento)))
}
function ej6() {
    let capital = parseFloat(document.getElementById("1ej6").value);
    let prestamo = 0;
    if (capital<0) {
        prestamo= 10000-capital
    } else if (capital<20000) {
        prestamo= 20000-capital} 
    if (prestamo !=0) {alert(`se ha pedido un prestamo de ${prestamo}`)}
    capital += prestamo
    capital-=7000
    let mid = capital/2
    alert(`de tu capital total, se destinaron\n5000 para equipo de computo\n2000 para mobiliario\n${mid} para la compra de insumos y ${mid} para insentivos al personal`)
}
function ej7() {
    let edad = 12*parseFloat(document.getElementById("1ej7").value) + parseFloat(document.getElementById("1ej72").value);
    let hemoglobina = parseFloat(document.getElementById("2ej7").value);
    let a = false
    alert("webos"+edad)
    if (edad<0) {
        alert("nonono")
    } else if (((edad<=1)&&(hemoglobina<13))||((1<edad<=6)&&(hemoglobina<10))||((6<edad<=12)&&(hemoglobina<11))||((12<edad<=60)&&(hemoglobina<11.5))||((60<edad<=120)&&(hemoglobina<12.6))||((120<edad<=180)&&(hemoglobina<13))) {a= true}
    else if (edad>180) {
        let b = prompt("¿sexo masculino(m) o femenino(f)?\n(escribe solo m o f)")
        if (((b=="m")&&(hemoglobina<14))||((b=="f")&&(hemoglobina<12))) {a=true}
    }
    if (a ==true) {alert(`tienes anemia UnU`)}
    else {alert("tas sano pa")}
}   
function ej8() {
    let promedio = parseFloat(document.getElementById("1ej8").value);
    let nivel = document.getElementById("2ej8").value;
    let unidades = 55
    let precio = 180
    if (nivel =="profesional") {
        precio +=120;
        if (promedio>=9.5) {
            precio *= 0.8;}
    } else if (nivel == "preparatoria") {
        if (promedio >=9.5){
            precio *= 0.75;
        }else if (promedio>=9) {
            precio *= 0.8;
            unidades -=5
        }else if (promedio>=9) {
            precio *= 0.9;
            unidades -=5
        }else if (promedio>7) {
            unidades -=5
        }else {
            let per = parseInt(prompt("cuantas materias reprobó?:"))
            unidades -=10
            if (per>3) {unidades-=5}
        }
    }
    let total = (unidades/5)*precio
    alert(`unidades ${unidades}\n precio ${precio}`)
    alert("el total a pagar es "+total)
}
function ej9() {
    let a = parseInt(document.getElementById("9num1").value);
    let b = parseInt(document.getElementById("9num2").value);
    let c = parseInt(document.getElementById("9num3").value);
    let m = 0;
    if ((((a<b)&&(b<c))||((c<b)&&(b<a)))||((a==b)||(c==b))) {
            m = b;
    } else if ((((b<a)&&(a<c))||((c<a)&&(a<b)))||((a==b)||(c==a))) {
                m = a;
    } else if ((((a<c)&&(c<b))||((b<c)&&(c<a)))||((c==b)||(c==a))) 
                m = c;
    else {
    } alert("el d en medio es: " + m);
};

