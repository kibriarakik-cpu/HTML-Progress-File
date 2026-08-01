pasta("Pasta Aribahtis", "Italian" ,"20"  ) # type: ignore
Biryani("chicken" , "basmati rice" , "saffron" , "Indian","56" ) # type: ignore
print("Recipe1:", pasta) # type: ignore
print("Recipe2:", Biryani) # type: ignore
print("Name",pasta[0]) # type: ignore
print("Cuisine",pasta[1]) # type: ignore
print("Cooking Time",pasta[2]) # type: ignore
print("Name",Biryani[0]) # type: ignore
print("Main Ingredient",Biryani[1]) # type: ignore
print("Spice Level",Biryani[2]) # type: ignore
print("Cuisine",Biryani[3]) # type: ignore
print("Cooking Time",Biryani[4]) # type: ignore
all_recipes = [pasta, Biryani] # type: ignore
print("All Recipes:", all_recipes) # type: ignore
print("\nFirst Recipe:", all_recipes[0]) # type: ignore
print("Second Recipe Time:", all_recipes[1][4], "mins") # type: ignore
print("pasta slice:", all_recipes[0][0][6:]) # type: ignore
print("\nPasta Recipe Details:", all_recipes[0][1:]) # type: ignore
for recipe in all_recipes: # type: ignore
    print("\nRecipe Name:", recipe[0]) # type: ignore
    print("Cuisine:", recipe[1]) # type: ignore
    print("Cooking Time:", recipe[2], "mins") # type: ignore
# STEP 1 - Create sets for ingredients (no duplicates allowed)
pasta_ingredients = {"tomato", "garlic", "olive oil", "chili", "pasta", "garlic"}
biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}

print("Bi-yani ingredients:", biryani_ingredients)
print("Total Pasta ingredients:", len(pasta_ingredients))

# STEP 2 - Modify the set
pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chili")

print("\nUpdated pasta ingredients:", pasta_ingredients)

# STEP 3 - Set operations
# 1. Union: Elements present in either or both sets
all_ingredients = pasta_ingredients.union(biryani_ingredients)

# 2. Intersection: Elements present in both sets
common_ingredients = pasta_ingredients.intersection(biryani_ingredients)

# 3. Difference: Elements in pasta but not in biryani
only_pasta = pasta_ingredients.difference(biryani_ingredients)

# 4. Symmetric Difference: Elements in either set, but not both
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

# Print results
print("\nAll Ingredients (union):", all_ingredients)
print("Common Ingredients (intersection):", common_ingredients)
print("Only in Pasta (difference):", only_pasta)
print("Unique to each (symmetric difference):", unique_to_each)
