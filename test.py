import re
liste = ['very interesting. it is a part of future', 'This is awe inspiring.', 'It is not clear that when he used the analogy of the matrix of numbers as a kind of brain fingerprint, whether that anology holds over time. A fingerprint does not change over time, but cannot an individual develop skills over the same timeframe. If indeed the brain signature does not change (or if that is the claim), then what you could be measuring is potential. It does bother me to think that once a scan is done on an individual, then the matrix is set in stone and there is no possibility for that unique person to grow and change.', 'So they can already records dreams, so cool, I will do a PhD in neurosciences in 5 years and I’ll try to make the nervegear in SAO a reality', 'i think this might be the best thing ive ever seen', 'Chung and Jordan Peterson could 100% do exact voice imitations of each other', 'I’m studying psychology and it seems as if my undergraduate degree is no longer useful if AI can do all the work of a psychologist so I’m doing minor in biology and then study cognitive science in grad school', 'After considering to study master of neuroscience , this video just came to my youtube :D', 'MRI. Brain scanners. Measure brain activity\nFrmi - Telescope\nMicroscope\nFrmi - what different parts of the brain do', 'brilliant :)', 'More research should be conducted on the neuroscience of intelligence....', 'incredible!', "Using Pre collected Data from brain activity and storing it into organized libraries which then can be accessed by a machine(computer) reading your brain and use it's real time machine learning skills to interpret your thoughts and output them into a monitor to give you a much clearer image of what you are thinking. Makes sense. Take my money lol", 'Can guess what you are looking at\nMatrix of numbers unique to you - functional connectome - brain fingerprint', 'To all humans Stop being  cry babies\n, artificial Intelligence do needs holidays according to labour law. So let them practise their rights', 'Oh my God', 'the video requires payment??\n\nTED TALKS SHOULD ALWAYS BE FREE!\nif the speaker wants to start a lesson on another platform thats monetized.. do that.. but dont insult your ted supporters by putting it on a free platform and charging us!', "You can not; Can not equate someone's intelligence by whatever method you used.", 'Vijay :-)....aj166', 'so basically, there ill be no such thing as human anymore...  everyone on phones and computer now (serial port) ... 20 yrs down line - everyone brain will be connected (wifi)....   we will all be cyborgs and controlled by a 16 yr old in his grandmas basement (who downloaded a script from 4chan and will be playing us all like a game of sim city) welcome to the future.', 'Only 18 comments its december 2020!!!', 'Do u believe in god', "he sounds like he's about to cry", "This guy is telling lies A.I learns things from an A.I cloud. They have the ability to know whts right or wrong because they mock us and mimic us. He's speaking as if this is in 90's. It's 2019 and the new age A.I has it's own algorithms. 🤔"]
for i in liste: 
    i = i.rstrip()
    i = i.rstrip("\n")
    i = re.sub(r'[^\w\s]','',i)

print(liste)