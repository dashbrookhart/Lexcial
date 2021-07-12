# Lexical 💬✍️

## About
This Text Semantic Similarity App uses a trained Natural Language Processing model to determine if two text entry answers are semantically the same. The idea for this app started in an attempt to solve a common problem we saw for professors in our Data Science program of trying to grade text answers. Grading manually is a hassle, and any current text autograder simply do not work. This product lets teachers spend more energy teaching and less time grading.


## The result
[Open the demo app!](https://share.streamlit.io/shahv1057/lexical_demo/main/st_lexical.py)

Enter in a text value to represent the Correct answer to the question and compare with various student answers to obtain a similarity score!


## Install and run
```
git clone https://github.com/MSDS698/2021-product-analytics-group-project-group_5_lexical.git
pip install -r requirements.txt
cd code
flask run
open http://127.0.0.1:5000 in your browser
```


## Coming Soon

The ability to load in a csv file full of student inputs and compare to a correct solution to automatically grade a text entry question!

