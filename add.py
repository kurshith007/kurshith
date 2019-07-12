def findSum(N, K): 
  
    an = 0; 


    y = N / K; 
  

    x = N % K; 
 
    an = ((K * (K - 1) / 2) * y + 
                (x * (x + 1)) / 2); 
  
    return int(an);
