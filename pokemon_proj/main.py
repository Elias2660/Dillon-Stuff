import pandas as pd



#creates a separate html file for each type of pokemon and lists out those pages
# create_subs() -> returns string
#author: Elias
def create_subs():
  end = ""
  for type, index in zip(['Grass', 'Fire', 'Water', 'Bug', 'Normal', 'Poison', 'Electric',
       'Ground', 'Fairy', 'Fighting', 'Psychic', 'Rock', 'Ghost', 'Ice',
       'Dragon'], range(17)):
    end += f'            <li> <a href="{type}.html"> {type} </a> </li> \n'
  return end

#creates the navbar by including links to the html files for the homepage and topten pokemon pages
# nav_creator() -> returns string
#author Elias
def nav_creator():
  result = f"""
    <nav>
    <ul>
      <li><a href="homepage.html">Homepage</a></li>
      <li><a href="#all_types">Types</a>
         <ul>
{create_subs()}
         </ul>
      </li>
      <li><a href="TopTen.html">Top Ten</a></li>
      <li><a href="all.html">All</a></li>
    </ul>
  </nav>
  """
  return result

#standardizes css to include the same font-family, font-size, and more across all pages
# add_css -> returns string
#author: Adeline
def add_css():
  return """
  html {
  height: 100%;
  width: 100%;
  font-size: 25px;
  font-family: 'Cinzel', serif;
}


table {
  border-collapse: collapse;
}

table, th, td {
  border: 1px solid black;
  padding: 8px;
}

th {
  font-family: 'Playfair Display', serif;
}

body {
  background-color: #8BD9E3;
}

h1 {
  font-size: 15px;
}
img {
  width: 100px;
  height: 100px;
}
      ul {
        list-style: none;
        padding-left: 0;
      }
      .nav-link {
        display: inline-block;
        padding: 10px;
        background-color: #337ab7;
        color: #fff;
        text-decoration: none;
        border-radius: 5px;
        margin-right: 10px;
      }
      .nav-link:hover {
        background-color: #23527c;
      }
  nav li {
   display: inline-block;
   position: relative;
}
nav li ul {
   display: none;
   position: absolute;
   width: 100px;
   top: 100%;
   padding: 0;
}
nav li:hover > ul {
   display: block;
}
nav a {
}

 .card {
      margin: auto;
      width: 18rem;
    }"""

