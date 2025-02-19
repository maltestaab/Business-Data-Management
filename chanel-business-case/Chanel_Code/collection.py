# Create a new column to indicate if "Love" is in the product name
df["Love_collection"] = df["collection"].str.contains(r"\bLove\b", case=False, na=False)
# Replace True with "Love" and False with an empty string
df["Love_collection"] = df["Love_collection"].replace({True: "Love", False: ""})

# Create a new column to indicate if "Love" is in the product name
df["Trinity_collection"] = df["collection"].str.contains(r"\bTrinity\b", case=False, na=False)
# Replace True with "Love" and False with an empty string
df["Trinity_collection"] = df["Trinity_collection"].replace({True: "Trinity", False: ""})

# Create a new column to indicate if "Love" is in the product name
df["Amulette_collection"] = df["collection"].str.contains(r"\bAmulette\b", case=False, na=False)
# Replace True with "Love" and False with an empty string
df["Amulette_collection"] = df["Amulette_collection"].replace({True: "Amulette de Cartier", False: ""})

# Create a new column to indicate if "Love" is in the product name
df["Juste_collection"] = df["collection"].str.contains(r"\bJuste un Clou\b", case=False, na=False)
# Replace True with "Love" and False with an empty string
df["Juste_collection"] = df["Juste_collection"].replace({True: "Juste un Clou", False: ""})

# Create a new column to indicate if "Love" is in the product name
df["Panthere_collection"] = df["collection"].str.contains(r"\bPanthère de Cartier\b", case=False, na=False)
# Replace True with "Love" and False with an empty string
df["Panthere_collection"] = df["Panthere_collection"].replace({True: "Panthère de Cartier", False: ""})

# Create a new column to indicate if "Love" is in the product name
df["Clash_collection"] = df["collection"].str.contains(r"\bClash de Cartier\b", case=False, na=False)
# Replace True with "Love" and False with an empty string
df["Clash_collection"] = df["Clash_collection"].replace({True: "Clash de Cartier", False: ""})

# Combine all collection columns into a single "Collection" column
df["Collection"] = df[
    ["Love_collection", "Trinity_collection", "Amulette_collection", 
     "Juste_collection", "Panthere_collection", "Clash_collection"]
].agg(lambda x: " ".join(x).strip(), axis=1)