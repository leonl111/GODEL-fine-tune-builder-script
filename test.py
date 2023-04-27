def func():
    obj = {'Context': 'I need information on a hotel that includes free parking please. EOS There are 29 hotels that meet your needs. Would you like to narrow your search by area and/or price range? EOS I also need free wifi, and it needs to be a hotel, not a guesthouse or anything like that. EOS The Ashley Hotel is in the north area of town in the moderate price range with internet and parking. Would you like to book a room? EOS Is there a fitness center onsite at the hotel? EOS The Ashley Hotel does not have a fitness center or gym onsite. Would you like to make a reservation? EOS Does The Ashley Hotel take Master card for payment?', 'Knowledge': 'Q: Which credit cards do you accept for payment? A: We accept Visa, mastercard, aestro, sold and switch.', 'Response': 'Yes, it does accept Master card as payment? Would you like to book a stay at the Ashley hotel?'}
    yield 0, obj


print(next(func()))
