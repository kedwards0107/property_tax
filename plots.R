

library(tidyverse)
tax <- read.csv("combined_dataframe_filter3.csv", stringsAsFactors = FALSE)
tax <- as.tibble(tax)
tax$Finished_Basement <- as.logical(Finished_Basement)
tax$Sale.Date <- as.Date(tax$Sale.Date, format="%m/%d/%Y")
str(tax)


# boxplot of sales price by unit style
my.box <- ggplot(data = tax, aes(x = LUC, y = Sales.Price))
my.box + geom_boxplot(outlier.color = "red", outlier.shape = 4) + 
  geom_jitter(width = 0.2, aes(color = Finished_Basement)) +
  labs(title = "Price range by unit style") +
  scale_y_continuous(breaks = c(170000,190000,210000,230000,250000,270000,290000,310000)) +
  theme_light()

# boxplot of sales price by tax
my.box <- ggplot(data = tax, aes(x = LUC, y = Total))
my.box + geom_boxplot(outlier.color = "red", outlier.shape = 4) + 
  geom_jitter(width = 0.2, aes()) +
  labs(title = "Tax by unit style") +
  theme_light()



# scatterplot sales date by price and separated by unit style
sp <- ggplot(tax, aes(Sale.Date, Sales.Price))
sp + geom_point(aes(color = LUC), shape = 21, fill = "white",
                size = 3, stroke = 2) + theme_light() +
  scale_y_continuous(breaks = c(170000,190000,210000,230000,250000,270000,290000,310000)) +
  labs(x = "Sale Date",
       y = "Sale Price",
       title = "Home Prices by Date") + 
  facet_wrap(~LUC) +
  theme(legend.position = "none") +
  stat_smooth(se = FALSE)
