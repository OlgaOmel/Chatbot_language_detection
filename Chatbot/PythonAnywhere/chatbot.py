import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random
from random import choice
def read_file(file_name):
    with open(file_name,'r') as file:
        return(file.read())
bot = telebot.TeleBot(read_file("bot.ini"))
robot_facts_eng = ['Chatbots are the fastest-growing brand communication channel, and the chatbot market size has increased by 92% over the last couple of years.', 'In 2020, almost one-quarter of purchasers used chatbots when communicating with businesses, which is a 13% increase from the previous year.', '67% of consumers worldwide have interacted with a chatbot in the previous 12 months.', 'On Facebook, there are more than 300,000 active chatbots, which was a three-fold increase from the previous year and perfectly illustrated the chatbot trend that’s been emerging over the past few years.', '68.9% of chats are handled from start to finish.', 'A chatbot platform can answer as much as 80% of all standard simple questions.', '1.4 billion people use chatbots.', 'This year, almost one in six global customer service interactions were handled by conversational AI (artificial intelligence).', '27% of consumers were unsure whether the last customer support interaction they had was with a chatbot or a real person.', 'When Facebook launched its messaging platform, it became the leading platform for chatbots.', 'More than 40% of consumers use conversational marketing tools for purchases, making them an excellent addition to your salesforce.', '87.2% of consumers report having a neutral or positive customer experience with chatbots.', 'Only 12.8% report a negative customer experience.', 'The number one reason consumers use chatbots is to get a quick answer.', 'Conversational marketing tools are used by 41.3% of consumers when making a purchase.', 'One-third of consumers would like to use a chatbot for making reservations.', 'On average, bot-only chats get a customer satisfaction rate of 87.58%, which is 2% higher than the rate for discussions that get passed over to human agents.', 'The US has the most chatbot users (36%), followed by India (11%) and Germany (4%).', '41% of people who start online chat conversations with businesses are C-level executives.', '27% of consumers are currently interested in AI (artificial intelligence) support tools.', '37% of people use a customer service bot to get a quick answer in an emergency.', 'Baby boomers are more likely to expect benefits from chatbots than millennials.', 'Almost 50% of female shoppers like chatbots and choose them to communicate when making purchases online, whereas only 36.81% of men do the same.', 'One in five live chats is ignored and not answered.', 'Millennials use social media apps more than any other generation, and three in five have used chatbots at least once in their lives.', '58% of B2B companies use chatbots, while only 42% of B2C websites have chatbots,\xa0according to Relay. Chatbots are more popular in B2B because they are successful in lead generation, which is important for B2B companies.', '39% of businesses use chatbots to make their websites more interactive.', '65.1% of businesses that have adopted chatbots are SaaS companies.', '35% of consumers say they would like to see more companies taking advantage of chatbots.', '24% of enterprises, 15% of mid-sized companies, and 16% of small businesses are currently using chatbots.', '60% of people have engaged with a chatbot in the last year.', 'By 2023, we could be talking to bots more than our partners.', '53% of service organizations say they plan to use chatbots within 18 months, which is a 136% growth rate.', '56% of businesses consider chatbots to be driving disruption in their industry.', 'Average chatbots generate 35-40% response rates.', 'The best bot experiences with more engaged customers can generate up to 90% response rates.', 'Chatbot technology can increase website conversion rates on average by between 10% and 100%, depending on the industry.', 'E-commerce stores that have adopted the social media Facebook Messenger chatbot along with an abandoned cart chatbox have been able to boost revenue by between 7 and 25%.', 'Nearly one-quarter of respondents trust virtual assistant recommendations for product purchases rather than a human salesforce.', 'Better bot experiences together with more engaged audiences, are getting 80-90% response rates.', 'Business leaders claim that, on average, chatbots have increased sales by 67%.', '57% of businesses say that chatbot delivers a massive ROI on minimal investment.', 'Chatbots have a faster response time than actual humans.', 'According to 68% of consumers, they like chatbots because they provide speedy answers.', 'Other features consumers like are the fact that a chatbot can help outside of business hours and forward them to a real person.', 'According to consumers, the #1 chatbot benefit is 24/7 support.', 'Chatbots have helped cut operational customer service costs by up to 30%.', 'Two of the biggest chatbot concerns for consumers are a lack of understanding and an inability to solve complex issues.', 'Almost half of the consumers think chatbots get in the way of them communicating with a live agent.', '60% of consumers thank that chatbot can’t understand their needs as well as a human.', '60% of consumers would prefer to wait and speak to a human rather than a chatbot.', 'Chatbots are used by 55% of businesses to generate higher-quality leads.', 'Business leaders say that chatbots have increased sales by 67%.', '40% of US, EU, and Chinese businesses use pre-built AI programs, including virtual agents and chatbots.', 'Chatbots are most commonly used for sales (41%), customer support (37%), and marketing (17%).', 'Top AI (artificial intelligence) chatbots use is for voice-to-text dictation (46%) and support team collaboration on tasks (26%).', '64% of businesses believe that chatbots will allow them to provide a more customized customer experience.', '50% of businesses plan on spending more on voice assistants than on mobile apps.', 'Companies with up to fifty employees use chatbots more than others.', 'Messaging apps have more than five billion active users a month.', '1.4 billion people use messaging apps and are happy to talk to chatbots.', 'In 2018, Blue-Bot sent two million messages to more than 500,000 customers.', 'There are more than 300,000 chatbots on Facebook Messenger.', 'Mobile apps account for 10 out of every 11 minutes people spend on their mobile devices.', 'Conversations between brands and customers via Messenger have a 30% better ROI than retargeting ads.', 'Three out of five millennials have used a chatbot at least once.', '47% of chatbot users purchase items.', '33% of internet users prefer conversational chatbots when making reservations and ordering online.', 'More than half of consumers prefer using chatbots instead of calling customer support.', 'The top three work-related AI chatbots are Microsoft Cortana (49%), Apple Siri (47%), and Google Assistant (23%).', '53% of consumers are more likely to shop if they can message the business.', '48% of people would rather a chatbot was able to solve their issues above having a personality.', 'The top five industries that benefit most from using chatbots are real estate (28%), travel (16%), education (14%), healthcare (10%, and finance (5%).', 'Real estate is the most profitable field for chatbots.', 'Projections are that chatbots will handle 75-90% of banking and healthcare customer queries by 2023', 'Cost savings from banking chatbots will reach $7.3 billion globally by 2023.', 'Two-thirds of leading global financial service firms have started using chatbots for their apps since the start of the global pandemic.', 'Two-thirds of people surveyed said they would find a chatbot useful (40%) or very useful (26%) in relation to the management of their business and work travel arrangements.', 'When making travel plans or comparing booking options, 37% of users would prefer to deal with an intelligent chatbot.', 'If it could save them time and money, 87% of users would choose a travel chatbot to interact with.', 'A chatbot from GRT Hotels & Resorts has exchanged more than 175,000 messages in the two and a half months following its launch.', 'Just over one-third of retail customers would happily speak with customer service via an AI chatbot rather than live chat.', 'By 2023, over 70% of chatbot conversations will be with retail chatbots.', 'In 2019, a survey found that more than 40% of US consumers had used chatbots to engage with the retail industry.', 'The most popular product sold online with the help of chatbots is clothing.', '22% of the most successful online stores sell clothes, followed by health products (9%), furniture (9%), electronics (8%), and jewelry (8%).', 'By the end of 2023, expectations are that 35% of organizations will use chatbots for a large part of the recruitment process.', 'XOR, a recruiting chatbot vendor, claims their chatbot solution improves the recruitment process by 33%, screens 85% more resumes with the same budget, and spends 50% less per hire.', 'According to a survey by Allegis, 58% of candidates were happy to interact with AI and recruitment chatbots during the early stages of the application process.', 'If you use abandoned cart chatbots alongside Messenger, you can boost your eCommerce revenue by up to 25%.', 'You can expect to save 30% on customer support costs by using chatbots.', 'In 2019, a growth rate of 136% was the prediction for customer service organizations.', '58% of consumers say their customer service expectations have been changed by chatbots.', '64% of customer support agents who use chatbots say they have more time to solve more complex and challenging problems.', '16% of Americans have used Alexa or Google Home chatbots when shopping.', '53% of companies use AI chatbots in their IT department, and only 23% use them for administrative tasks.', 'ELIZA, the first automated chatbot, was created in 1966.', 'The top five countries in terms of chatbot use are the USA, India, Germany, the UK, and Brazil.', 'By the end of 2019, estimates were that almost a quarter of the world’s population was using chatbots.', 'By the end of 2021, $5 billion will be invested in chatbots.', 'In 2018, chatbot interest increased by 160%.', 'Software represents around 40% of all cognitive artificial intelligence spending, and two areas of focus are conversational artificial intelligence and machine learning applications.', 'Predictions are that by 2024, consumer retail spending via voice bots worldwide will reach $142 billion, up from $2.8 billion in 2019.', 'Around 47% of organizations plan to have chatbots for customer support by the end of 2021.', 'Two-thirds of financial service companies have added chatbots to their apps.', 'The US is a global leader with almost 16,000 websites with a chatbot.', 'The healthcare chatbot market is estimated to reach $340 million by 2027.', '80% of businesses are projected to integrate some form of conversational bot system by 2023.', 'Social media is aimed to dominate AI integration.', 'By 2023, the predictions are that chatbot eCommerce transactions will hit $112 billion.', 'By 2023, estimates are that chatbots will save businesses $8 billion.', 'Chatbots are predicted to save businesses 2.5 billion hours by 2023.', 'By 2023, chatbots will be reducing cost per customer interaction by $0.70.', 'It is thought the global chatbot market will reach over $994 million by 2024.', '96% of businesses think that chatbots are here to stay.', 'Chatbots may take over email marketing.', '85% of customer interactions might be handled without a human agent by the end of 2021.']
robot_facts_rus = ['Чат-боты являются самым быстрорастущим видом бизнес-коммуникации, а объем рынка чат-ботов за последние пару лет увеличился на 92%.', 'В 2022 году почти четверть покупателей использовали ботов для коммуникации с компаниями, что на 13% больше, чем годом ранее.', '77% потребителей по всему миру использовали чат-ботов за последние 12 месяцев.', 'Вконтакте насчитывает более 160 000 активных чат-ботов, что в 3 раза больше, чем в предыдущем году, и прекрасно иллюстрирует тенденцию использования чат-ботов, которая сформировалась за последние несколько лет.', '68,9% диалогов обрабатываются ботами от начала и до конца сценария.', 'Боты могут покрывать 80-90% всех стандартных простых вопросов.', '1,4 миллиарда человек регулярно используют чат-ботов.', 'В этом году почти каждое шестое обращение в службу поддержки клиентов в мире обрабатывалось с помощью диалогового ИИ (искусственного интеллекта).', '27% потребителей не были уверены, с кем в последний раз общались при обращении в службу поддержки: с ботом или с реальным человеком.', 'Когда Facebook запустил свою платформу обмена сообщениями, она стала ведущей платформой для чат-ботов.', 'Более 40% потребителей используют диалоговые маркетинговые инструменты для покупок, что делает их отличным дополнением к вашим продажам.', '87,2% потребителей сообщают о нейтральном или положительном опыте работы с ботами.', 'Только 12,8% сообщают о негативном клиентском опыте при работе с ботами.', 'Причина №1, благодаря которой потребители используют чат-ботов, — получить моментальный ответ.', 'Инструменты диалогового маркетинга используют 41,3% потребителей при совершении покупки.', 'Одна треть потребителей предпочла бы использовать бота для бронирований.', 'В среднем, клиентская поддержка с помощью ботов имеет уровень удовлетворенности клиентов 87,58%, что на 2% выше, чем показатель удовлетворенности от поддержки с сотрудниками-людьми.', 'В США больше всего пользователей ботов (36%), за ними следуют Индия (11%) и Германия (4%).', '41% людей, которые начинают общение в онлайн-чатах с компаниями, являются руководителями высшего звена.', '27% потребителей в настоящее время интересуются инструментами поддержки на базе ИИ (искусственного интеллекта).', '37% людей используют бота службы поддержки, чтобы получить быстрый ответ в экстренной ситуации.', 'Бумеры с большей вероятностью ожидают получение выгоды от ботов, чем миллениалы.', 'Почти 50% покупателей-женщин любят ботов и выбирают их для общения при совершении покупок в интернете, в то время как только 36,81% мужчин поступают аналогично.', 'Каждый пятый чат поддержки игнорируется и на него не отвечают.', 'Миллениалы используют приложения для соцсетей чаще, чем любое другое поколение, а трое из пяти использовали ботов хотя бы раз в жизни.', 'По данным Relay, 58% компаний B2B используют чат-ботов, в то время как только 42% сайтов B2C используют чат-ботов. Чат-боты более популярны в B2B секторе, потому что они эффективны для лидогенерации, что важно для B2B-компаний.', '39% компаний используют чат-ботов, чтобы сделать свои сайты более интерактивными.', '65,1% компаний, внедривших ботов, — это SaaS-компании.', '35% потребителей говорят, что хотели бы, чтобы больше компаний использовали ботов.', 'В настоящее время ботов используют 24% предприятий, 15% компаний среднего размера и 16% малых предприятий.', '85% людей взаимодействовали с ботами в течение последнего года.', 'К 2024 году мы будем говорить с ботами чаще, чем с живыми сотрудниками.', '53% сервисных организаций заявили, что планируют внедрить ботов в течение 18 месяцев, что соответствует темпам роста 136%.', '56% компаний считают, что боты меняют их отрасль.', 'В среднем боты генерируют 35-40% ответов.', 'Правильно выстроенное взаимодействие ботов с наиболее заинтересованными клиентами может обеспечить до 90% откликов.', 'Технология ботов может увеличить конверсию веб-сайта на 10-100%, в зависимости от отрасли.', 'Интернет-магазины, которые внедрили ботов в свои социальные сети, смогли увеличить доход на 7–25%.', 'Почти четверть респондентов доверяют рекомендациям виртуального помощника при покупке продуктов, но не доверяют торговому персоналу.', 'Правильно выстроенное взаимодействие ботов с наиболее заинтересованной аудиторией может обеспечить 80-90% ответов.', 'Бизнес-лидеры утверждают, что в среднем боты увеличили продажи на 67%.', '57% компаний говорят, что боты обеспечивают высокую рентабельность инвестиций при минимальных вложениях.', 'Боты имеют гораздо более быстрое время отклика, чем реальные люди.', 'По словам 68% потребителей, им нравятся боты, потому что они дают быстрые ответы.', 'Потребителям нравится, что боты помогают в нерабочее время и могут перенаправить их запрос реальному человеку.', 'По мнению потребителей, преимущество №1 у ботов — это круглосуточная поддержка 7 дней в неделю.', 'Боты помогли сократить операционные расходы на обслуживание клиентов до 30%.', 'Две самые большие проблемы ботов у потребителей — непонимание и неспособность решать сложные проблемы.', 'Почти половина потребителей считает, что боты мешают им общаться с реальными сотрудниками.', '60% потребителей расстраивается о того, что бот не может понять их потребности так же хорошо, как человек.', '60% потребителей предпочли бы подождать и поговорить с человеком, а не с чат-ботом.', '55% предприятий используют ботов для получения более качественных лидов.', 'Лидеры бизнеса говорят, что боты увеличили продажи на 67%.', '40% предприятий США, ЕС и Китая используют готовые программы искусственного интеллекта, включая виртуальных агентов и ботов.', 'Боты чаще всего используются для продаж (41%), поддержки клиентов (37%) и маркетинга (17%).', 'Чаще всего боты с искусственным интеллектом используют для информирования (46%) и клиентской поддержки (26%).', '64% компаний считают, что боты позволяют им обеспечить более индивидуальный подход к клиентам.', '50% компаний планируют тратить на голосовых помощников больше, чем на мобильные приложения.', 'Компании, в которых работает до 50 сотрудников, чаще других используют ботов.', 'Мессенджеры имеют более пяти миллиардов активных пользователей в месяц.', '1,4 миллиарда человек ежедневно используют мессенджеры и с удовольствием общаются в них с чат-ботами.', 'В 2018 году компания Blue Robot отправила два миллиона сообщений более чем 500 000 клиентов.', 'В Facebook Messenger более 300\xa0000 чат-ботов.', 'Из каждых 11 минут, которые люди проводят, используя свои мобильные устройства, 10 минут приходятся на мобильные приложения.', 'Коммуникация между компаниями и клиентами через мессенджер приносит на 30% больше прибыли, чем рекламный таргет.', '3 из 5 миллениалов хотя бы раз использовали бота.', '47% пользователей ботов покупают с их помощью товары.', '33% интернет-пользователей предпочитают диалоговых чат-ботов при бронировании и доставке на дом.', 'Более половины потребителей предпочитают использовать ботов вместо того, чтобы звонить в службу поддержки.', 'В тройку лучших ботов с искусственным интеллектом для бизнеса входят Алиса (73%), Apple Siri (17%) и Google Assistant (10%).', '53% потребителей с большей вероятностью сделают покупки, если смогут отправить сообщение компании.', '48% людей предпочли бы, чтобы бот мог решить их проблему, а не человек.', 'В первую пятерку отраслей, которые больше всего выигрывают от использования ботов, входят недвижимость (28%), путешествия (16%), образование (14%), здравоохранение (10% и финансы (5%).', 'Недвижимость — самая прибыльная сфера для чат-ботов.', 'По оценкам, в 2023 году боты обрабатывают 75–90% запросов клиентов банков и медицинских учреждений.', 'В 2023 году экономия средств благодаря банковским ботам достигла 7,3 миллиарда долларов во всем мире.', 'Две трети ведущих мировых компаний, предоставляющих финансовые услуги, начали использовать чат-ботов в своих приложениях с началом глобальной пандемии.', 'Две трети опрошенных сказали, что сочли бы бота полезным (40%) или очень полезным (26%) в своих повседневных бизнес-задачах, и особенно для организации рабочих поездок.', 'При составлении планов поездок или сравнении вариантов бронирования 37% пользователей предпочли бы иметь дело с умным ботом.', 'Если бы это могло сэкономить им время и деньги, 87% пользователей выбрали бы бота для организации путешествий.', 'Чат-бот от GRT Hotels & Resorts за два с половиной месяца после запуска обменялся более чем 175\xa0000 сообщений.', 'Более трети розничных клиентов с удовольствием общались бы со службой поддержки через бота с искусственным интеллектом, а не через диалог с реальным сотрудником.', 'В 2023 году более 70% чатов с клиентами ведутся с помощью чат-ботов.', 'В 2022 году опрос показал, что более 68% потребителей в США использовали ботов для покупок.', 'Самый популярный товар, продаваемый онлайн с помощью чат-ботов, — это одежда.', 'Из самых успешных интернет-магазинов 22% продают с помощью ботов одежду, за ними следуют товары для здоровья (9%), мебель (9%), электроника (8%) и ювелирные изделия (8%).', 'Ожидается, что к концу 2023 года 35% организаций будут использовать ботов для первоначального этапа найма новых сотрудников.', 'Xor.ai, разработчик чат-ботов для рекрутинга, утверждает, что их решение улучшает процесс найма на 33%. Чат-бот просматривает на 85% больше резюме при том же бюджете и тратит на найм на 50% меньше.', 'Согласно опросу, проведенному Allegis, 58% кандидатов были рады взаимодействовать с ИИ и чат-ботами по подбору персонала на ранних этапах процесса подачи заявки.', 'При использовании бота для решения проблемы «брошенных корзин», вы можете увеличить свой доход от интернет-продаж на 25%.', 'Используя чат-бота, компания может сэкономить на 30% расходов на поддержку клиентов.', 'В 2021 году у организаций, связанных с клиентским сервисом, был зафиксирован значительный рост использования ботов (136%).', '58% потребителей говорят, что боты подняли их планку требований в отношении обслуживания клиентов.', '64% сотрудников службы поддержки, говорят, что у них теперь больше времени для решения более сложных проблем клиентов.', '16% американцев использовали помощников Alexa или Google Assistant для совершения покупок.', '53% компаний используют ботов с искусственным интеллектом в своем IT-отделе, а 23% используют их для административных задач.', 'ELIZA, первый чат-бот, был создан в 1966 году.', 'В первую пятерку стран по использованию ботов входят США, Индия, Германия, Великобритания и Бразилия.', 'По оценкам, к концу 2019 года почти четверть населения мира использовала ботов.', 'По оценкам, к концу 2021 года в чат-ботов было инвестировано 5 миллиардов долларов.', 'В 2018 году интерес к чат-ботам вырос на 160%.', 'На программное обеспечение приходится около 40% всех расходов на когнитивный искусственный интеллект, и два основных направления — разговорный искусственный интеллект и машинное обучение.', 'По прогнозам, к 2024 году потребительские розничные расходы с помощью голосовых ботов во всем мире достигнут 142 миллиардов долларов по сравнению с 2,8 миллиардами долларов в 2019 году.', 'Около 47% организаций использовали чат-ботов для поддержки клиентов к концу 2021 года.', 'Две трети компаний, предоставляющих финансовые услуги, добавили чат-ботов в свои приложения.', 'США являются мировым лидером с почти 16 тыс. веб-сайтов с чат-ботами.', 'По прогнозам, к 2027 году рынок медицинских чат-ботов достигнет 340 млн. $.', 'По прогнозам, к концу 2023 года 80% предприятий интегрируют ту или иную форму диалоговых ботов.', 'Социальные сети нацелены на то, чтобы доминировать в интеграции ИИ.', 'По прогнозам, к концу 2023 года транзакции электронной коммерции ботов достигнут 112 миллиардов $.', 'По прогнозам, к концу 2023 года боты сэкономят компаниям 8 млрд. $.', 'По прогнозам, к концу 2023 года боты сэкономят предприятиям 2,5 млрд. рабочих часов.', 'К 2023 году боты снизили стоимость коммуникации с клиентом на 0,7 $.', 'Считается, что к 2024 году мировой рынок чат-ботов превысит 994 млн. $.', '96% компаний уверены, что боты не потеряют свою актуальность в ближайшие годы.', 'Чат-боты могут эффективно выполнять задачи интернет-маркетинга.', '85% взаимодействий с клиентами могут осуществляться без участия человека.']
import pickle
with open('LanguageModel.pckl', 'rb') as f:
    language_detection_model = pickle.load(f)
