def esSubsecuencia(s: list[int], r: list[int]) -> bool:
    result: bool = False
    ultimoIndice: int = len(s) - len(r)
    
    for i in range(ultimoIndice + 1):
        subseq: list[int] = subsecuencia(s, i, len(r))
        sonIguales: bool = iguales(subseq, r)
        
        if sonIguales:
            result = True
            break
    
    return result

def subsecuencia(s: list[int], desde: int, longitud: int) -> list[int]:
    rv: list[int] = []
    hasta: int = desde + longitud
    
    for j in range(desde, hasta):
        elem: int  = s[j]
        rv.append(elem)
        
    return rv

def iguales(s: list[int], r: list[int]) -> bool:
    result: bool = True
    
    if len(s) != len(r):
        result = False
    else:
        for i in range(len(s)):
            if s[i] != r[i]:
                result = False
                break
    
    return result