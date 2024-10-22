# LING 581 Final Project Proposal
Sentiment analysis of 6 major news organizations 

## Personal relevancy:
I am planning on going into journalism after I graduate in April, and I am interested in the sentiment analysis/natural language processing aspect of the field. I believe that fake and overly biased news has a large negative influence on individuals, which in turn affects current politics and policies. 
While there are likely many solutions to this issue, one potential solution is to help readers understand what they are reading through sentiment analysis. An indication that an article is not neutral is simply in what language it uses—is the language provocative or charged? There is some current research like the All-sides Bias Checker that allows you to enter a URL and check what they ranked the bias as. However, this checker advertises that it relies largely on human analysis and only partly on machine learned algorithms. 
Focusing my project on natural language processing in journalism will advance my own data analysis capability, which is crucial to being a well-informed journalist. I also believe seeing how other publications manage bias will help readers of my own research be more aware of what these publications are doing, whether purposeful or not. 

## What I would like to accomplish:
For this project, I would like to analyze articles from six different news outlets, three largely recognized as Left-leaning papers and three largely recognized as Right-leaning papers. From the Left, I will use CNN, The Washington Post, and The Associated Press. From the Right, I will use The Washington Examiner, The Epoch Times, and The New York Post. Since these publications all produce articles on the same events, I will use their respective reporting and compare results for articles on the same topics. I will be creating my own corpus, and I will find 10 articles from each outlet. All of these publications are open sourced but The Washington Post, which could pose an issue. If I cannot access enough from The Washington Post, I will change this publication to another Left-leaning publication. 
I will write my own code to calculate a sentiment score, using Naïve Bayes techniques. I plan on using Python. Before calculating all my data, I will test my code against previously constructed code to ensure its accuracy. Sentiment is not too complicated and there has been research done on it for decades, so I’m not worried about finding questions to my coding questions. 

## Potential challenges:
One aspect of this project I am not sure how to account for yet is tone. According to previous research I’ve read, sentiment analysis algorithms have a hard time recognizing satire and sarcasm from charged language. I am worried about this specifically with the New York Post, where humans who read can easily recognize snark in its language, which is simply a stylistic choice. 

## Methodology:
To keep track of the data I am using, I have included a public GitHub repository for this project. Here I will manage my articles in txt files, allow public access to my code, and have an explanation for my methodology in a ReadMe file. 
Samuels and Mcgonical’s article outlined recent influential work in news sentiment analysis and referenced research published at the University of Bangladesh. This team performed sentiment analysis on news articles at a sentence level and used a dynamic dictionary with predefined positive and negative words. I will find a similar dictionary and check it to make sure the words’ scores are not biased themselves. After they had the dictionary, they selected online news articles, extracted sentences from them, and searched for positive words or phrases to find their polarities. This team found 91% accuracy results. I plan on having a similar approach, but instead of searching only for positive language, I will search for positive and negative language to have a more holistic understanding of these news publications. I will also save the words with the highest polarity scores and will present them. 

## Expandability:
I believe this project will reveal greater insight into what is popularly referred to as “media bias” by viewing news organizations through their word choice and its calculated sentiment. To end my project, I would like discuss other alternative sentiment analysis methods like deep learning or transformer-based models like BERT. 

Previous Research on News Sentiment Analysis — background provided in Samuels and Mcgonical’s article:

-	Reis, Olmo Benevenuto, Prates, and An:
o	They studied how the sentiment (positive, negative, neutral) of news headlines affects the popularity of articles.
o	By analyzing over 69,000 headlines from major media outlets (e.g., The New York Times, BBC), they found that headlines with positive or negative sentiments were more popular than neutral ones.
-	Islam, Ashraf, Abir, and Mottalib:
o	They created a method to classify news articles by sentiment using a dictionary of predefined positive and negative words.
o	Sentiment analysis was done at the sentence level, and by combining the sentiment of all sentences, they determined the overall sentiment of the news article. Their approach was 91% accurate in classifying news articles.
-	Lei, Rao, Li, Quan, and Wenyin
o	Developed a model to detect social emotions triggered by news articles, tweets, and similar content. The model has several components, including selecting documents, tagging parts of speech (POS), and generating lexicons for social emotions.
o	The process starts by creating a training set from a collection of news documents. Then, POS tagging and feature extraction are applied. Afterward, a social emotion lexicon is generated by calculating the likelihood of various emotions being present in the document. To assess the model’s accuracy, they tested it on a dataset of 40,897 news articles.

 

## Works Cited:

Ghadekar, P., Tilokchandani, M., Jevrani, A., Dumpala, S., Dass, S., Shinde, N. (2021). Prediction and Classification of Biased and Fake News Using NLP and Machine Learning Models. In: Swain, D., Pattnaik, P.K., Athawale, T. (eds) Machine Learning and Information Processing. Advances in Intelligent Systems and Computing, vol 1311. Springer, Singapore. https://doi.org/10.1007/978-981-33-4859-2_2

Nadeem, Muhammad Umar. Raza, Sarah. Detecting Bias in News Articles using NLP Models. Stanford University, CS224: Natural Language Processing with Deep Learning. https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1224/reports/custom_116661041.pdf

Samuels, Antony. Mcgonical, John. “News Sentiment Analysis.” University of Southern California, Caltech. 5 July 2020. https://arxiv.org/pdf/2007.02238/1000 

![image](https://github.com/user-attachments/assets/75fb462f-106e-4921-8981-64611619fd99)
