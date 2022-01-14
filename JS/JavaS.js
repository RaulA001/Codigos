function soma(ns, toria) {
    var res = 0
    if (toria) {
        for (var n = ns[0]; !(n == 0); n--) {
            console.log(n)
            res += n
        }
        return res

    }

    for (let v in ns) {
        res += ns[v]
    }
    return res
    
}

function subtracao (np, nn) {
    var res = 0
    np = soma(np)
    nn = soma(nn)
    res = np - nn
    return res
}

function mutiplicacao (ns) {
    var res = 1
    
    for (let n in ns) {
        res *= ns[0]
    }
    return res
}

function divisao(N, n) {
    N = soma(N)
    n = soma(n)
    res = N / n
    return res
}

function potencia(n, p=2) {
    res = n**p
    return res
}

function raiz(n, p=2) {
    Math.sqrt
    res = n**(1/p)
    return res
}
