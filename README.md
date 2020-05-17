# Game of Life
The Game of Life, also known simply as Life, is a cellular automaton
devised by the British mathematician John Horton Conway in 1970.

# Source
[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life "Wikipedia")

# How to run?
1. Clone or download this repository  
2. Create virtual environment in repository: ```python3 -m venv venv```  
3. Activate virtual environment: ```source venv/bin/activate```  
4. Install requirements: ```python3 -m pip install -r requirements.txt```  
5. Run from the terminal as: ```./game.py```  

# Table structure

|          | -n     | -n+1   | ...    | 0      | ...    | n-1    | n     |
|----------|:------:|:------:|:------:|:------:|:------:|:------:|------:|
| **n**    |        |        |        |        |        |        |       |
| **n-1**  |        |        |        |        |        |        | *     |
| **...**  |        |        |        |        |        |        |       |
| **0**    |        |        |        |        |        |        |       |
| **...**  |        |        |        |        |        |        |       |
| **-n+1** |        |        |        |        |        |        |       |
| **-n**   |        |        |        |        |        |        |       |

You should fill new ```.csv``` table in ```data``` folder  
For example __*__ has position ```n, n-1```

# Sample of execution 
### As an output, you will have a terminal image which will change every tick  
![alt-text](https://github.com/AleksandrTolstoy/Game-of-Life/blob/master/samples/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202020-04-16%20%D0%B2%2017.00.55.png)
![alt-text](https://github.com/AleksandrTolstoy/Game-of-Life/blob/master/samples/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202020-04-16%20%D0%B2%2017.00.51.png)
