######
'''WIP'''
#####


def moGate():
    p=nuke.Panel('Authentication Required')
    p.addPasswordInput('Password','abcdefg')
    p.show()
    val=p.value('Password')
    if val=='mohan-p@perp':
        print 'success'
    else:
        nuke.message('Please type the correct password or ask password to me(mohan-p)')
    return
