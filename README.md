This is a repository for [Otsimo Machine Learning Task](https://gitlab.com/-/snippets/2078938)
<p>
**wordCount**: Represent all the word in the text.<br>
**longestWord**: Represent longest word in the text.<br>
**language**: Represent the language of the text. It checks for stop words in the text and if number of english stop words more than turkish it returns English or vice-versa.<br>
**avgLength**: Represent average length of the words. First it counts all the letters (spaces and punctuations not counts) and divide id by wordCount.<br>
**letters**: Represent number of letters (spaces and punctuations not counts, It is different then len(text)).<br>
**alphabeticMedian**: Represent the median word when words ordered alphabetically.<br>
**medianWordByLength**:  Represent the median word when words ordered by their length.<br>
**mostFrequent**: Represent the most 5 frequent words in the text.<br>
**Duration**: Represent the reading duration of text in seconds. wordCount/265*60 refference to [Medium Read Time](https://help.medium.com/hc/en-us/articles/214991667-Read-time).<br>
</p>

After you run the script you can use following comand on your terminal:

curl -d '{    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing.\n\nHowever, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place.\n\nNeurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world."
}' -H "Content-Type: text/json" -X POST 127.0.0.1:9000/analyze

function_test.py is just for testing the function used in API.
