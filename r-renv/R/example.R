# Referenced with modifications from https://dplyr.tidyverse.org/
library(dplyr)

df <- starwars %>% 
  filter(species == "Droid")

print(df)
