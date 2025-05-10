# Reflection

Student Name:  Brayden Dawson
Student Email:  Bcdawson@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

This project helped me reinforce a lot of the concepts we practiced in IST 356. I learned how to structure a real-world Python application using modular files, such as separating the extract and transform logic into their own scripts. I also learned how to build a user interface using Streamlit and connect it with live API data from OpenWeatherMap.

One area I struggled with was handling API authentication errors. At one point, my API key worked in the browser but not in my Python code, and debugging that took more time than I expected. I learned how to use print statements and `st.write()` for debugging in Streamlit, and I now understand how secrets and environment variables are used to manage API keys securely.

Another challenge was learning how to implement caching. Once I understood how to check for an existing file and load it with `json.load()`, it became much clearer. I had never used file-based caching before, and I now see how useful it is to reduce API calls and speed up performance.

I also learned how to write unit tests for individual functions using `pytest`. While simple, writing tests helped me confirm that my data transformations were behaving as expected and made me more confident that future changes wouldn't break the app.

If I had more time, I would extend the dashboard with additional filters, like choosing temperature units (Celsius/Fahrenheit), or allowing users to select specific date ranges for the forecast. I would also try deploying it online using Streamlit Cloud so others could interact with it more easily.

Overall, this project helped me apply what I’ve learned about functions, APIs, Streamlit, testing, and data visualization — and gave me a better sense of how to build and organize Python projects from scratch.
