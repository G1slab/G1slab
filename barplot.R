library(tidyverse)

myData <- read.csv('DB3_bulk_L1_L2.vaf.barplot_sorted_truesort_100percent.csv', header = T, sep =',') #must be specific format for dataframe #row.names -> index_col

ggplot(data = myData, aes(x = region, y = vaf_2, fill = type)) + 
  geom_bar(stat = "identity", width = 0.4) +
  coord_flip()
  #geom_col() <- this makes bar width no use