#this function writes the homepage file for the homepage
#create_homepage() -> write file and print string
#Author Adeline
def create_homepage():
#homepage by Adeline:

  script = """
    <!---Required Javascript to make image carousel work--->
    <script>
  $(document).ready(function() {
    // Activate Carousel
    $("#carouselExampleCaptions").carousel();

    // Enable Carousel Indicators 
    $(".carousel-indicators li").click(function() {
      $("#carouselExampleCaptions").carousel(parseInt($(this).attr("data-bs-slide-to")));
    });

    // Enable Carousel Controls
    $(".carousel-control-prev").click(function() {
      $("#carouselExampleCaptions").carousel("prev");
    });
    $(".carousel-control-next").click(function() {
      $("#carouselExampleCaptions").carousel("next");
    });
  });
  </script>
"""
  css= """     
  
  body {
  font-size: 25px;
  font-family: 'Cinzel', serif;        
  background-color: #8BD9E3;
      }
      h1 {
        color: #337ab7;
        text-align: center;
      }
      #intro {
        text-align: center;
        font-size: 20px;
        margin-bottom: 20px;
      }
      ul {
        list-style: none;
        padding-left: 0;
      }
      .nav-link {
        display: inline-block;
        padding: 10px;
        background-color: #337ab7;
        color: #fff;
        text-decoration: none;
        border-radius: 5px;
        margin-right: 10px;
      }
      .nav-link:hover {
        background-color: #23527c;
      }
  nav li {
   display: inline-block;
   position: relative;
}
nav li ul {
   display: none;
   position: absolute;
   width: 100px;
   top: 100%;
   padding: 0;
}
nav li:hover > ul {
   display: block;
}
nav a {
}

 .card {
      margin: auto;
      width: 18rem;
    }"""
  file = f"""
  <!DOCTYPE html>
<html>

<head>

  <!-- Required JavaScript -->

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.9.3/umd/popper.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.1.0/js/bootstrap.min.js"></script>

{nav_creator()}
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Homepage</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
</head>
  <style>
{css}
  </style>
  </head>
  <body>

    
    <h1>Welcome to our project!</h1>
    <div id="intro">
      <p>Thanks for stopping by!</p>
    </div>
    
<div class="home image">
  <img src="https://www.gamespot.com/a/uploads/screen_kubrick/1601/16018044/4056259-gen-one-pokemon.jpg" class="card-img-top" alt="a group picture of Pokemon's original characters">
  <div class="card-body">
    <h3 class="card-title">Quick introduction...</h3>
    <p class="card-text">This is our Gyarados-themed webpage! Gyarados definitely stood out to us by evolving from what seems to be a harmless Magikarp into one of the most powerful, angry Pokemon. We've also created the ultimate place to compare our favorite pokemon, and, on this page, you can view a lot of really awesome and thorough wikis on the Pokemon!</p>
    <p class="card-text"><small class="text-body-secondary">Which is your favorite Pokemon?</small></p>
    <img src="https://i.pinimg.com/originals/77/3b/4f/773b4f0cd82382757eeca8493911e888.png" class="img-grid" alt="a grid showing many of the first gen pokemon">
  </div>

<div id="carouselExampleCaptions" class="carousel slide">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="https://th.bing.com/th/id/OIP.FQulcpolFElw406VR3w7mQHaEK?pid=ImgDet&rs=1" class="d-block w-100" alt="gyarados with its mouth closed, looking grim">
      <div class="carousel-caption d-none d-md-block">
        <h5>Beware the splash zone!</h5>
  
      </div>
    </div>
    <div class="carousel-item">
      <img src="https://m.media-amazon.com/images/I/71gNAgjLnKL._AC_UF894,1000_QL80_.jpg" class="d-block w-100" class="d-block w-100" alt="an example of a Gyarados pokemon card with attacks like berserker splash">
      <div class="carousel-caption d-none d-md-block">
        <h5>Generation V Gyarados card</h5>
        <p>Gyarados' approach is through anger!</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="https://preview.redd.it/va9fgh93kac31.png?auto=webp&s=ea17717ffebe195a45fa33e5bd0772e3b60acd0b" class="d-block w-100" alt="a scene from the most recent pokemon movie involving Gyarados">
      <div class="carousel-caption d-none d-md-block">
        <h5>Gyarados meets Pikachu</h5>
        <p>from the Pokémon Detective Pikachu movie</p>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
  
    <div class="card" style="width: 18rem;">
      <img src="https://th.bing.com/th/id/R.0a050151aa3c0f13d54285b1d8fe80e6?rik=8giEXJ%2b44nK%2fFw&pid=ImgRaw&r=0" class="img-magikarp" alt="shiny magikarp" width = "285" height = "250">

  <div class="card-body">
    <h5 class="card-title">Magikarp</h5>
    <p class="card-text"> Magikarp is known colloquially as the "Fish Pokemon". Magikarp is also the identity of my friend on Duolingo, who is on a 300 day streak. The concept of Magikarp evolving into Gyarados is based on the ancient Chinese myth about carp that can evolve into flying dragons after leaping into a waterfall.</p>
    <a href="https://pokemondb.net/pokedex/magikarp" class="btn btn-primary">Go to Pokedex!</a>
      <img src="https://img.pokemondb.net/sprites/home/normal/2x/avif/magikarp.avif" class="img-magikarp" alt="clay magikarp">
    <a href= "https://www.serebii.net/pokedex-swsh/magikarp/" button type="button" class="btn btn-success">Go to a beautiful Wiki</button>
  </div>
      
      <div class="card" style="width: 18rem;">
  <img src="https://static.pokemonpets.com/images/monsters-images-300-300/2130-Shiny-Gyarados.webp" class="img-gyarados" alt="gyarados looking fierce">
  <div class="card-body">
    <h5 class="card-title">Gyarados</h5>
    <p class="card-text">Called "Léviator" in French,  </p>
    <img src="https://archives.bulbagarden.net/media/upload/e/e3/Spr_5b_130_m.png" class="rounded float-end" alt="a gif of gyarados roaring and shimmying">
    <p class="in-depth-description">Gyarados is both a water and dark-type Pokemon. In the Pokémon Red and Blue beta, Gyarados' name was "Skulkraken", a combination of skull and kraken (a mythological sea monster).</p>
     <a href="https://en.wikipedia.org/wiki/Gyarados" class="btn btn-primary">Visit Gyarados' actual Wikipedia page</a>
     <p> While Magikarp is just a Water-type Pokemon, when it evolves into Gyarados, it becomes both a Water and Flying-type Pokemon.</p>
  </div>
        <div class="Mega Gyarados Card" style="width: 18rem;">
  
  <img src="https://sg.portal-pokemon.com/play/resources/pokedex/img/pm/d1b4b9ec796de5d101e85258987036767c37a34b.png" class="img-megagyarados" alt="mega gyarados looking fierce">
  </div>
  <div class="card-body">
    <h5 class="card-title">Mega Gyarados</h5>
    <p class="card-text">Mega Gyarados is tied with Hoopa Unbound as the tallest Dark-Type Pokemon! It also appears in Pokemon Battle Chess, and appears only when Magikarp is destroyed. </p>
    <p class="card-text">Check out what some of the inspiration for Gyarados might have looked like! </p>
    <img src= "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Chinese_dragon_asset_heraldry.svg/220px-Chinese_dragon_asset_heraldry.svg.png" class= "img-qing-dynasty-flag" alt="the qing dynasty flag, yellow with a blue dragon icon in the center">
    <p class="motif-in-chinese-culture">Here is the dragon featured on the flag of the Qing dynasty, where dragons represented a range of things, from feudal imperial power to a Buddhist interpretation of the dragon: 'as water destroys, they said, so can some dragons destroy via floods, tidal waves, and storms. They suggested that some of the worst floods were believed to have been the result of a mortal upsetting a dragon.'</p>
    <a href="https://bulbapedia.bulbagarden.net/wiki/Gyarados_%28Pok%C3%A9mon%29" class="btn btn-primary">Go to Bulbapedia and read trivia</a>
    <img src="https://veekun.com/static/pokedex/images/trainer-male.png" alt="tiny hooman named ash ketchum" width= "40" height= "50">
    <a href="#" class="jump-to-top-button">Go back to top</a>
    
{script}
  
</div>



  </body>
</html>
  """
  with open("homepage.html", "w") as website:
    website.write(file)

  print("completed homepage")
  #homepage by Adeline