@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.id
    sticker = "CAACAgIAAxkBAAJTyWR6Z4fttTULK3KHnZaefPNZOP6GAAIBAQACVp29CiK-nw64wuY0LwQ"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton("🇷🇺 Русский"), types.KeyboardButton('🇬🇧 English'))
    bot.send_sticker(user, sticker)
    bot.send_message(user, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == '👩‍💼 Связаться с менеджером')
def handle_manager_contact(message):
    user = message.chat.id
    markup_inline = types.InlineKeyboardMarkup()
    sender = bot.send_message
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn01 = types.KeyboardButton('🔙 Главное меню')
    btn1 = types.KeyboardButton('📞 Оставить контакт', request_contact=True)
    markup.row(btn1)
    markup.row(btn01)
    btn00 = types.InlineKeyboardButton('⬅️ Назад', callback_data='about_booking')
    markup_inline.add(btn00)
    sender(user, '📞 Пожалуйста, нажмите на кнопку ниже, чтобы сообщить свой номер телефона. Наш сотрудник скоро свяжется и проконсультирует по любому вопросу 🤗', reply_markup=markup)
    sender(user, '🙌 Также можно оставить сообщение в форме для обратной связи у нас [на сайте](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat) или в [гугл-форме](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat', reply_markup=markup_inline, parse_mode='Markdown')
