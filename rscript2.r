vector1 = c(1,2,3,4,5)

library(palmerpenguins)
penguins_adelie <- penguins |>
    filter(species == "Adelie") |>
    select(species, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g) |>
    mutate(bill_ratio = bill_length_mm / bill_depth_mm)

write_csv(penguins_adelie, "data/processed/penguins_adelie.csv")
