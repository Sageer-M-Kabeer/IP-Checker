import socket

print('''
  ___ ___    ___ _  _ ___ ___ _  _____ ___ 
 |_ _| _ \  / __| || | __/ __| |/ / __| _ \
  | ||  _/ | (__| __ | _| (__| ' <| _||   /
 |___|_|    \___|_||_|___\___|_|\_\___|_|_\
                                           
''')
print('By SageerMK aka Hendri3x22')

hostnamez= socket.gethostname()
ipad=socket.gethostbyname(hostnamez)

print("IP found on this machine is : " , ipad)
