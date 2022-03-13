entrada = input ('Introduce en nombre de un navegador:\n ')

navegadores = ['chrome','firefox','opera','safari']


# in = dentro de y de ser cierto, enseña un True

if entrada in navegadores:
    print('El navegador que buscas está en la lista.')
    
else:
    print('El navegador que buscas no está en la lista.')