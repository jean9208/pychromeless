from autocompara_lambda import cotizar

def lambda_handler(*args, **kwargs):

    #tipo    = args[0]
    #year    = args[1]
    #version = args[2]
    #cp      = args[3]

    tipo = 'AUTO'
    year = '2021'
    version = 'YARIS S HB CVT 1.5L 4CIL'
    cp = '55717'
    
    output = cotizar(tipo, year, version, cp)
    
    return(output)
