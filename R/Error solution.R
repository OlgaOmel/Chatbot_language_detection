# R очень помог, так как один скачанный из интернета дф 
# не хотел открываться в питоне с error и спокойно открылся в R

install.packages("tidyr")
install.packages("dplyr")
library(tidyr)
library(dplyr)
df <- read.csv("multi_test.csv")

df$Utterance0. <- gsub(";", "", df$Utterance0.)

df <- df %>% filter(Utterance0. != "")

df <- df %>% distinct()

rows_to_remove <- grep("\\*", df$Utterance0.)
df <- df[-rows_to_remove,]
write.csv(df, file = "1.csv", row.names = FALSE)

# новая часть
df <- read.csv("Conversation.csv")
df$X <- NULL 
df$text <- paste(df$question, df$answer, sep = " ")
df <- df[, -c(1:2)]
write.csv(df, file = "2.csv", row.names = FALSE)