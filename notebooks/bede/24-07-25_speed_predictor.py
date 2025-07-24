import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import time
import json

### This is a very hard coded file, but a demonstration of a model working from a single call :)
### We will learn about refactoring code and writing better code another week :D

def main():
    model_root = "../../models/"

    # Load your models

    with open(f"{model_root}speed_predictor.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open(f"{model_root}speed_predictor_scaler.pkl", "rb") as model_file:
        sc = pickle.load(model_file)


    # Define you pokemons name and stats

    dummy_pokemon = {
    "name": "Bede's Dummy 2",
    "attack": 34,
    "defense": 54,
    "sp_attack":45,
    "sp_defense": 23
    }

    # Prepare your Data

    input_data = pd.DataFrame(dummy_pokemon, columns = dummy_pokemon.keys(), index = range(1))
    
    # Drop the columns the model does not use as inputs ie. name, keep the stats ones :)
    input_data = input_data.drop(columns="name")

    # Scale the data using the same scaling model we built previously
    input_data_sc = sc.transform(input_data)
    # Convert the scaled array back to a dataframe
    input_data =  pd.DataFrame(input_data_sc, columns=input_data.columns)

    # Predict the speed output from the input data
    speed_stat = model.predict(input_data).item()

    # Print the results
    print(f"""Pokemon Name: {dummy_pokemon["name"]}

Stats:
          Attack : {dummy_pokemon["attack"]}
         Defense : {dummy_pokemon["defense"]}
      Sp. Attack : {dummy_pokemon["sp_attack"]}
     Sp. Defense : {dummy_pokemon["sp_defense"]}

Loading Speed Prediction...
""")
    # Simuluting a loading time :) doesnt actually do anything else
    time.sleep(1.5)

    print(f"Speed Stat Prediction : {int(speed_stat)}")

    # Add the speed stat to the old dictionary
    dummy_pokemon["speed"] = int(speed_stat)
    with open(f"../../data/new_pokemon_database/{dummy_pokemon['name']}.json", "w") as file:
        json.dump(dummy_pokemon, file, indent=4)
if __name__ == "__main__":
    main()