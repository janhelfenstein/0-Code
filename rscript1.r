# Author: Jan Helfenstein
# Date: 2025-03-24

library(tidyverse)
library(ggplot2)
library(dplyr)

data_2023 = read_csv("data/raw/SM10K-2023-raw.csv")


# test basic course knowledge
library(gapminder)

gapminder_2007 <- gapminder |>
    filter(year == 2007)

ggplot(data = gapminder_2007,
      mapping = aes(x = continent,
                   y = lifeExp,
                   fill = continent
                   )
      ) +
    geom_boxplot()

# somehow the plot doesn't appear