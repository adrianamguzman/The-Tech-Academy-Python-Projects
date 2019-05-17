



import os


def fileName():
    path = '/Users/adriana/pyDrill'
    f =''
    for f in os.listdir(path):
        if f.endswith('.txt'):
            names = (os.path.join(path, f))
            time = (os.path.getmtime(names))
            print (names,time)


fileName()
            
                   
    
    


       
    
        


    
    



            

        


   
   
    
        


    




    
    
     
     
