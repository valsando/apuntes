"use strict";

const ej1 = (n) => {
    let prom = 0;
    let lista = [];
    for (let i = 1; i <= n; i++) {
        let a = parseFloat(prompt("calificacion " + (i)))
        lista.push(a)
        prom +=a
    }
    prom /= lista.length
    alert("el promedio de calificaciones es de: " + prom)
}
const ej2 = (n) => {
    let lista = []
    let cuadrado = []
    let cubo =[]
    for (let i = 1; i<=n; i++) {
        let a = parseFloat(prompt("numero #" + i))
        lista.push(a)
        cuadrado.push(a**2)
        cubo.push(a**3)
    }
    let list = []
    for (let i = 0; i < n; i++) {
        let ala = String(lista[i]) + "   " + String(cuadrado[i]) + "   "+ String(cubo[i]) + "\n"
        list.push(ala)
    }
    alert(list)
}
const ej3 = (n) => {
    let lista = []
    for (let i = 0; i<n; i++) {
        let a = parseFloat(prompt("numero: #" + i))
        if (a>0) {
            lista.push(a)
        }
    } alert(lista)
}
const ej4 = (n) => {
    let pos = 0
    let neg = 0
    let cero = 0
    for (let i = 0; i<n; i++) {
        let a = parseFloat(prompt("numero: #" )) 
        if (a>0) {pos++}
        else if (a<0) {neg++}
        else {cero++}
    }
    alert(`hay ${pos} positivos; ${neg} negativos y ${cero} neutros`)
}
const ej5 = (n) => {
    let neg = 0
    let lista = []
    while (neg<n) {
        let a = parseFloat(prompt("numero: #" )) 
        if (a<0) {neg++;a*=-1; lista.push(a)}
    }
    alert("los numeros negativos (que son ahora positivos) son los siguientes: " + lista)
}
const ej6 = (n) => {
    let prom = 0
    let bajo = 11
    for (let i = 0; i<n; i++) {
        let a = parseFloat(prompt("numero: #" )) 
        prom += a
        if (a<bajo) {bajo = a}
    }
    prom /= n
    alert(`el promedio del grupo es de ${prom} y la nota mas baja es de ${bajo}`)
}
const ej7 = () => {
    let a = parseFloat(prompt("numero a multiplicar:" )) 
    let l = ""
    for (let i = 1; i<=10; i++) {
        let b = a * i
        let r = `${a} *${i} =${b}\n`
        l+=r
    } alert(l)
}
const ej8 = () => {
    var hoy = new Date()
    let hora = hoy.getHours() + ":" + hoy.getMinutes() + ":" + hoy.getSeconds()
    alert("la hora es: " + hora)
}