@bot.message_handler(func=lambda message: message.text == '👩‍💼 Book a meeting')
def handle_manager_contact(message):
    user = message.chat.id
    markup_inline = types.InlineKeyboardMarkup()
    sender = bot.send_message
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn01 = types.KeyboardButton('🔙 Главное меню')
    btn1 = types.KeyboardButton('📞 Send your phone number', request_contact=True)
    markup.row(btn1)
    markup.row(btn01)
    btn00 = types.InlineKeyboardButton('⬅️ Back', callback_data='about_booking_eng')
    markup_inline.add(btn00)
    sender(user, '📞 Please, press the button below to provide your phone number. Our employee will contact you soon and advise you on any issue 🤗', reply_markup=markup)
    sender(user, '🙌 You can also leave a message in the feedback form with us [on our website](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat) or in [гугл-форме](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat) using correct contact details', reply_markup=markup_inline, parse_mode='Markdown')
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    user = message.from_user.id
    sender = bot.send_message
    sticker = "CAACAgIAAxkBAAJh2GSMDJ54yrvAcF9gUbqF4FHJjUAjAAL-AANWnb0K2gRhMC751_8vBA"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🔙 Главное меню')
    btn1_eng = types.KeyboardButton('🔙 Main menu')
    markup.add(btn1, btn1_eng)
    markup_inline = types.InlineKeyboardMarkup()
    markup_inline_eng = types.InlineKeyboardMarkup()
    btn00 = types.InlineKeyboardButton('⬅️ Назад', callback_data='about_booking')
    btn00_eng = types.InlineKeyboardButton('⬅️ Back', callback_data='about_booking_eng')
    markup_inline.add(btn00)
    markup_inline_eng.add(btn00_eng)
    phone_number = message.contact.phone_number
    bot.send_sticker(user, sticker, reply_markup=markup)
    sender(-999649322, f"Контактный номер телефона: {phone_number}; ID: {message.chat.id}")
    sender(user, f"🤝 Спасибо! Вы отправили свой номер телефона: {phone_number}", reply_markup=markup_inline)
    sender(user, f"🤝 Thank you! You have sent your phone number: {phone_number}", reply_markup=markup_inline_eng)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text = message.text
    user = message.from_user.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_inline = types.InlineKeyboardMarkup()
    sender = bot.send_message
    if text == '🇷🇺 Русский':
        btn1 = types.KeyboardButton("💡 О нас")
        btn2 = types.KeyboardButton('🤖 О ботах')
        btn3 = types.KeyboardButton('💰 Cтоимость')
        btn4 = types.KeyboardButton('❓ Частые вопросы')
        btn5 = types.KeyboardButton('🤝 Консультация')
        btn6 = types.KeyboardButton('👀 А ты знаешь?')
        btn7 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.row(btn1, btn2, btn3)
        markup.row(btn4, btn5)
        markup.row(btn6)
        markup.row(btn7)
        sender(user, "👋 Мы - компания Kittens \n\nМы создаем разговорных ботов, чтобы помогать другим компаниям автоматизировать бизнес-процессы 📈")
        sender(user, '🧐 Выберите интересующий вас раздел', reply_markup=markup)

    elif text == '🔙 Вернуться к выбору языка':
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        markup.row(btn1, btn2)
        sender(user, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    elif text == '👀 А ты знаешь?':
        sender(user, random.choice(robot_facts_rus))

    elif text == '💡 О нас':
        btn1 = types.KeyboardButton('🩵 Кто мы')
        btn2 = types.KeyboardButton('💼 Что мы предлагаем')
        btn01 = types.KeyboardButton('🔙 Главное меню')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, "▫️ Наша компания Kittens помогает внедрять современные технологии в работу других компаний и улучшать процессы обработки как внутренних, так и внешних задач с помощью разговорных ботов")
        sender(user, "▫️ Боты-помощники разрабатываются под разнообразные цели и ежедневно радуют как своих работодателей, так и клиентов-собеседников 🥳")
        sender(user, '⬇ Выберите подраздел', reply_markup=markup)

    elif text == '🩵 Кто мы':
        btn00 = types.InlineKeyboardButton('⬅️ Назад', callback_data='about_us')
        markup_inline.add(btn00)
        btn01 = types.KeyboardButton('🔙 Главное меню')
        markup.row(btn01)
        sender(user, '🔐 Мы - российский системный интегратор, работающий на рынке связи, телекоммуникационных и IT-решений, инженерной инфраструктуры c 2001 года', reply_markup=markup)
        sender(user, '📌 Подробнее о компании можно узнать [на нашем сайте](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat)', reply_markup=markup_inline, parse_mode='Markdown')

    elif text == '💼 Что мы предлагаем':
        btn1 = types.InlineKeyboardButton('⬅️ Назад', callback_data='about_us')
        markup_inline.add(btn1)
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn2 = types.KeyboardButton('🔧 Как создать бота')
        markup.row(btn2, btn01)
        sender(user, "️▫️ Мы предлагаем услуги по созданию разговорных роботов")
        sender(user, "️▫️ У вас может быть только идея, без понимания что и как можно автоматизировать в бизнесе, которую мы доведем до финальной успешной эксплуатации👌 \n▫️ Все заботы по составлению сценария, настройке и интеграции с вашими системами наша команда возьмет на себя, внимательно прислушиваясь ко всем индивидуальным пожеланиям")
        sender(user, "️▫️ Вам остается только радоваться меньшему количеству нагрузки и новому сотруднику 😎🤖", reply_markup=markup)
        sender(user, '🔎 Хотите узнать как создается робот?', reply_markup=markup_inline)

    elif text == '🔧 Как создать бота':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💻 Наши решения')
        btn2 = types.KeyboardButton('🤝 Консультация')
        btn3 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_us')
        markup_inline.add(btn3)
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, "🔵 Наши шаги по созданию робота включают:")
        sender(user, "1️⃣ Заполнение брифа для первоначального знакомства с компанией \n2️⃣ Встреча с нашей командой, где мы дадим подробные ответы на техническую и организационную часть создания робота \n3️⃣ Разработка робота \n4️⃣ Тестирование работы перед финальным запуском \n5️⃣ Непрерывная поддержка работы готового помощника")
        sender(user, "🔸 Также, мы предлагаем помочь с обучением вашей команды, чтобы обеспечить максимально приятную и легкую интеграцию с уже используемыми системами", reply_markup=markup)
        sender(user, '🔎 Хотите покажу примеры решений или свяжу с нашим консультантом?', reply_markup=markup_inline)

    elif text == '💻 Наши решения':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_us')
        markup_inline.add(btn1)
        markup.add(btn01)
        sender(user, "️🔶 У нас обширный опыт в создании разнообразных разговорных решений, от традиционных ботов и до необычных проектами по индивидуальным запросам", reply_markup=markup)
        sender(user, '📌 Подробнее узнать о решениях можно [на нашем сайте](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat)', reply_markup=markup_inline, parse_mode='Markdown')

    elif text == '🔙 Главное меню':
        btn1 = types.KeyboardButton("💡 О нас")
        btn2 = types.KeyboardButton('🤖 О ботах')
        btn3 = types.KeyboardButton('💰 Cтоимость')
        btn4 = types.KeyboardButton('❓ Частые вопросы')
        btn5 = types.KeyboardButton('🤝 Консультация')
        btn6 = types.KeyboardButton('👀 А ты знаешь?')
        btn7 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.row(btn1, btn2, btn3)
        markup.row(btn4, btn5)
        markup.row(btn6)
        markup.row(btn7)
        sender(user, "🧐 Выберите интересующий вас раздел", reply_markup=markup)

    elif text == '🤖 О ботах':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💬 О чат-ботах')
        btn2 = types.KeyboardButton('🗣️ О голосовых ботах')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, '⬇ О каких роботах хотите узнать?', reply_markup=markup)

    elif text == '💬 О чат-ботах':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('📌 Пример чат-бота')
        markup.row(btn1)
        markup.row(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Назад', callback_data='about_bots')
        markup_inline.add(btn00)
        sender(user, '✍️ Отлично! Наши чат-боты - это прекрасные помощники, которые могут выполнять задачи по обработке запросов от пользователей в текстовых каналах и сделать простой и удобный сервис для пользователей.', reply_markup=markup)
        sender(user, '🧐 Хотите посмотреть пример работы чат-бота?', reply_markup=markup_inline)

    elif text == '📌 Пример чат-бота':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ К виду роботов', callback_data='about_bots')
        markup_inline.add(btn00)
        sender(user, '⚪ Помимо такого варианта кнопочного бота как я, мы можем сделать бота с распознаванием речи и общением с пользователями')
        sender(user, '✈️ Один из наших ботов - это бот для сервиса Kittens. Можете перейти и попробовать самостоятельно 👇')
        sender(user, '@BotFather', reply_markup=markup)
        sender(user, '📹 Пример работы в [видео](https://www.youtube.com/watch?v=BNSp_DFr5f0) 👈', reply_markup=markup_inline, parse_mode='Markdown')

    elif text == '🗣️ О голосовых ботах':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('📌 Пример голосового бота')
        markup.row(btn1)
        markup.row(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Назад', callback_data='about_bots')
        markup_inline.add(btn00)
        sender(user, '🔉 Отлично! Наши голосовые боты - это прекрасные помощники, которые могут выполнять задачи по обработке исходящих и входящих звонков и снижать операторскую нагрузку.', reply_markup=markup)
        sender(user, '🧐 Хотите посмотреть пример работы голосовых ботов?', reply_markup=markup_inline)

    elif text == '📌 Пример голосового бота':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('🚛 Логистика')
        btn2 = types.KeyboardButton('🚑 Медицина')
        btn3 = types.KeyboardButton('🏦 Финансы')
        markup.row(btn1, btn2, btn3)
        markup.row(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ К виду роботов', callback_data='about_bots')
        markup_inline.add(btn00)
        sender(user, '📌 Подробнее узнать о других решениях можно [на нашем сайте](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat)', reply_markup=markup, parse_mode='Markdown')
        sender(user, '⬇ Выберите сферу бизнеса', reply_markup=markup_inline)

    elif text == '🚛 Логистика':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn00 = types.InlineKeyboardButton('⬅️ К другим сферам', callback_data='about_voice_bots')
        markup_inline.add(btn00)
        markup.add(btn01)
        sender(user, '🔹 Здорово! Мы предлагаем множество решений для этой сферы, например помощь робота при найме водителей, проверка веса и расстояния грузоперевозок, напоминание о сроках хранения заказов', reply_markup=markup)
        sender(user, '👉[Здесь](https://www.youtube.com/watch?v=BNSp_DFr5f0) можно посмотреть один из примеров работы бота в этой сфере.', reply_markup=markup_inline,  parse_mode='Markdown')

    elif text == '🚑 Медицина':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ К другим сферам', callback_data='about_voice_bots')
        markup_inline.add(btn00)
        sender(user, '🔹 Здорово! Мы предлагаем множество решений для этой сферы, например обзвон для подтверждения визита к врачу, информирование о времени записи и другие варианты', reply_markup=markup)
        sender(user, '👉[Здесь](https://www.youtube.com/watch?v=BNSp_DFr5f0) можно посмотреть один из примеров работы бота в этой сфере.', reply_markup=markup_inline,  parse_mode='Markdown')

    elif text == '🏦 Финансы':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ К другим сферам', callback_data='about_voice_bots')
        markup_inline.add(btn00)
        sender(user, '🔹 Здорово! Мы предлагаем множество решений для этой сферы, например обзвон для лидогенерации с готовыми скриптами по финансовой тематике, голосовые команды для мобильного приложения и другие варианты', reply_markup=markup)
        sender(user, '👉[Здесь](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat) можно посмотреть один из примеров работы бота в этой сфере.', reply_markup=markup_inline,  parse_mode='Markdown')

    elif text == '💰 Cтоимость':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('🔎 Тарифы разработки')
        btn2 = types.KeyboardButton('🔎 Тарифы поддержки')
        btn3 = types.KeyboardButton('🤝 Консультация')
        markup.row(btn1, btn2)
        markup.row(btn3, btn01)
        sender(user, '▫️ Каждый робот оценивается индивидуально, в зависимости от количества автоматизируемых сценариев, их сложности, а также необходимых интеграций с внешними системами')
        sender(user, '🔵 Стоимость бота включает в себя: \n\n1️⃣ Единоразовый тариф для разработки и настройки робота \n2️⃣ Регулярный тариф по поддержке работы робота')
        sender(user, '▫️ Для того, чтобы точно посчитать стоимость бота для конкретно Ваших задач, необходимо провести консультацию и уточнить детали. \n▫️ Однако, чтобы помочь сориентироваться в стоимости, мы предлагаем ознакомиться со средними тарифами')
        sender(user, '⬇ Выберите тип услуги', reply_markup=markup)

    elif text == '🔎 Тарифы разработки':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💬 Разработка чат-бота')
        btn2 = types.KeyboardButton('🗣️ Разработка голосового бота')
        btn3 = types.KeyboardButton('✌️ Параллельная разработка')
        btn4 = types.KeyboardButton('🤝 Консультация')
        markup.row(btn1, btn2)
        markup.row(btn3)
        markup.row(btn4, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Другие тарифы', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, 'Тарифы отличаются, в зависимости от вида робота. Кроме того, возможна параллельная разработка: создается чат-бот и его сценарий адаптируется под голосового бота', reply_markup=markup)
        sender(user, '⬇ Выберите тип робота', reply_markup=markup_inline)

    elif text == '💬 Разработка чат-бота':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💬 Тариф XS')
        btn2 = types.KeyboardButton('💬 Тариф S')
        btn3 = types.KeyboardButton('💬 Тариф M')
        btn4 = types.KeyboardButton('💬 Тариф L')
        btn5 = types.KeyboardButton('🤝 Консультация')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, 'Тарифы отличаются, в зависимости от количества уникальных пользователей и веток сценария')
        sender(user, 'Наша команда поможет индивидуально подобрать тариф во время консультации', reply_markup=markup)
        sender(user, '⬇ Выберите тариф', reply_markup=markup_inline)

    elif text == '💬 Тариф XS':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup_inline = types.InlineKeyboardMarkup()
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф XS\n \n👍🏻 Хороший выбор, если маленькое количество уникальных пользователей и/или от 1 до 2 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 50.000 рублей', reply_markup=markup_inline)

    elif text == '💬 Тариф S':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup_inline = types.InlineKeyboardMarkup()
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф S\n \n👍🏻 Хороший выбор, если небольшое количество уникальных пользователей и/или от 2 до 4 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 100.000 рублей', reply_markup=markup_inline)

    elif text == '💬 Тариф M':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф M\n \n👍🏻 Хороший выбор, если среднее количество уникальных пользователей и/или от 4 до 8 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 150.000 рублей', reply_markup=markup_inline)

    elif text == '💬 Тариф L':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф L\n \n👍🏻 Хороший выбор, если большое количество уникальных пользователей и/или от 8 до 12 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 250.000 рублей', reply_markup=markup_inline)

    elif text == '🗣️ Разработка голосового бота':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('🗣️ Тариф XS')
        btn2 = types.KeyboardButton('🗣️ Тариф S')
        btn3 = types.KeyboardButton('🗣️ Тариф M')
        btn4 = types.KeyboardButton('🗣️ Тариф L')
        btn5 = types.KeyboardButton('🤝 Консультация')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, 'Тарифы отличаются, в зависимости от количества минут и веток сценария')
        sender(user, 'Наша команда поможет индивидуально подобрать тариф во время консультации', reply_markup=markup)
        sender(user, '⬇ Выберите тариф', reply_markup=markup_inline)

    elif text == '🗣️ Тариф XS':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф XS\n \n👍🏻 Хороший выбор, если маленькое количество минут и/или от 1 до 2 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 65.000 рублей', reply_markup=markup_inline)

    elif text == '🗣️ Тариф S':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф S\n \n👍🏻 Хороший выбор, если небольшое количество минут и/или от 2 до 4 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 115.000 рублей', reply_markup=markup_inline)

    elif text == '🗣️ Тариф M':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф M\n \n👍🏻 Хороший выбор, если среднее количество минут и/или от 4 до 8 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 165.000 рублей', reply_markup=markup_inline)

    elif text == '🗣️ Тариф L':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф L\n \n👍🏻 Хороший выбор, если большое количество минут и/или от 8 до 12 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 265.000 рублей', reply_markup=markup_inline)

    elif text == '✌️ Параллельная разработка':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('✌️ Тариф XS')
        btn2 = types.KeyboardButton('✌️ Тариф S')
        btn3 = types.KeyboardButton('✌️ Тариф M')
        btn4 = types.KeyboardButton('✌️ Тариф L')
        btn5 = types.KeyboardButton('🤝 Консультация')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, 'Тарифы отличаются, в зависимости от оптимального для двух ботов количества минут, уникальных пользователей и веток сценария')
        sender(user, 'Наша команда поможет индивидуально подобрать тариф во время консультации', reply_markup=markup)
        sender(user, '⬇ Выберите тариф', reply_markup=markup_inline)

    elif text == '✌️ Тариф XS':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф XS\n \n👍🏻 Хороший выбор, если маленькое количество минут и уникальных пользователей и/или от 1 до 2 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 100.000 рублей', reply_markup=markup_inline)

    elif text == '✌️ Тариф S':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф S\n \n👍🏻 Хороший выбор, если небольшое количество минут и уникальных пользователей и/или от 2 до 4 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 200.000 рублей', reply_markup=markup_inline)

    elif text == '✌️ Тариф M':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф M\n \n👍🏻 Хороший выбор, если среднее количество минут и уникальных пользователей и/или от 4 до 8 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 300.000 рублей', reply_markup=markup_inline)

    elif text == '✌️ Тариф L':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф L\n \n👍🏻 Хороший выбор, если большое количество минут и уникальных пользователей и/или от 8 до 12 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 500.000 рублей', reply_markup=markup_inline)

    elif text == '🔎 Тарифы поддержки':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💬 Поддержка чат-бота')
        btn2 = types.KeyboardButton('🗣️ Поддержка голосового бота')
        btn3 = types.KeyboardButton('✌️ Параллельная поддержка')
        btn4 = types.KeyboardButton('🤝 Консультация')
        markup.row(btn1, btn2)
        markup.row(btn3)
        markup.row(btn4, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Другие тарифы', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, 'Тарифы отличаются, в зависимости от вида робота. Кроме того, выполняется параллельная поддержка, когда в работе голосовой бот и чат-бот одновременно', reply_markup=markup)
        sender(user, '⬇ Выберите тариф', reply_markup=markup_inline)

    elif text == '💬 Поддержка чат-бота':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💬 Тариф Bronze')
        btn2 = types.KeyboardButton('💬 Тариф Standart')
        btn3 = types.KeyboardButton('💬 Тариф Gold')
        btn4 = types.KeyboardButton('💬 Тариф Brilliant')
        btn5 = types.KeyboardButton('🤝 Консультация')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, 'Тарифы отличаются, в зависимости от количества уникальных пользователей, а также степени необходимой поддержки')
        sender(user, 'Наша команда поможет индивидуально подобрать тариф во время консультации', reply_markup=markup)
        sender(user, '⬇ Выберите тариф', reply_markup=markup_inline)

    elif text == '💬 Тариф Bronze':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Bronze\n \n👍🏻 Хороший выбор, если маленькое количество уникальных пользователей и/или от 1 до 2 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 50.000 рублей', reply_markup=markup_inline)

    elif text == '💬 Тариф Standart':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Standart\n \n👍🏻 Хороший выбор, если небольшое количество уникальных пользователей и/или от 2 до 4 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 70.000 рублей', reply_markup=markup_inline)

    elif text == '💬 Тариф Gold':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Gold\n \n👍🏻 Хороший выбор, если среднее количество уникальных пользователей и/или от 4 до 8 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 85.000 рублей', reply_markup=markup_inline)

    elif text == '💬 Тариф Brilliant':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Brilliant\n \n👍🏻 Хороший выбор, если большое количество уникальных пользователей и/или от 8 до 12 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 100.000 рублей', reply_markup=markup_inline)

    elif text == '🗣️ Поддержка голосового бота':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('🗣️ Тариф Bronze')
        btn2 = types.KeyboardButton('🗣️ Тариф Standart')
        btn3 = types.KeyboardButton('🗣️ Тариф Gold')
        btn4 = types.KeyboardButton('🗣️ Тариф Brilliant')
        btn5 = types.KeyboardButton('🤝 Консультация')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, 'Тарифы отличаются, в зависимости от количества минут, а также степени необходимой поддержки')
        sender(user, 'Наша команда поможет индивидуально подобрать тариф во время консультации', reply_markup=markup)
        sender(user, '⬇ Выберите тариф', reply_markup=markup_inline)

    elif text == '🗣️ Тариф Bronze':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Bronze\n \n👍🏻 Хороший выбор, если маленькое количество минут и/или от 1 до 2 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 65.000 рублей', reply_markup=markup_inline)

    elif text == '🗣️ Тариф Standart':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Standart\n \n👍🏻 Хороший выбор, если небольшое количество минут и/или от 2 до 4 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 85.000 рублей', reply_markup=markup_inline)

    elif text == '🗣️ Тариф Gold':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Gold\n \n👍🏻 Хороший выбор, если среднее количество минут и/или от 4 до 8 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 95.000 рублей', reply_markup=markup_inline)

    elif text == '🗣️ Тариф Brilliant':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Brilliant\n \n👍🏻 Хороший выбор, если большое количество минут и/или от 8 до 12 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 110.000 рублей', reply_markup=markup_inline)

    elif text == '✌️ Параллельная поддержка':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('✌️ Тариф Bronze')
        btn2 = types.KeyboardButton('✌️ Тариф Standart')
        btn3 = types.KeyboardButton('✌️ Тариф Gold')
        btn4 = types.KeyboardButton('✌️ Тариф Brilliant')
        btn5 = types.KeyboardButton('🤝 Консультация')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, 'Тарифы отличаются, в зависимости от оптимального для двух ботов количества минут и уникальных пользователей, а также степени необходимой поддержки')
        sender(user, 'Наша команда поможет индивидуально подобрать тариф во время консультации', reply_markup=markup)
        sender(user, '⬇ Выберите тариф', reply_markup=markup_inline)

    elif text == '✌️ Тариф Bronze':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Bronze\n \n👍🏻 Хороший выбор, если маленькое количество минут и уникальных пользователей и/или от 1 до 2 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 100.000 рублей', reply_markup=markup_inline)

    elif text == '✌️ Тариф Standart':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Standart\n \n👍🏻 Хороший выбор, если небольшое количество минут и уникальных пользователей и/или от 2 до 4 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 150.000 рублей', reply_markup=markup_inline)

    elif text == '✌️ Тариф Gold':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Gold\n \n👍🏻 Хороший выбор, если среднее количество минут и уникальных пользователей и/или от 4 до 8 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 170.000 рублей', reply_markup=markup_inline)

    elif text == '✌️ Тариф Brilliant':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ В начало', callback_data='about_price')
        markup_inline.add(btn00)
        sender(user, '🔎 Тариф Brilliant\n \n👍🏻 Хороший выбор, если большое количество минут и уникальных пользователей и/или от 8 до 12 веток сценария.', reply_markup=markup)
        sender(user, '🔎 Стоимость 190.000 рублей', reply_markup=markup_inline)

    elif text == '❓ Частые вопросы':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💡 Технология ботов')
        btn2 = types.KeyboardButton('🤔 Зачем нужны боты')
        btn3 = types.KeyboardButton('💼 Интеграция бота')
        btn4 = types.KeyboardButton('⌛ Срок разработки')
        btn5 = types.KeyboardButton('Другой вопрос')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        sender(user, '📔 Мы собрали в этом разделе несколько частых вопросов по поводу внедрения ботов')
        sender(user, '⬇ Выберите подраздел', reply_markup=markup)

    elif text == '💡 Технология ботов':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💡 Как работают чат-боты')
        btn2 = types.KeyboardButton('🤔 Как работают голосовые боты')
        markup.add(btn1, btn2)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Другие вопросы', callback_data='about_faq')
        markup_inline.add(btn00)
        sender(user, 'Боты - это полезные программы-помощники. Могут быть чат-ботами или голосовыми ботами.', reply_markup=markup)
        sender(user, '⬇ Выберите о каких ботах мне рассказать подробнее', reply_markup=markup_inline)

    elif text == '💡 Как работают чат-боты':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💡 Узнать больше о технологиях чат-ботов')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Другие вопросы', callback_data='about_faq')
        markup_inline.add(btn00)
        sender(user, '🔹 Чат-боты бывают кнопочные (как я), которые распознают команды по кнопкам, и разговорные, которые общаются с помощью слов')
        sender(user, '🔹 В разговорных ботах используются технологии искусственного интеллекта и обработки естественного языка для имитации разговоров, похожих на привычные разговоры между людьми')
        sender(user, '🔹 Ботов можно запрограммировать таким образом, чтобы они отвечали на часто задаваемые вопросы, предоставляли индивидуальные рекомендации и выполняли другие рутинные задачи, помогая сотрудникам', reply_markup=markup)
        sender(user, '💡 Хотите я расскажу больше о технологии, лежащей в основе чат-ботов?', reply_markup=markup_inline)

    elif text == '💡 Узнать больше о технологиях чат-ботов':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('👩‍💼 Связаться с менеджером')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Другие вопросы', callback_data='about_faq')
        markup_inline.add(btn00)
        sender(user, '😊 Обожаю про это рассказывать!')
        sender(user, '🔹 Наши чат-боты используют комбинацию алгоритмов машинного обучения и систем, основанных на правилах, чтобы корректно понимать запросы клиентов и отвечать на них. \n🔹 Кроме того, боты интегрируются с внешними системами для предоставления информации в режиме реального времени и персонализированных рекомендаций')
        sender(user, '🔹 Процесс разработки нашего чат-бота включает в себя несколько этапов, а именно: \n1️⃣ консультация для определения запроса \n2️⃣ разработка \n3️⃣ тестирование нового робота-сотрудника \n4️⃣ постоянная поддержка')
        sender(user, 'Наша команда экспертов будет работать в постоянном контакте с вами над разработкой бота, отвечающего индивидуальным целям и требованиям', reply_markup=markup)
        sender(user, '👩‍💼 Хотите я свяжу вас с консультантом и он расскажет подробнее?', reply_markup=markup_inline)

    elif text == '🤔 Как работают голосовые боты':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💡 Узнать больше о технологиях голосовых ботов')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Другие вопросы', callback_data='about_faq')
        markup_inline.add(btn00)
        sender(user, '🔹 Голосовые боты используют технологию обработки естественного языка и распознавания речи для имитации разговоров, похожих на разговоры между людьми. \n🔹 Они распознают речь с помощью ASR и синтезируют в свою очередь речевой ответ с помощью записанного голоса диктора или технологии TTS. \n🔹 Голосовых ботов можно использовать для самых разных целей, включая обслуживание клиентов, в качестве личных помощников и даже просто для развлечения.')
        sender(user, '🔹 Голосовых ботов можно использовать для самых разных целей, включая обслуживание клиентов, в качестве личных помощников и даже просто для развлечения', reply_markup=markup)
        sender(user, '💡 Хотели бы вы узнать больше о технологии, лежащей в основе голосовых ботов?', reply_markup=markup_inline)

    elif text == '💡 Узнать больше о технологиях голосовых ботов':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('👩‍💼 Связаться с менеджером')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Другие вопросы', callback_data='about_faq')
        markup_inline.add(btn00)
        sender(user, '😊 Такая интересная тема!')
        sender(user, '🔹 Наши голосовые боты используют комбинацию алгоритмов глубокого обучения и нейронных сетей, чтобы корректно понимать запросы клиентов и отвечать на них. \n🔹 Кроме того, боты интегрируются с внешними системами для предоставления информации в режиме реального времени и персонализированных рекомендаций')
        sender(user, '🔹 Процесс разработки нашего чат-бота включает в себя несколько этапов, а именно: \n1️⃣ консультация для определения запроса \n2️⃣ разработка \n3️⃣ тестирование нового робота-сотрудника \n4️⃣ постоянная поддержка')
        sender(user, 'Наша команда экспертов будет работать в постоянном контакте с вами над разработкой бота, отвечающего индивидуальным целям и требованиям', reply_markup=markup)
        sender(user, '👩‍💼 Хотите я свяжу вас с консультантом и он расскажет подробнее?', reply_markup=markup_inline)

    elif text == '🤔 Зачем нужны боты':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('👩‍💼 Связаться с менеджером')
        markup.row(btn1)
        markup.row(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Другие вопросы', callback_data='about_faq')
        markup_inline.add(btn00)
        sender(user, '✌️ Боты могут снять нагрузку с сотрудников и автоматизировать рутинные задачи')
        sender(user, '➕ Использование ботов имеет много преимуществ. Они могут помочь снизить затраты на обслуживание клиентов, сократить время отклика, предоставить персонализированные рекомендации и даже повысить вовлеченность и удовлетворенность клиентов. И все это в формате 24/7.', reply_markup=markup)
        sender(user, '👩‍💼 Хотите я свяжу вас с консультантом и он расскажет подробнее о преимуществах использования чат-ботов и голосовых ботов?', reply_markup=markup_inline)

    elif text == '💼 Интеграция бота':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('👩‍💼 Связаться с менеджером')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Другие вопросы', callback_data='about_faq')
        markup_inline.add(btn00)
        sender(user, 'Все будет отлично - 💯, так как у нашей команды богатый опыт интеграций со многими сложными системами, что в итоге делает работу с ботами еще удобнее')
        sender(user, '🔹 Наши боты могут быть максимально интегрированы с уже существующими системами, включая CRM-систему, телефонию, платформу электронной коммерции и многое другое. \n🔹 Это позволяет осуществлять обмен информацией в режиме реального времени и получать персонализированные рекомендации для ваших клиентов.', reply_markup=markup)
        sender(user, '👩‍💼 Хотели бы вы получить более подробную информацию от менеджера о наших возможностях интеграции?', reply_markup=markup_inline)

    elif text == '⌛ Срок разработки':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('👩‍💼 Связаться с менеджером')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Другие вопросы', callback_data='about_faq')
        markup_inline.add(btn00)
        sender(user, '🔹 Время разработки ботов зависит от сложности бота и функций, которые он выполняет. \n🔹 Как правило, разработка полнофункционального бота может занимать от нескольких недель до нескольких месяцев', reply_markup=markup)
        sender(user, '👩‍💼 Хотите, чтобы я связал с консультантом, который даст больше информации о сроках нашей разработки под ваш конкретный запрос?', reply_markup=markup_inline)

    elif text == 'Другой вопрос':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('👩‍💼 Связаться с менеджером')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ К списку вопросов', callback_data='about_faq')
        markup_inline.add(btn00)
        sender(user, '🤔 Да, тема роботов - очень интересная и обширная. И конечно многое хочется узнать', reply_markup=markup)
        sender(user, '👍 Давайте я переведу Вас на менеджера и он подробно ответит на любые вопросы', reply_markup=markup_inline)

    elif text == '🤝 Консультация':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton("📔 Заполнить форму")
        btn2 = types.KeyboardButton('👩‍💼 Связаться с менеджером')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, '👩‍💼 Наш сотрудник будет рад подсказать по всем вопросам')
        sender(user, '📔 Я же могу отправить небольшую форму, чтобы было удобно описать свой индивидуальный запрос по роботу')
        sender(user, '⬇ Выберите подраздел', reply_markup=markup)

    elif text == '📔 Заполнить форму':
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Назад', callback_data='about_booking')
        markup_inline.add(btn00)
        sender(user, 'Заполнить форму обратной связи можно [здесь](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat) 👈', parse_mode='Markdown')
        sender(user, '☝️ В этой форме можно рассказать подробнее о своем запросе', reply_markup=markup)
        sender(user, '💼 Тогда к первой встрече наши менеджеры уже подготовят индивидуальные решения под вашу задачу', reply_markup=markup_inline)
    elif text == '🇬🇧 English':
        btn1 = types.KeyboardButton("💡 About us")
        btn2 = types.KeyboardButton('🤖 About bots')
        btn3 = types.KeyboardButton('💰 Price')
        btn4 = types.KeyboardButton('❓ FAQ')
        btn5 = types.KeyboardButton('🤝 Contact us')
        btn6 = types.KeyboardButton('👀 Fun facts')
        btn7 = types.KeyboardButton('🔙 Back to language selection')
        markup.row(btn1, btn2, btn3)
        markup.row(btn4, btn5)
        markup.row(btn6)
        markup.row(btn7)
        sender(user, "👋 We are Kittens. \n\nWe build conversational bots to help other companies automate their business processes 📈")
        sender(user, '🧐 Choose the option below', reply_markup=markup)

    elif text == '🔙 Back to language selection':
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        markup.row(btn1, btn2)
        sender(user, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    elif text == '👀 Fun facts':
        sender(user, random.choice(robot_facts_eng))

    elif text == '💡 About us':
        btn1 = types.KeyboardButton('🩵 Our company')
        btn2 = types.KeyboardButton('💼 Our work')
        btn01 = types.KeyboardButton('🔙 Main menu')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, "▫️ Our company Kittens helps to implement modern technology in other companies and improve the processing of both internal and external tasks with the help of conversational bots")
        sender(user, "▫️ Bot assistants are built for a variety of purposes and bring joy to their employers as well as to their customers every day 🥳")
        sender(user, '⬇ Choose the option below', reply_markup=markup)

    elif text == '🩵 Our company':
        btn00 = types.InlineKeyboardButton('⬅️ Back', callback_data='about_us_eng')
        markup_inline.add(btn00)
        btn01 = types.KeyboardButton('🔙 Main menu')
        markup.row(btn01)
        sender(user, '🔐 We are a Russian systems integrator, working on the market of communications, telecommunication and IT-solutions and engineering infrastructure since 2001', reply_markup=markup)
        sender(user, '📌 More information about our company on [our website](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat)', reply_markup=markup_inline, parse_mode='Markdown')

    elif text == '💼 Our work':
        btn1 = types.InlineKeyboardButton('⬅️ Back', callback_data='about_us_eng')
        markup_inline.add(btn1)
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn2 = types.KeyboardButton('🔧 How to build a bot')
        markup.row(btn2, btn01)
        sender(user, "️▫️ We offer services for the creation of conversational robots")
        sender(user, "️▫️ You can only have an idea, without understanding what and how you can automate in business, which we will bring to the final successful operation👌 \n▫️  Our team will take care of all the worries of writing a script, configuring and integrating with your systems, carefully listening to all individual wishes")
        sender(user, "️▫️ You will only have to be happy with less workload and a new employee 😎🤖", reply_markup=markup)
        sender(user, '🔎 Do you want to learn how to build a bot?', reply_markup=markup_inline)

    elif text == '🔧 How to build a bot':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💻 Our solutions')
        btn2 = types.KeyboardButton('🤝 Contact us')
        btn3 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_us_eng')
        markup_inline.add(btn3)
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, "🔵 Our steps to build a robot include")
        sender(user, "1️⃣ Filling out a brief for initial acquaintance with the company \n2️⃣ Meeting with our team, where we will give detailed answers to the technical and organizational part of creating a robot \n3️⃣ Developing a robot \n4️⃣ Testing the work before the final launch \n5️⃣ Continuous support for the work of a ready-made assistant")
        sender(user, "🔸 Also, we offer to help with the training of your team to ensure the most pleasant and easy integration with already used systems", reply_markup=markup)
        sender(user, '🔎 Would you like to see examples of solutions or contact our consultant?', reply_markup=markup_inline)

    elif text == '💻 Our solutions':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_us_eng')
        markup_inline.add(btn1)
        markup.add(btn01)
        sender(user, "️🔶 We have extensive experience in creating a variety of conversational solutions, from traditional bots to unusual projects for individual requests", reply_markup=markup)
        sender(user, '📌 More information about our solutions on [our website](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat)', reply_markup=markup_inline, parse_mode='Markdown')

    elif text == '🔙 Main menu':
        btn1 = types.KeyboardButton("💡 About us")
        btn2 = types.KeyboardButton('🤖 About bots')
        btn3 = types.KeyboardButton('💰 Price')
        btn4 = types.KeyboardButton('❓ FAQ')
        btn5 = types.KeyboardButton('🤝 Contact us')
        btn6 = types.KeyboardButton('👀 Fun facts')
        btn7 = types.KeyboardButton('🔙 Back to language selection')
        markup.row(btn1, btn2, btn3)
        markup.row(btn4, btn5)
        markup.row(btn6)
        markup.row(btn7)
        sender(user, '🧐 Choose the option below', reply_markup=markup)

    elif text == '🤖 About bots':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💬 About chatbots')
        btn2 = types.KeyboardButton('🗣️ About voicebots')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, '⬇ What kind of robots do you want to learn about?', reply_markup=markup)

    elif text == '💬 About chatbots':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('📌 Chatbot example')
        markup.row(btn1)
        markup.row(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back', callback_data='about_bots_eng')
        markup_inline.add(btn00)
        sender(user, '✍️ Great! Our chatbots are great assistants who can perform the task of handling requests from users in text channels and make a simple and convenient service for users', reply_markup=markup)
        sender(user, '🧐 Would you like to see our example of a chatbot?', reply_markup=markup_inline)

    elif text == '📌 Chatbot example':
        btn01 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the types of robots', callback_data='about_bots_eng')
        markup_inline.add(btn00)
        sender(user, '⚪ In addition to a button bot option like me, we can make a bot with speech recognition and communication with users.')
        sender(user, '✈️ One of our bots is for Kittens company. You can go and try it out on your own 👇')
        sender(user, '@BotFather', reply_markup=markup)
        sender(user, '📹 Example in the [video](https://www.youtube.com/watch?v=BNSp_DFr5f0) 👈', reply_markup=markup_inline, parse_mode='Markdown')

    elif text == '🗣️ About voicebots':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('📌 Voicebot example')
        markup.row(btn1)
        markup.row(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back', callback_data='about_bots_eng')
        markup_inline.add(btn00)
        sender(user, '🔉 Great! Our voice bots are great assistants that can handle outgoing and incoming calls and reduce operator workload', reply_markup=markup)
        sender(user, '🧐 Would you like to see our example of a voicebot?', reply_markup=markup_inline)

    elif text == '📌 Voicebot example':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('🚛 Logistics')
        btn2 = types.KeyboardButton('🚑 Medicine')
        btn3 = types.KeyboardButton('🏦 Finance')
        markup.row(btn1, btn2, btn3)
        markup.row(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back', callback_data='about_bots_eng')
        markup_inline.add(btn00)
        sender(user, '📌 More information about other solutions on [our website](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat)', reply_markup=markup, parse_mode='Markdown')
        sender(user, '⬇ Choose one of the business areas below', reply_markup=markup_inline)

    elif text == '🚛 Logistics':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn00 = types.InlineKeyboardButton('⬅️ Back to the other areas', callback_data='about_voice_bots_eng')
        markup_inline.add(btn00)
        markup.add(btn01)
        sender(user, '🔹 Great! We offer many solutions for this area, such as robot assistance in hiring drivers, checking trucking weights and distances, and reminding you of order storage times', reply_markup=markup)
        sender(user, '👉[Here](https://www.youtube.com/watch?v=BNSp_DFr5f0) you can see one of our voicebot examples in this area', reply_markup=markup_inline,  parse_mode='Markdown')

    elif text == '🚑 Medicine':
        btn01 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the other areas', callback_data='about_voice_bots_eng')
        markup_inline.add(btn00)
        sender(user, '🔹 Great! We offer a variety of solutions for this area, for example, calling to confirm a visit to a doctor, informing about the time of the appointment and other options', reply_markup=markup)
        sender(user, '👉[Here](https://www.youtube.com/watch?v=BNSp_DFr5f0) you can see one of our voicebot examples in this area', reply_markup=markup_inline,  parse_mode='Markdown')

    elif text == '🏦 Finance':
        btn01 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the other areas', callback_data='about_voice_bots_eng')
        markup_inline.add(btn00)
        sender(user, '🔹 Great! We offer many solutions for this area, such as call for lead generation with ready-made scripts on financial topics, voice commands for mobile applications and other options', reply_markup=markup)
        sender(user, '👉[Here](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat) you can see one of our voicebot examples in this area', reply_markup=markup_inline,  parse_mode='Markdown')

    elif text == '💰 Price':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('🔎 Development price')
        btn2 = types.KeyboardButton('🔎 Support price')
        btn3 = types.KeyboardButton('🤝 Contact us')
        markup.row(btn1, btn2)
        markup.row(btn3, btn01)
        sender(user, '▫️ Each robot is evaluated individually, depending on the number of automated scenarios, their complexity, as well as the necessary integrations with external systems')
        sender(user, '🔵 The cost of the bot includes: \n\n1️⃣ One-time rate for the development and configuration of the robot \n2️⃣ Regular rate for the support of the robot')
        sender(user, '▫️ In order to accurately calculate the cost of a bot for your specific tasks, it is necessary to consult and clarify the details. However, to help you navigate the cost, we suggest that you familiarize yourself with the average tariffs')
        sender(user, '⬇ Choose the type of service', reply_markup=markup)

    elif text == '🔎 Development price':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💬 Chatbot development')
        btn2 = types.KeyboardButton('🗣️ Voicebot development')
        btn3 = types.KeyboardButton('✌️ Parallel development')
        btn4 = types.KeyboardButton('🤝 Contact us')
        markup.row(btn1, btn2)
        markup.row(btn3)
        markup.row(btn4, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Other prices', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, 'The rates differ depending on the type of robot. In addition, parallel development is possible: a chatbot is created and its script is adapted to the voice bot', reply_markup=markup)
        sender(user, '⬇ Choose the type of robots', reply_markup=markup_inline)

    elif text == '💬 Chatbot development':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💬 Rate XS')
        btn2 = types.KeyboardButton('💬 Rate S')
        btn3 = types.KeyboardButton('💬 Rate M')
        btn4 = types.KeyboardButton('💬 Rate L')
        btn5 = types.KeyboardButton('🤝 Contact us')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, 'The rates differ depending on the number of unique users and branches of the scenario')
        sender(user, 'Our team will help you individually choose the tariff during the consultation', reply_markup=markup)
        sender(user, '⬇ Choose your option below', reply_markup=markup_inline)

    elif text == '💬 Rate XS':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        markup_inline = types.InlineKeyboardMarkup()
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate XS\n \n👍🏻 A good choice if there is a small number of unique users and/or from 1 to 2 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽50.000', reply_markup=markup_inline)

    elif text == '💬 Rate S':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        markup_inline = types.InlineKeyboardMarkup()
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate S\n \n👍🏻 A good choice if there are a small number of unique users and/or 2 to 4 script branches.', reply_markup=markup)
        sender(user, '🔎 Price: ₽100.000', reply_markup=markup_inline)

    elif text == '💬 Rate M':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate M\n \n👍🏻 A good choice if the average number of unique users and/or from 4 to 8 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽150.000', reply_markup=markup_inline)

    elif text == '💬 Rate L':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate L\n \n👍🏻 A good choice if there are a large number of unique users and/or 8 to 12 script branches', reply_markup=markup)
        sender(user, '🔎 Price: ₽250.000', reply_markup=markup_inline)

    elif text == '🗣️ Voicebot development':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('🗣️ Rate XS')
        btn2 = types.KeyboardButton('🗣️ Rate S')
        btn3 = types.KeyboardButton('🗣️ Rate M')
        btn4 = types.KeyboardButton('🗣️ Rate L')
        btn5 = types.KeyboardButton('🤝 Contact us')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, 'The rates differ depending on the number of minutes and branches of the scenario')
        sender(user, 'Our team will help you individually choose the tariff during the consultation', reply_markup=markup)
        sender(user, '⬇ Choose your option below', reply_markup=markup_inline)

    elif text == '🗣️ Rate XS':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate XS\n \n👍🏻 A good choice if there is a small number of minutes and/or from 1 to 2 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽65.000', reply_markup=markup_inline)

    elif text == '🗣️ Rate S':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate S\n \n👍🏻 A good choice if a small number of minutes and/or 2 to 4 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽115.000', reply_markup=markup_inline)

    elif text == '🗣️ Rate M':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate M\n \n👍🏻 A good choice if the average number of minutes and/or 4 to 8 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽165.000', reply_markup=markup_inline)

    elif text == '🗣️ Rate L':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate L\n \n👍🏻 A good choice if there are a large number of minutes and/or 8 to 12 script branches', reply_markup=markup)
        sender(user, '🔎 Price: ₽265.000', reply_markup=markup_inline)

    elif text == '✌️ Parallel development':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('✌️ Rate XS')
        btn2 = types.KeyboardButton('✌️ Rate S')
        btn3 = types.KeyboardButton('✌️ Rate M')
        btn4 = types.KeyboardButton('✌️ Rate L')
        btn5 = types.KeyboardButton('🤝 Contact us')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, 'The rates differ depending on the optimal number of minutes for two bots, unique users and script branches')
        sender(user, 'Our team will help you individually choose the tariff during the consultation', reply_markup=markup)
        sender(user, '⬇ Choose your option below', reply_markup=markup_inline)

    elif text == '✌️ Rate XS':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate XS\n \n👍🏻 A good choice if there are a small number of minutes and unique users and/or from 1 to 2 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽100.000', reply_markup=markup_inline)

    elif text == '✌️ Rate S':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate S\n \n👍🏻 A good choice if there are a small number of minutes and unique users and/or 2 to 4 script branches', reply_markup=markup)
        sender(user, '🔎 Price: ₽200.000', reply_markup=markup_inline)

    elif text == '✌️ Rate M':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate M\n \n👍🏻 A good choice if the average number of minutes and unique users and/or 4 to 8 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽300.000', reply_markup=markup_inline)

    elif text == '✌️ Rate L':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate L\n \n👍🏻 A good choice if there are a large number of minutes and unique users and/or 8 to 12 script branches', reply_markup=markup)
        sender(user, '🔎 Price: ₽500.000', reply_markup=markup_inline)

    elif text == '🔎 Support price':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💬 Chatbot support')
        btn2 = types.KeyboardButton('🗣️ Voicebot support')
        btn3 = types.KeyboardButton('✌️ Parallel support')
        btn4 = types.KeyboardButton('🤝 Contact us')
        markup.row(btn1, btn2)
        markup.row(btn3)
        markup.row(btn4, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, 'The rates differ depending on the type of robot. In addition, parallel support is performed when a voice bot and a chat bot are in operation at the same time', reply_markup=markup)
        sender(user, '⬇ Choose your option below', reply_markup=markup_inline)

    elif text == '💬 Chatbot support':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💬 Rate Bronze')
        btn2 = types.KeyboardButton('💬 Rate Standart')
        btn3 = types.KeyboardButton('💬 Rate Gold')
        btn4 = types.KeyboardButton('💬 Rate Brilliant')
        btn5 = types.KeyboardButton('🤝 Contact us')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, 'The rates differ depending on the number of unique users, as well as the degree of necessary support')
        sender(user, 'Our team will help you individually choose the tariff during the consultation', reply_markup=markup)
        sender(user, '⬇ Choose your option below', reply_markup=markup_inline)

    elif text == '💬 Rate Bronze':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Bronze\n \n👍🏻 A good choice if there is a small number of unique users and/or from 1 to 2 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽50.000', reply_markup=markup_inline)

    elif text == '💬 Rate Standart':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Standart\n \n👍🏻 A good choice if there are a small number of unique users and/or 2 to 4 script branches', reply_markup=markup)
        sender(user, '🔎 Price: ₽70.000', reply_markup=markup_inline)

    elif text == '💬 Rate Gold':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Gold\n \n👍🏻 A good choice if the average number of unique users and/or from 4 to 8 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽85.000', reply_markup=markup_inline)

    elif text == '💬 Rate Brilliant':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Brilliant\n \n👍🏻 A good choice if there are a large number of unique users and/or 8 to 12 script branches', reply_markup=markup)
        sender(user, '🔎 Price: ₽100.000', reply_markup=markup_inline)

    elif text == '🗣️ Voicebot support':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('🗣️ Rate Bronze')
        btn2 = types.KeyboardButton('🗣️ Rate Standart')
        btn3 = types.KeyboardButton('🗣️ Rate Gold')
        btn4 = types.KeyboardButton('🗣️ Rate Brilliant')
        btn5 = types.KeyboardButton('🤝 Contact us')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, 'The rates differ depending on the number of minutes, as well as the degree of necessary support')
        sender(user, 'Our team will help you individually choose the tariff during the consultation', reply_markup=markup)
        sender(user, '⬇ Choose your option below', reply_markup=markup_inline)

    elif text == '🗣️ Rate Bronze':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Bronze\n \n👍🏻 A good choice if there is a small number of minutes and/or from 1 to 2 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽65.000', reply_markup=markup_inline)

    elif text == '🗣️ Rate Standart':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Standart\n \n👍🏻 A good choice if a small number of minutes and/or 2 to 4 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽85.000', reply_markup=markup_inline)

    elif text == '🗣️ Rate Gold':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Gold\n \n👍🏻 A good choice if the average number of minutes and/or 4 to 8 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽95.000', reply_markup=markup_inline)

    elif text == '🗣️ Rate Brilliant':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Brilliant\n \n👍🏻 A good choice if there are a large number of minutes and/or 8 to 12 script branches', reply_markup=markup)
        sender(user, '🔎 Price: ₽110.000', reply_markup=markup_inline)

    elif text == '✌️ Parallel support':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('✌️ Rate Bronze')
        btn2 = types.KeyboardButton('✌️ Rate Standart')
        btn3 = types.KeyboardButton('✌️ Rate Gold')
        btn4 = types.KeyboardButton('✌️ Rate Brilliant')
        btn5 = types.KeyboardButton('🤝 Contact us')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, 'The rates differ depending on the optimal number of minutes and unique users for two bots, as well as the degree of necessary support')
        sender(user, 'Our team will help you individually choose the tariff during the consultation', reply_markup=markup)
        sender(user, '⬇ Choose your option below', reply_markup=markup_inline)

    elif text == '✌️ Rate Bronze':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Bronze\n \n👍🏻 A good choice if there are a small number of minutes and unique users and/or from 1 to 2 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽100.000', reply_markup=markup_inline)

    elif text == '✌️ Rate Standart':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Standart\n \n👍🏻 A good choice if there are a small number of minutes and unique users and/or 2 to 4 script branches', reply_markup=markup)
        sender(user, '🔎 Price: ₽150.000', reply_markup=markup_inline)

    elif text == '✌️ Rate Gold':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Gold\n \n👍🏻 A good choice if the average number of minutes and unique users and/or 4 to 8 branches of the script', reply_markup=markup)
        sender(user, '🔎 Price: ₽170.000', reply_markup=markup_inline)

    elif text == '✌️ Rate Brilliant':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back to the beginning', callback_data='about_price_eng')
        markup_inline.add(btn00)
        sender(user, '🔎 Rate Brilliant\n \n👍🏻 A good choice if there are a large number of minutes and unique users and/or 8 to 12 script branches', reply_markup=markup)
        sender(user, '🔎 Price: ₽190.000', reply_markup=markup_inline)

    elif text == '❓ FAQ':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💡 Bot technology')
        btn2 = types.KeyboardButton('🤔 Why do we need bots')
        btn3 = types.KeyboardButton('💼 Bot integration')
        btn4 = types.KeyboardButton('⌛ Terms of development')
        btn5 = types.KeyboardButton('Different question')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        sender(user, '📔 We have collected in this section a few frequent questions about the introduction of bots')
        sender(user, '⬇ Choose the option below', reply_markup=markup)

    elif text == '💡 Bot technology':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💡 How chatbots work')
        btn2 = types.KeyboardButton('🤔 How voicebots work')
        markup.add(btn1, btn2)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Other questions', callback_data='about_faq_eng')
        markup_inline.add(btn00)
        sender(user, 'Bots are useful helper programs. They can be chatbots or voice bots.', reply_markup=markup)
        sender(user, '⬇ Choose which bots to tell you more about', reply_markup=markup_inline)

    elif text == '💡 How chatbots work':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💡 Learn more about chatbot technologies')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Other questions', callback_data='about_faq_eng')
        markup_inline.add(btn00)
        sender(user, '🔹 Chatbots can be push-button (like me), which recognize commands by buttons, and conversational, which communicate using words')
        sender(user, '🔹 Conversational bots use artificial intelligence and natural language processing technologies to simulate conversations similar to the usual conversations between people')
        sender(user, '🔹 Bots can be programmed in such a way that they answer frequently asked questions, provide individual recommendations and perform other routine tasks, helping employees', reply_markup=markup)
        sender(user, '💡 Do you want me to tell you more about the technology underlying chatbots?', reply_markup=markup_inline)

    elif text == '💡 Learn more about chatbot technologies':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('👩‍💼 Book a meeting')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Other questions', callback_data='about_faq_eng')
        markup_inline.add(btn00)
        sender(user, '😊 I love talking about it!')
        sender(user, '🔹 Our chatbots use a combination of machine learning algorithms and rule-based systems to correctly understand customer requests and respond to them. \n🔹 In addition, bots integrate with external systems to provide real-time information and personalized recommendations')
        sender(user, '🔹 The development process of our chatbot includes several stages, namely: \n1️⃣ consultation to determine the request \n2️⃣ development \n3️⃣ testing a new robot-employee \n4️⃣ constant support')
        sender(user, 'Our team of experts will work in constant contact with you to develop a bot that meets individual goals and requirements', reply_markup=markup)
        sender(user, '👩‍💼 Do you want me to contact you with a consultant and he will tell you more?', reply_markup=markup_inline)

    elif text == '🤔 How voicebots work':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💡 Learn more about voicebot technologies')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Other questions', callback_data='about_faq_eng')
        markup_inline.add(btn00)
        sender(user, "🔹 Voice bots use natural language processing and speech recognition technology to simulate conversations similar to conversations between people. \n🔹 They recognize speech using ASR and synthesize in turn a speech response using a recorded speaker's voice or TTS technology. \n🔹 Voice bots can be used for a variety of purposes, including customer service, as personal assistants, and even just for fun.")
        sender(user, '🔹 Voice bots can be used for a variety of purposes, including customer service, as personal assistants, and even just for fun', reply_markup=markup)
        sender(user, '💡 Would you like to learn more about the technology behind voice bots?', reply_markup=markup_inline)

    elif text == '💡 Learn more about voicebot technologies':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('👩‍💼 Book a meeting')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Other questions', callback_data='about_faq_eng')
        markup_inline.add(btn00)
        sender(user, '😊 Such an interesting topic!')
        sender(user, '🔹 Our voice bots use a combination of deep learning algorithms and neural networks to correctly understand customer requests and respond to them. \n🔹 In addition, bots integrate with external systems to provide real-time information and personalized recommendations')
        sender(user, '🔹 The development process of our chatbot includes several stages, namely: \n1️⃣ consultation to determine the request \n2️⃣ development \n3️⃣ testing a new robot-employee \n4️⃣ constant support')
        sender(user, 'Our team of experts will work in constant contact with you to develop a bot that meets individual goals and requirements', reply_markup=markup)
        sender(user, '👩‍💼 Do you want me to contact you with a consultant and he will tell you more?', reply_markup=markup_inline)

    elif text == '🤔 Why do we need bots':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('👩‍💼 Book a meeting')
        markup.row(btn1)
        markup.row(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Other questions', callback_data='about_faq_eng')
        markup_inline.add(btn00)
        sender(user, '✌️ Bots can take the load off employees and automate routine tasks')
        sender(user, '➕ Using bots has many advantages. They can help reduce customer service costs, reduce response time, provide personalized recommendations, and even increase customer engagement and satisfaction. And all this in a 24/7 format', reply_markup=markup)
        sender(user, '👩‍💼 Would you like me to contact you with a consultant and he will tell you more about the benefits of using chatbots and voice bots?', reply_markup=markup_inline)

    elif text == '💼 Bot integration':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('👩‍💼 Book a meeting')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Other questions', callback_data='about_faq_eng')
        markup_inline.add(btn00)
        sender(user, 'Everything will be fine - 💯, Since our team has a rich experience of integration with many complex systems, which ultimately makes working with bots even more convenient')
        sender(user, '🔹 Our bots can be maximally integrated with existing systems, including CRM system, telephony, e-commerce platform and much more. \n🔹 This allows you to exchange information in real time and receive personalized recommendations for your customers.', reply_markup=markup)
        sender(user, '👩‍💼 Would you like to get more detailed information from the manager about our integration capabilities?', reply_markup=markup_inline)

    elif text == '⌛ Terms of development':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('👩‍💼 Book a meeting')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Other questions', callback_data='about_faq_eng')
        markup_inline.add(btn00)
        sender(user, '🔹 The development time of bots depends on the complexity of the bot and the functions it performs. \n🔹 As a rule, the development of a fully functional bot can take from several weeks to several months', reply_markup=markup)
        sender(user, '👩‍💼 Do you want to get in touch with a consultant who will give more information about the timing of our development for your specific request?', reply_markup=markup_inline)

    elif text == 'Different question':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('👩‍💼 Book a meeting')
        markup.add(btn1)
        markup.add(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back to question selection', callback_data='about_faq_eng')
        markup_inline.add(btn00)
        sender(user, '🤔 Yes, the topic of robots is very interesting and extensive. And of course you want to know a lot', reply_markup=markup)
        sender(user, '👍 Let me transfer you to the manager and he will answer any questions in detail', reply_markup=markup_inline)

    elif text == '🤝 Contact us':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton("📔 Fill in a form")
        btn2 = types.KeyboardButton('👩‍💼 Book a meeting')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, '👩‍💼 Our manager will be glad to help you with any questions.')
        sender(user, '📔 I can also send a small form to make it convenient to describe my individual request for the robot')
        sender(user, '⬇ Choose the option below', reply_markup=markup)

    elif text == '📔 Fill in a form':
        btn1 = types.KeyboardButton('🔙 Main menu')
        markup.add(btn1)
        btn00 = types.InlineKeyboardButton('⬅️ Back', callback_data='about_booking_eng')
        markup_inline.add(btn00)
        sender(user, 'You may fill out the feedback form [here](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat) 👈', parse_mode='Markdown')
        sender(user, '☝️ In this form, you can tell us more about your request', reply_markup=markup)
        sender(user, '💼 Then, by the first meeting, our managers will have already prepared individual solutions for your task', reply_markup=markup_inline)
    else:
        output = language_detection_model.predict([message.text])
        predicted_language = output[0]
        if predicted_language == 'Russian':
            btn1 = types.KeyboardButton("💡 О нас")
            btn2 = types.KeyboardButton('🤖 О ботах')
            btn3 = types.KeyboardButton('💰 Cтоимость')
            btn4 = types.KeyboardButton('❓ Частые вопросы')
            btn5 = types.KeyboardButton('🤝 Консультация')
            btn6 = types.KeyboardButton('👀 А ты знаешь?')
            btn7 = types.KeyboardButton('🔙 Вернуться к выбору языка')
            markup.row(btn1, btn2, btn3)
            markup.row(btn4, btn5)
            markup.row(btn6)
            markup.row(btn7)
            sender(user, "👋 Будем общаться на русском языке. Дружеский совет - пожалуйста, пользуйтесь кнопочками ниже, чтобы я мог точно понимать, что от меня требуется 👀")
            sender(user, "🧐 Выберите интересующий раздел", reply_markup=markup)
        else:
            btn1 = types.KeyboardButton("🩵 About us")
            btn2 = types.KeyboardButton('🤖 About bots')
            btn3 = types.KeyboardButton('💰 Price')
            btn4 = types.KeyboardButton('❓ FAQ')
            btn5 = types.KeyboardButton('🤝 Book a meeting')
            btn6 = types.KeyboardButton('👀 Fun facts')
            btn7 = types.KeyboardButton('🔙 Back to language selection')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
            sender(user, "👋 Let's chat in English. Just a friendly reminder - please, make sure to use the buttons below to help me understand you better 👀")
            sender(user, "🧐 Choose the option below", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user = call.message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_inline = types.InlineKeyboardMarkup()
    sender = bot.send_message

    if call.data == 'about_us':
        btn1 = types.KeyboardButton('🩵 Кто мы')
        btn2 = types.KeyboardButton('💼 Что мы предлагаем')
        btn01 = types.KeyboardButton('🔙 Главное меню')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, "▫️ Наша компания Kittens помогает внедрять современные технологии в работу других компаний и улучшать процессы обработки как внутренних, так и внешних задач с помощью разговорных ботов")
        sender(user, "▫️ Боты-помощники разрабатываются под разнообразные цели и ежедневно радуют как своих работодателей, так и клиентов-собеседников 🥳")
        sender(user, '⬇ Выберите подраздел', reply_markup=markup)

    elif call.data == 'about_us_eng':
        btn1 = types.KeyboardButton('🩵 Our company')
        btn2 = types.KeyboardButton('💼 Our work')
        btn01 = types.KeyboardButton('🔙 Main menu')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, "▫️ Our company Kittens helps to implement modern technology in other companies and improve the processing of both internal and external tasks with the help of conversational bots")
        sender(user, "▫️ Bot assistants are developed for a variety of purposes and bring joy to their employers as well as to their customers every day 🥳")
        sender(user, '⬇ Choose the option below', reply_markup=markup)

    elif call.data == 'about_bots':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💬 О чат-ботах')
        btn2 = types.KeyboardButton('🗣️ О голосовых ботах')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, '⬇ О каких роботах хотите узнать?', reply_markup=markup)

    elif call.data == 'about_bots_eng':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💬 About chatbots')
        btn2 = types.KeyboardButton('🗣️ About voicebots')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, '⬇ What kind of robots do you want to learn about?', reply_markup=markup)

    elif call.data == 'about_voice_bots':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('🚛 Логистика')
        btn2 = types.KeyboardButton('🚑 Медицина')
        btn3 = types.KeyboardButton('🏦 Финансы')
        markup.row(btn1, btn2, btn3)
        markup.row(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Назад', callback_data='about_bots')
        markup_inline.add(btn00)
        sender(user, '📌 Подробнее узнать о других решениях можно [на нашем сайте](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat)', reply_markup=markup, parse_mode='Markdown')
        sender(user, '⬇ Выберите сферу бизнеса', reply_markup=markup_inline)

    elif call.data == 'about_voice_bots_eng':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('🚛 Logistics')
        btn2 = types.KeyboardButton('🚑 Medicine')
        btn3 = types.KeyboardButton('🏦 Finance')
        markup.row(btn1, btn2, btn3)
        markup.row(btn01)
        btn00 = types.InlineKeyboardButton('⬅️ Back', callback_data='about_bots_eng')
        markup_inline.add(btn00)
        sender(user, '📌 More information about other solutions on [our website](https://www.nationalgeographic.com/animals/mammals/facts/domestic-cat)', reply_markup=markup, parse_mode='Markdown')
        sender(user, '⬇ Choose one of the business areas below', reply_markup=markup_inline)

    elif call.data == 'about_price':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('🔎 Тарифы разработки')
        btn2 = types.KeyboardButton('🔎 Тарифы поддержки')
        btn3 = types.KeyboardButton('🤝 Консультация')
        markup.row(btn1, btn2)
        markup.row(btn3, btn01)
        sender(user, '▫️ Каждый робот оценивается индивидуально, в зависимости от количества автоматизируемых сценариев, их сложности, а также необходимых интеграций с внешними системами')
        sender(user, '🔵 Стоимость бота включает в себя: \n\n1️⃣ Единоразовый тариф для разработки и настройки робота \n2️⃣ Регулярный тариф по поддержке работы робота')
        sender(user, '▫️ Для того, чтобы точно посчитать стоимость бота для конкретно Ваших задач, необходимо провести консультацию и уточнить детали. \n▫️ Однако, чтобы помочь сориентироваться в стоимости, мы предлагаем ознакомиться со средними тарифами')
        sender(user, '⬇ Выберите тип услуги', reply_markup=markup)

    elif call.data == 'about_price_eng':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('🔎 Development price')
        btn2 = types.KeyboardButton('🔎 Support price')
        btn3 = types.KeyboardButton('🤝 Contact us')
        markup.row(btn1, btn2)
        markup.row(btn3, btn01)
        sender(user, '▫️ Each robot is evaluated individually, depending on the number of automated scenarios, their complexity, as well as the necessary integrations with external systems')
        sender(user, '🔵 The cost of the bot includes: \n\n1️⃣ One-time rate for the development and configuration of the robot \n2️⃣ Regular rate for the support of the robot')
        sender(user, '▫️ In order to accurately calculate the cost of a bot for your specific tasks, it is necessary to consult and clarify the details. However, to help you navigate the cost, we suggest that you familiarize yourself with the average tariffs')
        sender(user, '⬇ Choose the type of service', reply_markup=markup)

    elif call.data == 'about_faq':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton('💡 Технология ботов')
        btn2 = types.KeyboardButton('🤔 Зачем нужны боты')
        btn3 = types.KeyboardButton('💼 Интеграция бота')
        btn4 = types.KeyboardButton('⌛ Срок разработки')
        btn5 = types.KeyboardButton('Другой вопрос')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        sender(user, '📔 Мы собрали в этом разделе несколько частых вопросов по поводу внедрения ботов')
        sender(user, '⬇ Выберите подраздел', reply_markup=markup)

    elif call.data == 'about_faq_eng':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton('💡 Bot technology')
        btn2 = types.KeyboardButton('🤔 Why do we need bots')
        btn3 = types.KeyboardButton('💼 Bot integration')
        btn4 = types.KeyboardButton('⌛ Terms of development')
        btn5 = types.KeyboardButton('Different question')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn01)
        sender(user, '📔 We have collected in this section a few frequent questions about the introduction of bots')
        sender(user, '⬇ Choose the option below', reply_markup=markup)

    elif call.data == 'about_booking':
        btn01 = types.KeyboardButton('🔙 Главное меню')
        btn1 = types.KeyboardButton("📔 Заполнить форму")
        btn2 = types.KeyboardButton('👩‍💼 Связаться с менеджером')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, '👩‍💼 Наш сотрудник будет рад подсказать по всем вопросам')
        sender(user, '📔 Я же могу отправить небольшую форму, чтобы было удобно описать свой индивидуальный запрос по роботу')
        sender(user, '⬇ Выберите подраздел', reply_markup=markup)

    elif call.data == 'about_booking_eng':
        btn01 = types.KeyboardButton('🔙 Main menu')
        btn1 = types.KeyboardButton("📔 Fill in a form")
        btn2 = types.KeyboardButton('👩‍💼 Book a meeting')
        markup.row(btn1, btn2)
        markup.row(btn01)
        sender(user, '👩‍💼 Our manager will be glad to help you with any questions.')
        sender(user, '📔 I can also send a small form to make it convenient to describe my individual request for the robot')
        sender(user, '⬇ Choose the option below', reply_markup=markup)
bot.polling()