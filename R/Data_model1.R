df <- data.frame(language = character(), text = character(), stringsAsFactors = FALSE)

#мои русские отдельные df под каждый тип предложений
file1 <- read.csv("rus.csv")
temp_df1 <- rbind(df, data.frame(language = "Russian", text = file1$sentence))
write.csv(temp_df1, file = "russian_1.csv", row.names = FALSE)
file2 <- read.csv("Тикеты.csv")
temp_df2 <- rbind(df, data.frame(language = "Russian", text = file2$x))
write.csv(temp_df2, file = "russian_2.csv", row.names = FALSE)
file3 <- read.csv("rus_bridget_sentences.csv")
temp_df3 <- rbind(df, data.frame(language = "Russian", text = file3$Text))
write.csv(temp_df3, file = "russian_3.csv", row.names = FALSE)

#Соединяем все русские df
russian_df <- rbind(temp_df1, temp_df2, temp_df3)
write.csv(russian_df, file = "russian_data.csv", row.names = FALSE)

#мои англ отдельные df под каждый тип предложений
file1 <- read.csv("eng.csv")
temp_df1 <- rbind(df, data.frame(language = "English", text = file1$sentence))
write.csv(temp_df1, file = "english_1.csv", row.names = FALSE)
file2 <- read.csv("Conversation.csv")
temp_df2 <- rbind(df, data.frame(language = "English", text = file2$x))
write.csv(temp_df2, file = "english_2.csv", row.names = FALSE)
file3 <- read.csv("eng_bridget_sentences.csv")
temp_df3 <- rbind(df, data.frame(language = "English", text = file3$Text))
write.csv(temp_df3, file = "english_3.csv", row.names = FALSE)

#Соединяем все английские df
english_df <- rbind(temp_df1, temp_df2, temp_df3)
write.csv(english_df, file = "english_data.csv", row.names = FALSE)

#Соединяем русский и английский df
both_df <- rbind(english_df, russian_df)
write.csv(both_df, file = "all_data.csv", row.names = FALSE)