import os
from pygoogle_image import image as pi

celebrities = [
    'Michael Jordan',
    'Cristiano Ronaldo',
    'Lionel Messi',
    'LeBron James',
    'Serena Williams',
    'Tom Brady',
    'Usain Bolt',
    'Muhammad Ali',
    'Tiger Woods',
    'Roger Federer',
    'Diego Maradona',
    'Kobe Bryant',
    'Neymar Jr.',
    'Rafael Nadal',
    'Floyd Mayweather Jr.',
    'Michael Phelps',
    'Wayne Gretzky',
    'Novak Djokovic',
    'David Beckham',
    'Michael Schumacher',
    'Mike Tyson',
    'Steph Curry',
    'Pele',
    'Lewis Hamilton',
    'Kevin Durant',
    'Ronda Rousey',
    'Manny Pacquiao',
    'Virat Kohli',
    'Ronaldinho',
    'Cristiano Ronaldo',
    'Sachin Tendulkar',
    'Roger Federer',
    'David Beckham',
    'Ronaldo',
    'Kobe Bryant',
    'Usain Bolt',
    'LeBron James',
    'Lewis Hamilton',
    'Michael Phelps',
    'Novak Djokovic',
    'Tiger Woods',
    'Tom Brady',
    'Serena Williams',
    'Lionel Messi',
    'Neymar Jr.',
    'Kobe Bryant',
    'Lewis Hamilton',
    'Michael Jordan',
    'David Beckham',
    'Virat Kohli',
    'Kevin Durant',
    'Roger Federer',
    'Usain Bolt',
    'Lionel Messi',
    'LeBron James',
    'Michael Phelps',
    'Muhammad Ali',
    'Michael Schumacher',
    'Wayne Gretzky',
    'Novak Djokovic',
    'Rafael Nadal',
    'Serena Williams',
    'Mike Tyson',
    'David Beckham',
    'Cristiano Ronaldo',
    'Lionel Messi',
    'Tom Brady',
    'LeBron James',
    'Usain Bolt',
    'Michael Jordan',
    'Wayne Gretzky'
]

def download_images(celebrity):
    celebrity_directory = os.path.join(celebrity)
    pi.download(celebrity, limit=1000)
    for filename in os.listdir('.'):
        if filename.endswith('.jpg'):
            os.rename(filename, os.path.join(celebrity_directory, filename))
    print(f"Downloaded images for {celebrity}")
    
for celebrity in celebrities:
    download_images(celebrity)