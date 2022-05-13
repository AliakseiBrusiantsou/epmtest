import telebot
from telebot import types
import requests
import re
import PIL
from PIL import Image
from requests import get

bot = telebot.TeleBot('5335366767:AAGh2nyrmQS0acJIBkOo99aly3t5YILsgGk');

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'hi, I am simplified EPAM NL bot with customized menu buttons to help you with navigation across major EPAM NL entities. Please use /menu to see all staff')
    
#@bot.message_handler(commands=['policy'])
#def start_message(message):
#    bot.send_message(message.chat.id, 'EPAM NL guideline EPAM Policies and Guides NL https://info.epam.com/policy/netherlands/all-cities/contractual-policies-and-procedures.html')

#@bot.message_handler(commands=['help'])
#def start_message(message):
#    bot.send_message(message.chat.id, 'List of available commands: /start /policy /menu /help . We highly recommend to use /menu for all available options. Commands are used for technical bot management.')

@bot.message_handler(commands=['menu'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("🏢 Office")
    item2=types.KeyboardButton("♥️ Health")
    item3=types.KeyboardButton("💰 Finance")
    item4=types.KeyboardButton("🍬 Benefits")
    item5=types.KeyboardButton("🏚 HouseRoom")
    item6=types.KeyboardButton("🚨 Emergency")
    item7=types.KeyboardButton("🤖 Bot Map")
    item8=types.KeyboardButton("⚙️ Others")
    markup.add(item1,item2)
    markup.add(item3,item4)
    markup.add(item5,item6)
    markup.add(item7,item8)
    bot.send_message(message.chat.id,'Please Chose One',reply_markup=markup)
    
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="🏢 Office":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("🛋 Facilities")
        item2=types.KeyboardButton("👱‍♀️ HR,People Operations")
        item3=types.KeyboardButton("🖥 Local IT")
        item4=types.KeyboardButton("🤰 Office Manager")
        item5=types.KeyboardButton("📖 Learning")
        item6=types.KeyboardButton("/menu")
        markup.add(item1,item2)
        markup.add(item3,item4)
        markup.add(item5,item6)
        bot.send_message(message.chat.id,'Please Chose One',reply_markup=markup)
    if message.text=="♥️ Health":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("🌂 Issurance")
        item2=types.KeyboardButton("💊 Pharmacy,Pills,Hospital")
        item3=types.KeyboardButton("🏃‍♀️ Sport")
        item4=types.KeyboardButton("🚨 Emergency")
        item5=types.KeyboardButton("/menu")
        markup.add(item1,item2)
        markup.add(item3,item4)
        markup.add(item5)
        bot.send_message(message.chat.id,'Please Chose One',reply_markup=markup)
    if message.text=="💰 Finance":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("🏦 Banks")
        item2=types.KeyboardButton("🤑 Ruling")
        item3=types.KeyboardButton("💶 Taxes")
        item4=types.KeyboardButton("👨‍🦳 Pension")
        item5=types.KeyboardButton("🏘 Mortgage")
        item6=types.KeyboardButton("/menu")
        markup.add(item1,item2)
        markup.add(item3,item4)
        markup.add(item5,item6)
        bot.send_message(message.chat.id,'Please Chose One',reply_markup=markup)
    if message.text=="🍬 Benefits":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("🚌 📱 Travel,SIM cards")
        item2=types.KeyboardButton("🏖 Vacation/Sick leave")
        item3=types.KeyboardButton("🍬 Small costs reimbursement")
        item4=types.KeyboardButton("🎉 Parties,talks")
        item5=types.KeyboardButton("/menu")
        markup.add(item1,item2)
        markup.add(item3,item4)
        markup.add(item5)
        bot.send_message(message.chat.id,'Please Chose One',reply_markup=markup)
    if message.text=="🏚 HouseRoom":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("🚪 Renting")
        item2=types.KeyboardButton("🏡 Buying")
        item3=types.KeyboardButton("🏘 Mortgage")
        item4=types.KeyboardButton("/menu")
        markup.add(item1,item2)
        markup.add(item3,item4)
        bot.send_message(message.chat.id,'Please Chose One',reply_markup=markup)        
    if message.text=="⚙️ Others":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("📡 Useful Links")
        item2=types.KeyboardButton("ℹ️ About")
        item3=types.KeyboardButton("/menu")
        markup.add(item1,item2)
        markup.add(item3)
        bot.send_message(message.chat.id,'Please Chose One',reply_markup=markup)  
    if message.text=="🚨 Emergency":
        bot.send_message(message.chat.id,
        '112 is the emergency number for fire, police and ambulance (use only in cases of emergencies)\n'+
        'Useful phrases for emergencies:\n'+
        'Call an ambulance = Bel een ambulance\n'+
        'Calling the police = Bel de politie\n'+
        'Call the fire brigade = Bel de brandweer\n'+
        'Get/call a doctor = Haal/bel een dokter\n'+
        'I am ill = Ik ben ziek\n'+
        'Don’t wait for an emergency before registering with a family doctor (huisarts)\n'+
        'Find one at www.zorgkaartnederland.nl by typing in your postcode and clicking zoek. Your health insurance company may also help you find a family doctor in your area\n'+
        'More info here https://epa.ms/nlemergency ')
    if message.text=="🤖 Bot Map":
        bot.send_message(message.chat.id,
        'list of all groups:'
        '🏢 Office (Facilities ,HR, Local IT, Office Manager, Learning)\n'+
        '♥️ Health (Issurance, Pharmacy,Pills,Hospital, Sport)\n'+
        '💰 Finance (Banks, Ruling, Taxes, Pension, Mortgage)\n'+
        '🍬 Benefits (Travel,SIM cards, Vacation/Sick leave, Small costs reimbursement, Parties,talks)\n'+
        '🏚 HouseRoom (Renting, Buying, Mortgage)\n'+
        '🚨 Emergency\n'+
        '⚙️ Others (Useful Links, About)')
    if message.text=="🛋 Facilities":
        bot.send_message(message.chat.id,
        'EPAM office is located by Address: Mercuriusplein 1, 2132 HA Hoofddorp ,  available from 8am to 8pm.  Once you enter office building without physical access card,  just ask receptionist to help with a lift\n'+
        'You may find printer/scanner/copier on 9th and 10th floors.\n'+
        'HR/Office manager/Local IT are located on 10th floor\n'+
        'Kitchen is located on 10th floor: Tangerines,bananas,kiwi,water,tea,coffee,cola,fanta,etc\n'+
        'Almost every Friday, office manager orders catering with a lunch\n'+
        'Please book seat prior your visit at https://desk.epam.com/  (meanwhile, usually there are a lot of available seats')
    if message.text=="👱‍♀️ HR,People Operations":
        bot.send_message(message.chat.id,
        'our HRs: Aldona Kokosza (principal) and Rosalynn Noomen (right hand).\n'+
        'Head of People, NL is Marcel de Mooij\n'+
        'People Operations specialist: Ghida Kleyn\n'+
        'If you have any questions, please reach out to HR_NL@epam.com')
    if message.text=="🖥 Local IT":
        bot.send_message(message.chat.id,
        'Local IT is ready to help you with hardware/custom images:\n'+
        'Nasser Silakhori and Eleni Anagnostopoulou\n'+
        'They are located on 10th floor.\n'+
        'BTW, you may request by https://support.epam.com/esp/ess.do additional monitor or other hardware by car.  Once you submit request for hardware and indicate your address, local IT creates task and deliver devices by post/car and there is no need to visit office')
    if message.text=="🤰 Office Manager":
        bot.send_message(message.chat.id,
        'NL office manager: Ilknur Basdemircan\n'+
        'In case of any paper correspondence, she informs you by email\n'+
        'It doesn`t require to have physical card in case of working from home or visiting office rarely\n'+
        'In case of often visiting office, you may ask Ilknur for physical card (your physical card from other offices are not applicable)')        
    if message.text=="📖 Learning":
        bot.send_message(message.chat.id,'Learning specialist: Krystsina Katouskaya \n'+
        'Dutch courses are organized by her and available from time-to-time\n'+
        'Useful resources to train and learn Dutch from ground up:\n'+
        'https://www.duolingo.com \n'+ 
        'https://instagram.com/mamadutch.teacher \n'+
        'telegram channel @learning_nederlands ')
    if message.text=="🌂 Issurance":
        bot.send_message(message.chat.id,
        'Basic issurance costs about 120-130 eur per month.\n'+
        'There are 3 good companies for your choice:\n'+
        'https://www.hollandzorg.com/nl \n'+
        'https://www.zilverenkruis.nl \n'+
        'https://zorgverzekeringhema.nl \n'+
        'Basic packadge is enough. Can be purchased with BSN and opened bank account only')
    if message.text=="💊 Pharmacy,Pills,Hospital":
        bot.send_message(message.chat.id,
        'Most of pills can be puchased by prescription only.\n'+
        'Find your family doctor (GP) https://www.kiesuwhuisarts.nl/ \n'+
        'Hospital visit is available only by appoitment from GP\n'+
        'A hospital is called ziekenhuis. Complete list of hospitals and medical centres www.ziekenhuis.nl \n'+ 
        'More information https://www.expatica.com/nl/healthcare/healthcare-services/hospitals-in-the-netherlands-100735/ ')
    if message.text=="🏃‍♀️ Sport":
        bot.send_message(message.chat.id,
        'EPAM has vitaliy program: https://info.epam.com/policy/netherlands/all-cities/contractual-policies-and-procedures/benefits/vitalityprogram.html \n'+
        'Weekly rewards: get a voucher/ product from f.e. Bol.com and Zalando. More information can be found in the app.\n'+
        'Monthly rewards: buy your Apple Watch/ Fitbit via a.s.r. Vitality (in the app) and connect it to the app*. If you meet your monthly goal you will receive a reimbursement for the Apple Watch/ Fitbit \n'+
        'Annual rewards: receive a cashback on your additional health insurance and dental insurance.\n'+
        '\n'+
        'Office is not equipped by gym; EPAM doesnt reimburse sport activities.\n'+
        'telegram channel: @velobenelux – all about bicycles')
    if message.text=="🏦 Banks":
        bot.send_message(message.chat.id,
        'It needs to have BSN first prior to open bank account\n'+
        'Popular banks: \n'+
        'ABN AMRO https://www.abnamro.nl/ \n'+
        'ING https://www.ing.nl/ \n'+
        'Revolut https://www.revolut.com/en-NL \n'+
        'Bunq https://www.bunq.com/ \n'+
        'In exceptional cases: create online account at Revolut (acceptable by NL accountants), and once you get BSN, open regular account)\n'+
        'Notes: https://www.abnamro.nl/en/personal/specially-for/expats/international-clients-desk.html ')
    if message.text=="🤑 Ruling":
        bot.send_message(message.chat.id,
        '30% tax ruling can be apllied once you  receive BSN \n'+
        'Contact HR to apply for ruling, they wil redirect you to LIMES company that helps with submitting application form \n'+
        'Duration: 5 years only \n'+
        'More about ruling: https://info.epam.com/policy/netherlands/all-cities/contractual-policies-and-procedures/benefits/30--tax-ruling/30--ruling-process.html ')
    if message.text=="💶 Taxes":
        bot.send_message(message.chat.id,
        'It`s your personal responsibility to track and report your taxes on annual basis \n'+
        'calculate your taxes online https://thetax.nl \n'+
        'All info about taxes can be found here in telegram chat https://t.me/nalognl_talk or on site https://www.nalog.nl/ ')
    if message.text=="👨‍🦳 Pension":
        bot.send_message(message.chat.id,
        'There are 2 options: \n'+
        'medical issurance (read appropriate group at this bot) \n'+
        'or EPAM pension scheme. https://info.epam.com/policy/netherlands/all-cities/contractual-policies-and-procedures/benefits/pension-scheme/pension-provision-in-the-netherlands.html . Based on expirience, EPAM pension scheme is useful once tax ruling is ended.\n'+
        'You need to inform HR about your decision: issurance or pension.')           
    if message.text=="🏘 Mortgage":
        bot.send_message(message.chat.id,
        'Mortgage is highly depend on your salary base (not overtime payments or additional bonuses)\n'+
        'Check online bank calculators for max mortgage https://www.abnamro.nl/en/personal/mortgages/calculating-your-maximum-mortgage.html \n'+
        'Read more about mortgage https://rabotaem.nl/housing/faq-ipoteka-v-niderlandah/ ')
    if message.text=="🚌 📱 Travel,SIM cards":
        bot.send_message(message.chat.id,
        'Ask office manager to receive card NS Business Card (NSBC). This is an OV-chipcard that offers you an all-in-one (bus,tram,metro,all trains) travel solution within the Netherlands. https://info.epam.com/policy/netherlands/all-cities/contractual-policies-and-procedures/benefits/ns-businesscard-and-commuting-expenses/public-transport-strikes.html \n'+ 
        'The subscription is ordered from NS, you will receive a confirmation e-mail with the log in details to the portal (log in to the potal and activate card). You must check in and out when using the NSBC \n'+
        'You`ll receive NBSC card with Off-peak subscription by default. When you use your card for minimal € 120,- per month, you will receive a new card with the Subscription OV-vrij \n'+
        'Re SIM-card, please ask Local IT to receive it. More info https://info.epam.com/policy/netherlands/all-cities/contractual-policies-and-procedures/benefits/simcard.html \n'+
        'You`ll have unlimited internet in NL (in case of traveling in EU, traffic is limited by 10 GB ')
    if message.text=="🏖 Vacation/Sick leave":
        bot.send_message(message.chat.id,
        'There are regual PTO, additional PTO, exceptional leave, unpaid leave, overtime leave and meternity/paternity leaves \n'+
        'More about process https://info.epam.com/policy/netherlands/all-cities/contractual-policies-and-procedures/policies--procedures/leave-types/regular---additional-pto.html ')
    if message.text=="🍬 Small costs reimbursement":
        bot.send_message(message.chat.id,
        'You`ll receive costs reimbursement for small costs (short parking, professional literature, office supplies, setting up your home office) of € 40,- per month. This amount will be automatically added to your monthly salary.\n' +
        'Don`t need to request/report it additionally')
    if message.text=="🎉 Parties,talks":
        bot.send_message(message.chat.id,
        'There are Summer/Winter parties organized by Head of People, NL Marcel de Mooij.  Keep his emails attentively\n'+
        'Next party will be on 🔥JUNE 24, 2022 at AMSTERDAM WEST🔥\n' +
        'Moreover: TechTalks, Town Halls, Trainings, Strava Club, Friday`s afternoon drinks.. :) ')
    if message.text=="🚪 Renting":
        bot.send_message(message.chat.id,
        'Rent house/apartment use sites: \n'+
        'https://www.pararius.com \n'+
        'Rent a room use sites: \n'+
        'https://kamernet.nl/ (ask EPAMers in chat for referral code \n'+
        'FB groups: \n'+
        'https://www.facebook.com/groups/396367587188451 \n'+
        'https://www.facebook.com/groups/484600675031215 \n'+
        'Duration for renting contracts: 6+ months, 1 year with indefinite option \n'+
        'More info https://rabotaem.nl/housing/arenda-zhilya-v-niderlandah/ \n'+
        '\n'+
        'Be aware, there are a lot of scamers. Don`t pay without offline view,  don`t be fooled.')
    if message.text=="🏡 Buying":
        bot.send_message(message.chat.id,
        'You need to have financial advisor, broker, inspector, and other specialists. \n'+
        'a lot of talks in telegram chat @RealEstateNL \n'+
        'Read more https://rabotaem.nl/housing/pokupka-nedvizhimosti-v-niderlandah-chast-i/ ')
    if message.text=="📡 Useful Links":
        bot.send_message(message.chat.id,
        'telegram channels:\n'+
        '@inBenelux – все люди, общий чат (взаимопомощь, практические вопросы)\n'+
        '@RealEstateNL – всё про поиск, покупку и продажу недвижимости в НЛ\n'+
        '@immigration2nl – вопросы и ответы об иммиграции в Нидерланды и эмиграции из СНГ\n'+
        '@BeneluxInsuranceAndLaw – о страховых и юридических вопросах в Бенилюксе\n'+
        '@InvestInNL – инвестиции, финансы, биржа\n'+
        '@learning_nederlands – чат про изучение голландского\n'+
        '@parentsInBenelux – чатик для родителей\n'+
        '@autobenelux – все про машины\n'+
        '@DelovoyBenelux – всё о ведении бизнеса в Бенилюксе\n'+
        '@nlriders – русскоязычные мотобратья и мотосестры Бенилюкса\n'+
        '@Bnl_baraholka – Купи-Продай-Отдай\n'+
        '@benelux_foodie – о еде в Бенилюксе\n'+
        '@PetsNL – Все о наших четвероногих друзьях и их быте\n'+
        '@velobenelux – всё о велосипедах\n'+
        '\n'+
        'Facebook:\n'+
        'https://www.facebook.com/groups/396367587188451 \n'+
        '\n'+
        'Youtube: \n'+
        'https://www.youtube.com/c/amsterdammers\n'+
        '\n'+
        'Instagram:\n'+
        'https://instagram.com/mamadutch.teacher ')     
    if message.text=="ℹ️ About":
        bot.send_message(message.chat.id,"создано на коленке за один вечер. есть /help . Присылайте пожалуйста любые пожелания (что нравится, что не нравится и надо убрать, или видоизменить) (какой контент добавить, какие темы раскрыть побольше) (какие полезные автоматизации хочется видеть) сюда @Banzaaai или Aliaksei Brusiantsou")
bot.infinity_polling()
