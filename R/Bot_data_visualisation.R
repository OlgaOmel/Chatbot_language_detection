library(ggplot2)
library(dplyr)

data1 <- read.csv("data.csv")
data2 <- read.csv("English_short_Russian.csv")

# bar
ggplot(data2, aes(x = language, fill = language)) +
  geom_bar(width = 0.8, position = position_dodge(width = 0.5)) +
  geom_text(stat='count', aes(label=..count..), position = position_dodge(width=0.5), vjust=1.5, size=4, color="white") +
  labs(title = "Number of texts (English & Russian)", x = "Language", y = "Count") +
  theme_minimal() +
  theme(legend.position = "none")

# pie
lang_counts <- data2 %>%
  group_by(language) %>%
  summarize(count = n())

ggplot(lang_counts, aes(x = "", y = count, fill = language)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar(theta = "y") +
  geom_text(aes(label = paste0(round(count/sum(count)*100), "%")),
            position = position_stack(vjust = 0.5)) +
  labs(fill = "Language", x = NULL, y = NULL, title = "Language Distribution") +
  theme_void()