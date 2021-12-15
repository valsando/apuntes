function califica() {
    var m1 = parseFloat(document.getElementById("1m10").value);
    var m2 = parseFloat(document.getElementById("2m10").value);
    var m3 = parseFloat(document.getElementById("3m10").value);
    var me = parseFloat(document.getElementById("em10").value);
    var f1 = parseFloat(document.getElementById("1f10").value);
    var f1 = parseFloat(document.getElementById("2f10").value);
    var fe = parseFloat(document.getElementById("ef10").value);
    var q1 = parseFloat(document.getElementById("1q10").value);
    var qe = parseFloat(document.getElementById("eq10").value);
    var mat = 0.1 *((m1 + m2 + m3)/3) + (me * 0.9);
    var fis = 0.2 *((f1+f2)/2) + (fe * 0.8);
    var qui = (0.15*q1) + (0.85 * qe);
    var prome = ((mat)+ (fis)+ (qui))/3;
    alert("aja")
}