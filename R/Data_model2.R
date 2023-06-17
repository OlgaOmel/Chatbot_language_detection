df <- read.csv("english_1.csv")

short_df <- head(df, 96000)
write.csv(short_df, file = "short_english_1.csv", row.names = FALSE)

#сделали английские отдельные df под каждый тип предложений

english1 <- read.csv("short_english_1.csv")
english2 <- read.csv("english_2.csv")
english3 <- read.csv("english_3.csv")

#Соединяем все английские df

english_combined <- rbind(english1, english2, english3)
write.csv(english_combined, "English_data_short.csv", row.names = FALSE)

#Соединяем русский и английский df

english <- read.csv("English_data_short.csv")
russian <- read.csv("russian_data.csv")
both_df <- rbind(english, russian)

#записываем в общий английский csv
write.csv(both_df, "English_short_Russian.csv", row.names = FALSE)
