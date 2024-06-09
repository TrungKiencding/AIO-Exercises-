def md_nre (y=90, y_hat=89, n=2, p=1):
    result = (y ** (1/n) - y_hat ** (1/n)) ** p
    
    return result

print(md_nre())
