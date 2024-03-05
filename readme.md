# Problem Statement:
Throughout history, academic learning that can be recorded and evaluated has been confined to schools. However, nowadays indicators of learning are more than just essays and responses to multiple choice exams – millions of people on the Internet provide tangible artifacts and evidence of knowledge progression every single day. One of the most accessible sources of data for learning is through online forums, the most popular of which being hosted on the website Reddit. Within Reddit, there are subreddits – online communities dedicated to talking about a singular topic – that have publicaly available data.

Users’ language is at the heart of understanding learning in these subreddits and other online forums. After all, users are not being given tests to show their understanding; rather, what they say signals how much they have learned. Research has yet to apply methodologies of language analysis and theoretical frameworks of user-community interaction within the field of learning sciences. Our inquiry uses the theoretical framework of _Legitimate Peripheral Participation Theory_ (Lave & Wenger, 1991), which characterizes learning at the individual level as a progression from the periphery of a community to the center. My project in collaboration with Professor Sherin examines the specific application of this theory in online communities with the guiding research question **how does progression of expertise differ among various subreddits?**

Our methodology focuses on the adoption of key vocabulary because it is the best approximation for both learning and _acculturation_ – adapting to a culture by learning its explicit and implicit rules – because correct vocabulary usage entails understanding both meaning and style. In order to investigate this adoption (or potentially lack thereof) of language, our scripts output graphs plotting the similarity between the language of a community at a certain time point (e.g. week 1) and the language of the community during its whole lifespan, thus creating a rough trajectory of acculturation. Each script does this through different measures of similarity -- KL-divergence and ngram similarity respectively. In short, the main difference between the two is that bigram similarity strings together the conditional probability of two word sequences (or bigrams), thus making the measure a bit more context-dependent than KL-divergence.

# General Outline of Steps:
1. Pre-process and clean text
2. Put text into bins based on time elapsed from user's first post (e.g. first bin is week 1, second is week 2, etc.)
3. Convert text into desired input format for similarity measures
4. Run similarity measures between each bin's vocabulary and the overall vocabulary

# Areas of Improvement:
- Faster and more accurate (e.g. not mushing words together) data cleaning
- Implementing Laplace smoothing into model used in ngram similarity
- Bins should hold a uniform number of posts instead of being disproportionate and arbitrarily-defined (currently just by week)
- Potentially filtering posts out from users that don't stay in the community long enough
- Deciding whether to add in "UNKNOWN" tokens (denote that a bigram doesn't occur enough times to be significant to community vocabulary) based on vocabulary from each bin or the subreddit's whole lifespan

# FAQ's:

### How do I extract a file to use in the scripts?
1. Download torrent for all subreddit data here: [https://academictorrents.com/details/c398a571976c78d346c325bd75c47b82edf6124e](url)
2. Using QBitTorrent, download selected folders (will end up just giving you a folder of all the subreddits anyways)
3. Move the zipped folders into desired subdirectory for all different subreddit data -- DO NOT NEED TO EXTRACT IT TO A DIFFERENT DIRECTORY
4. Filter file script (https://github.com/Watchful1/PushshiftDumps/blob/master/scripts/filter_file.py) will just use the zipped folder as its input
5. Store the outputted file

# References:
Lave, J., & Wenger, E. (1991). Situated learning: Legitimate peripheral participation. Cambridge University Press.
