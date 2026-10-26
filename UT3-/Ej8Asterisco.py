#parametros obligatoriamente nombrados (keyword-only arguments)
#el * significa que los parametros a partir de ahi deben pasarse con ese nombre

def suma(n1,n2,*,op="+"):
    if op=="+":
        return n1+n2
    elif op=="-":
        return n1-n2
    else:
        return "error"

print(suma(2,3, op="-"))