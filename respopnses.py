def get_response(message: str) -> str:
    p_message = message.lower()
################################hi/bye############################
    if p_message == 'hi':
        return '''Hey there! Ask anything about Bangladesh
NOTE:Don't use WH in your question.
ask question by keywords (like national flower,capital city,old name of dhaka etc)'''
    elif p_message == 'hello':
        return '''Hey there! Ask anything about Bangladesh
NOTE:Don't use WH in your question.
ask question by keywords (like national flower,capital city,old name of dhaka etc)'''
    elif p_message == 'whats up':
        return '''Hey there! Ask anything about Bangladesh
NOTE:Don't use WH in your question.
ask question by keywords (like national flower,capital city,old name of dhaka etc)'''
    elif p_message == "what's up":
        return '''Hey there! Ask anything about Bangladesh
NOTE:Don't use WH in your question.
ask question by keywords (like national flower,capital city,old name of dhaka etc)'''
    elif p_message == "bye":
        return 'Bye!!!'
    elif p_message == 'who are you?':
        return 'I am a simple bot.My name is Titho'
    elif p_message == 'tell me about you':
        return 'I am titho'
############################about titho############################
    elif p_message == 'who create you?':
        return 'Fahim'
    elif p_message == "who create's you?":
        return 'Fahim'
    elif p_message == 'who created you?':
        return 'Fahim'
#############################national things#############################
    elif p_message == 'national flower':
        return 'Water lili '
    elif p_message == 'national fruit':
        return 'Jack fruit'
    elif p_message == 'national bird':
        return 'Magpie robin'
    elif p_message == 'national fish':
        return 'Hilsa'
    elif p_message == 'national river':
        return 'The Jamuna river'
    elif p_message == 'national sport':
        return 'Ha-Du-Du'
    elif p_message == 'national animal':
        return 'The Royal Bengal Tiger'
    elif p_message == 'national game':
        return 'Ha-Du-Du'
    elif p_message == 'national anthem':
        return 'Amar Shonar Bangla by Rabindranath Tagore https://youtu.be/eEK7pF1hIzc'
    elif p_message == 'national poet':
        return 'Kazi Nazrul Islam'
    elif p_message == 'national day':
        return 'Sunday, March 26'
    elif p_message == 'national symbol':
        return 'National Emblem of Bangladesh'
    elif p_message == 'national food':
        return ' Rice with fish'
    elif  p_message == 'national mosque':
        return 'Baitul Mukarram National Mosque'
###################################important days########################
    elif p_message == 'international mother language day':
        return '21 February'
    elif p_message == 'victory day':
        return '16 December'
    elif p_message == 'independence day':
        return '26 March'
    elif p_message == 'may day':
        return '1 May'
    elif p_message == 'labour day':
        return '1 May'
###################################cool stufs############################
    elif p_message == 'old name of dhaka':
        return 'Jahangirnagar'
    elif p_message == 'capital  city':
        return 'Dhaka'
    elif p_message == 'old name of capital city':
        return 'Jahangirnagar'
    elif p_message == 'old name of bangladesh':
        return 'East Pakistan'
##########################common staf###################################
    elif p_message == 'common bird':
        return 'Sparrow'
    elif p_message == 'common animal':
        return 'Dogs and Cat'
    elif p_message == 'common food':
        return 'Rice'
    elif p_message == 'common vehicle':
        return 'Rickshaw'  
##################################biggest############################
    elif p_message == 'largest river':
        return 'Brahmaputra'
    elif p_message == 'largest bridge':
        return 'The Padma Sheto'
    elif p_message == 'largest city':
        return 'Dhaka'
    elif p_message == 'largest building':
        return 'City Centre Dhaka'
    elif p_message == 'largest flyover':
        return 'The Mayor Mohammed Hanif Flyover'
    elif p_message == 'biggest district':
        return 'Rangamati'
    elif p_message == 'biggest university':
        return 'Dhaka University'
########################popular staf####################################
    elif p_message == 'most popular  drink':
        return  'Tea'
    elif p_message == 'popular drink':
        return 'Tea'
    elif p_message == 'most crowded place':
        return 'Dhaka'
    elif p_message == 'popular food':
        return 'Kacchi'
    elif p_message == 'popular place':
        return 'There are many popular place in Bangladesh.You can checked them on Google.'
    elif p_message == 'populer vehicle':
        return 'Boat'
    elif p_message == 'popular sweet':
        return 'Rosh malai'
###################################important############################
    elif p_message == 'prime minister':
        return 'Sheikh Hasina'  
##################################failur################################## 
    else:
        return 'Try to ask this in another way or check your spelling and puntuation marks.'

