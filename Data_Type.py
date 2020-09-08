

def dataType(kata):
    if type(kata) is str:
        print('username %s' % kata)
    
    elif type(kata) is int:
        print('age %s' % kata)
    elif type(kata) is bool:
        if kata == False:
            print('Cannot proceed without agreement')
        elif kata == True:
            print('Thank you for agreeing')
    elif kata == "NaN" or kata == 0 or kata == '' or kata == 'null' or kata == 'undefined':
            print('Invalid Data')
    else:
        print('ini bukan string')
dataType(False)