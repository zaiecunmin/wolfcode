import os
def install():
    try:
        will_pip=['pygame','pandas','requests','selenium','opencv_python','myqr','PyEmail','vika','flask']
        for p in will_pip:
            os.system('pip install '+p)
    except:
        print('Download failed\nPlease download manually')
        return False
    else:
        print('Download successful')
        return True


if __name__ == '__main__':
    install()