#This function writes the top_ten file and a css file. Using a python code to fill in the colomns of the html table along with creating the skeleton for the table as well.
#top_ten() -> write two files
#Author: Khadijah 
def top_ten():
  style = f"""
  {add_css()}
  """
  file = f"""
  <!DOCTYPE html> 
<html>
{nav_creator()}
  <head>
    <p>Top Ten Pokemon!</p>
    <link rel="stylesheet" type="text/css" href="TopTen.css">
  </head>
  <body> 
    <table>
        <tr>
          <th>Pokemon</th>
          <th>Type 1</th>
          <th>Type 2</th>
          <th>Total</th>
          <th> HP</th>
          <th>Attack</th>
          <th>Defense</th>
          <th>Sp.Defense</th>
          <th>Sp.Atk</th>
          <th>Speed</th>
          <th>Generation</th>
          <th>Lengendary</th>
        </tr>
          
            <tr>
			 <td>Gyarados</td>
			 <td>Water</td>
			 <td>Flying</td>
			 <td>540</td>
			 <td>95</td>
			 <td>125</td>
			 <td>79</td>
			 <td>60</td>
			 <td>100</td>
			 <td>81</td>
			 <td>1</td>
			 <td>False</td>
</tr>
<tr>
			 <td>Rapidash</td>
			 <td>Fire</td>
			 <td>Fire</td>
			 <td>500</td>
			 <td>65</td>
			 <td>100</td>
			 <td>70</td>
			 <td>80</td>
			 <td>80</td>
			 <td>105</td>
			 <td>1</td>
			 <td>False</td>
</tr>
<tr>
			 <td>Squirtle</td>
			 <td>Water</td>
			 <td>Water</td>
			 <td>314</td>
			 <td>44</td>
			 <td>48</td>
			 <td>65</td>
			 <td>50</td>
			 <td>64</td>
			 <td>43</td>
       <td> 1</td>
			 <td>False</td>
</tr>
<tr>
			 <td>Meowth</td>
			 <td>Normal type</td>
			 <td>Normal type</td>
			 <td>290</td>
			 <td>40</td>
			 <td>45</td>
			 <td>35</td>
			 <td>40</td>
			 <td>40</td>
			 <td>90</td>
			 <td>1</td>
			 <td>False</td>
</tr>
<tr>
			 <td>Ditto</td>
			 <td>Normal</td>
			 <td>Normal</td>
			 <td>288</td>
			 <td>48</td>
			 <td>48</td>
			 <td>48</td>
			 <td>48</td>
			 <td>48</td>
			 <td>48</td>
			 <td>1</td>
			 <td>False</td>
</tr>
<tr>
			 <td>Dragonair</td>
			 <td>Dragon</td>
			 <td>Dragon</td>
			 <td>420</td>
			 <td>61</td>
			 <td>84</td>
			 <td>65</td>
			 <td>70</td>
			 <td>70</td>
			 <td>70</td>
			 <td>1</td>
			 <td>False</td>
</tr>
<tr>
			 <td>Raichu</td>
			 <td>Electric</td>
			 <td>Electric</td>
			 <td>485</td>
			 <td>60</td>
			 <td>90</td>
			 <td>55</td>
			 <td>90</td>
			 <td>80</td>
			 <td>110</td>
			 <td>1</td>
			 <td>False</td>
</tr>
<tr>
			 <td>Venusaur</td>
			 <td>Grass</td>
			 <td>Poison</td>
			 <td>525</td>
			 <td>80</td>
			 <td>82</td>
			 <td>83</td>
			 <td>100</td>
			 <td>100</td>
			 <td>80</td>
			 <td>1</td>
			 <td>False</td>
</tr>
<tr>
			 <td>Mew</td>
			 <td>Psychic</td>
			 <td>Psychic</td>
			 <td>600</td>
			 <td>100</td>
			 <td>100</td>
			 <td>100</td>
			 <td>100</td>
			 <td>100</td>
			 <td>100</td>
			 <td>1</td>
			 <td>False</td>
</tr>
<tr> 
			 <td>Charmeleon</td>
			 <td>Fire</td>
			 <td>Fire</td>
			 <td>405</td>
			 <td>58</td>
			 <td>64</td>
			 <td>58</td>
			 <td>80</td>
			 <td>65</td>
			 <td>80</td>
       <td> 1</td>
			 <td>False</td>
</tr>
<h1>Take a look at all the Pokemon on our Top Ten Pokemon list through the images below (all in order from left to right)!</h1>

   
			<img src="https://i.pinimg.com/474x/0a/76/16/0a7616c95ef4859d857f1515f3034fd2.jpg" alt="Gyarados">
			<img src="https://oyster.ignimgs.com/mediawiki/apis.ign.com/pokemon-x-y-version/6/6e/Rapidash.jpg" alt="Rapidash">
			<img src="https://i.pinimg.com/550x/1b/47/3a/1b473a97ded04ac7c5b85eaf2baa5441.jpg" alt="Squirtle">
			<img src="https://cosplayfu-website.s3.amazonaws.com/_Upload/b/40cm-Meowth-Pokemon-Plush-Toy.jpg" alt="Meowth">
			<img src="https://img.pokemondb.net/artwork/large/ditto.jpg" alt="Ditto">
      <img src="https://assets.pokemon.com/assets/cms2/img/pokedex/full/148.png" alt="Dragonair">
      <img src="https://i.pinimg.com/736x/b7/5a/41/b75a41b1f2136e999c46efbb216abb72--draw-pokemon-pokemon-team.jpg" alt="Raichu">
      <img src="https://oyster.ignimgs.com/mediawiki/apis.ign.com/pokemon-x-y-version/1/13/Mega_venusaur.jpg?width=325" alt="Venusaur">
      <img src="https://e7.pngegg.com/pngimages/404/471/png-clipart-pokemon-let-s-go-pikachu-and-let-s-go-eevee-pokemon-go-pokemon-red-and-blue-mew-pokemon-go.png" alt="Mew">
      <img src="https://static.pokemonpets.com/images/monsters-images-300-300/5-Charmeleon.webp" alt="Charmeleon">
		
          
  </body>
</html>
  """
  with open("TopTen.html", "w") as website:
    website.write(file)
  with  open("TopTen.css", "w") as website:
    website.write(style)

