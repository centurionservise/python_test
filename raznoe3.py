import logging, coloredlogs

# logging.basicConfig(filename='serg_python.log',level=logging.INFO,format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
logging.basicConfig(level=logging.INFO,format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
# logging.basicConfig(level=logging.INFO)
coloredlogs.install()

# for j in "Hi! I'm mister Robert":
# 	if j == "\":
# 	  print ("Найдено")
# 	  break
# else:
# 	print ("Готово")
logging.info('ghjkhgjhgjh')

def foo(b,a=[]):
    a.append(b)
    print(a)
    logging.info("CCCCC")
    
foo(11,['a','b','c'])
foo(22)
foo(33)

# def bbbb (*args){
#     return args
# }

