import pandas as pd
import numpy as np
import pickle
import time
import json
import os

from sklearn.linear_model import LinearRegression

def main():
    model_root = "C:/Users/tiggy/Documents/VSCode/Data Science/Projects/pokemon-project/models/"
    output_folder = "../../data/new_pokemon_database/"
    os.makedirs(output_folder, exist_ok=True)

    with open(f"{model_root}speed_predictor.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open(f"{model_root}speed_predictor_scaler.pkl", "rb") as model_file:
        sc = pickle.load(model_file)

    dummy_pokemon = {
    "name": "Sharkigo",
    "attack":90,
    "defense": 40,
    "sp_attack": 150,
    "sp_defense": 90
}
    input_data = pd.DataFrame(dummy_pokemon, columns = dummy_pokemon.keys(), index = range(1))
    input_data = input_data.drop(columns="name")
    input_data_sc = sc.transform(input_data)
    input_data = pd.DataFrame(input_data_sc, columns=input_data.columns)
    speed_stat = model.predict(input_data).item()

    print(f"""Pokemon Name: {dummy_pokemon["name"]}

Stats:
          Attack : {dummy_pokemon["attack"]}
         Defense : {dummy_pokemon["defense"]}
      Sp. Attack : {dummy_pokemon["sp_attack"]}
     Sp. Defense : {dummy_pokemon["sp_defense"]}

Loading Speed Prediction...
""")
    time.sleep(1.5)
    print(f"Speed Stat Prediction : {int(speed_stat)}")

    dummy_pokemon["speed"] = int(speed_stat)
    with open(f"../../data/new_pokemon_database/{dummy_pokemon['name']}.json", "w") as file:
        json.dump(dummy_pokemon, file, indent=4)

if __name__ == "__main__":
    main()