#preprocesses css file and return pandas dataframe with converted from csv
# data_preprocessing() -> pandas dataframe
#Author: Elias
def data_preprocessing():
  data = pd.read_csv("pokemon.csv")
  data.drop(["#"],axis = 1, inplace = True )
  data.rename(columns = {"Type 1": "Type1", "Type 2": "Type2"}, inplace = True)
  return data


#creates info table for each type page
# create_lines(pokeType, data) -> string 
# pokeType: type of pokemon as string
# data: pokemon data as a pandas dataframe from data_preprocessing
#returns a string the constitues the table data
#Author: Elias
def create_lines(pokeType, data):
  that_type = (data.Type1 == pokeType) | (data.Type2 == pokeType)
  
  pokemen = data.loc[that_type]
  template = '<table class = "styled-table">\n'
  template += '    <tr class="active-row">\n'
  for feature in data:
    template+= f"      <td> {feature} </td>\n"
  template += '    </tr>\n'
  for index in pokemen.index:
    template += '      <tr class="active-row">\n'
    for feature in data:
      template += f"        <td>{data.iloc[index][feature]}</td>\n"
    template += "      </tr>\n"
  template += "    </table>"
  return template


#file with name outputFileName for each type and adds some text  for pokeType
#makePage(pokeType,outputFileName, data) -> written file
#pokeType: type of pokemon type being created
#outputFileName: what file is written as
#data: pokemon data as a pandas dataframe from data_preprocessing
#author: Adeline, Khadijah, Elias
def makePage(pokeType,outputFileName, data):
        template = f"""
        <!DOCTYPE html>
          <html lang="en">
          <head>
             <meta charset="UTF-8">
             <meta http-equiv="X-UA-Compatible" content="IE=edge">
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <title>Data for {pokeType} Pokemon</title>
             <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
{nav_creator()}
          </head>
          <body> 
          <h1 class = "title"> Table Data for {pokeType} Pokemon! </h1>
{create_lines(pokeType, data)}
          </body>
          <style>
{add_css()}
          </style>
          </html> """
        with open(outputFileName, "w") as text:
          text.write(template)

#creates all the lists for the table in the all page
#create_all_lines(data) -> string
#data -> string
#data: pokemon data as a pandas dataframe from data_preprocessing
# string: multi line string with all 
#author: Elias
def create_all_lines(data):
  template = '<table class = "styled-table">\n'
  template += '    <tr class="active-row">\n'
  for feature in data:
    template+= f"      <td> {feature} </td>\n"
  template += '    </tr>\n'
  for index in data.index:
    template += '      <tr class="active-row">\n'
    for feature in data:
      template += f"        <td>{data.iloc[index][feature]}</td>\n"
    template += "      </tr>\n"
  template += "    </table>"
  return template


#write file and adds css for the all page
#make_all_lines(data)
#data: pokemon data as a pandas dataframe from data_preprocessing
#author: Elias
def make_all(data):
  types = ['Grass', 'Fire', 'Water', 'Bug', 'Normal', 'Poison', 'Electric',
         'Ground', 'Fairy', 'Fighting', 'Psychic', 'Rock', 'Ghost', 'Ice',
         'Dragon']
  total_table = create_all_lines(data)
  html = f"""
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    {nav_creator()}
</head>
<body>
    {total_table}
</body>
<style>
{add_css()}
</style>
</html>
  """
  with open("all.html","w") as all:
    all.write(html)
    
    

#puts everything together into one function that creates the homepage, creates the top ten page
# make_pages() -> files, implementation
#and then applies the processing function to the data for each pokemon type
#implemation file for each of the earlier functions
#Author: Adeline, Khadijah, Elias
def make_pages():
  create_homepage()
  top_ten()
  types =  ['Grass', 'Fire', 'Water', 'Bug', 'Normal', 'Poison', 'Electric',
         'Ground', 'Fairy', 'Fighting', 'Psychic', 'Rock', 'Ghost', 'Ice',
         'Dragon']
  data = data_preprocessing()

  for type in types:
    print(f"making {type}")
    makePage(type, f"{type}.html", data)

  make_all(data)

  
"""
One function to rule them all,
one function to find them,
One funtion to bring them all,
and in the bottom of the file bind them;
In the Land of Replit where the shadows lie.
"""
make_pages()