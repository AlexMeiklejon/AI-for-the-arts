# %% [markdown]
# # I am learning Python coding with the help of Copilot.
# **Here is the prompt I put into Copilot:**
# “Could you suggest a python code for ‘Hello, world!’to demonstrate the concept of printing to a complete beginner in programming? Please explain the code step-by-step highlighting any key aspects.”
# 
# **Here is the response Copilot gave me:**
# "print("Hello, World!")"

# %%

print("Hello, World!")

# %% [markdown]
# This above is my first attempt at coding in this codespace, and by following this i have learnt the difference between a markdown cell and code cell.

# %% [markdown]
# # Now I am going to look at other prompts in Microsoft Copilot:
# ### Variables
# 
# **Initial Prompt:**
#  Could you suggest a modification of the Python code for “Hello, 
# world!” to demonstrate the concept of variables to a complete beginner in 
# programming? Please explain the code step-by-step highlighting any key 
# aspects.
# 
# **Copilot response:** Copilot explained that a variable in Python is like a labeled box where you can store information to use later. 
# It explained that I need to create a greeting, in this case this would be 'Hello', a target which Copilot said would be 'world', and punctuation would be '!'.
# This would look like the following:

# %%
# 1) Create variables
greeting = "Hello"
target = "world"
punctuation = "!"

# 2) Combine them to make the message
message = greeting + ", " + target + punctuation

# 3) Show the result
print(message)

# %% [markdown]
# I am going to use this code I have learnt to create my own new variable:

# %%
# 4) Change a variable and reuse it
target = "Github"
message = greeting + ", " + target + punctuation
print(message)

# %% [markdown]
# **Copilot's tips to remember:**
# - Use clear, lowercase names with underscores. Names can’t start with a number and can’t use spaces.
# - Storing parts in variables makes your code easier to change. If you update the variable once, all outputs can reflect the change.
# 
# Copilot also discussed f-strings, which I asked to describe in more detail:
# 
# **Initial Prompt:** 
# Can you explain the f strings step by step and more simply.
# 
# **Copilot Response:** 
# It explained to firstly put my text into variables, which i have already done. Then add the f before the quotes: The f tells Python this is a “formatted string” (an f-string).
# Next use curly braces to insert values: Write {greeting} where you want the value of greeting to appear. Do the same for {name} and {punctuation}.
# Build the final message inside one string: Python replaces each {...} with the current value of that variable, making "Hello, Alex!".
# 
# Now that I fully understand f strings, here is my new code:

# %%
greeting = "Hello"
name = "Alex"
punctuation = "!"
print(f"{greeting}, {name}{punctuation}")

# %% [markdown]
# ### Functions
# 
# Firstly, I wanted to ask Copilot more about functions so I can understand what they are and what they do:
# 
# **Initial Prompt:**
# What are functions and why are they important?
# 
# **Copilot Response:**
# 
# - A function is a named block of code that carries out a particular job.
# - It can take inputs (parameters), process them, and often give back an output (return value).
# 
# 
# Why are functions important?
# 
# *Organization & clarity:* Functions break a big program into smaller, manageable pieces. Each piece has a clear purpose, which makes the whole program easier to read and understand.
# 
# *Reusability:* Once you write a function, you can use it multiple times without rewriting the same code. For example, a calculate_tax() function can be reused whenever tax needs to be computed.
# 
# *Avoid repetition:* Without functions, you’d have to copy-paste the same code everywhere. Functions let you write it once and call it whenever needed, reducing errors.
# 
# *Collaboration:* In team projects, different people can work on different functions. This modular approach makes teamwork smoother.
# 
# *Debugging & maintenance:* If something goes wrong, you only need to fix the function in one place. This makes troubleshooting much easier.
# 
# *Scalability:* As programs grow, functions help keep complexity under control. They act like mini-programs inside the larger program.
# 
#     I then asked Copilot the same prompt again, to see if it would provide an answer with different or new information:
# 
# **Initial Prompt:**
# What are functions and why are they important?
# 
# **Copilot Response:**
# - A function is a named block of code that performs a specific task.
# - Think of it like a recipe: you give it ingredients (inputs), it follows steps (the code), and it produces a dish (the output).
# - In Python, you define a function with def and call it by its name.
# 
# #### Now I am going to ask it about introducing functions into my code: 
# 
# **Initial Prompt:**
# Could you suggest a modification of the Python code for “Hello, 
# world!” to demonstrate the concept of functions to a complete beginner in 
# programming? Please explain the code step-by-step highlighting any key 
# aspects.
# 
# **Copilot Response:** Copilot explained that I firstly need to define a function: def make_greeting(name): this creates a reusable block of code named make_greeting. The part in parentheses, name, is a parameter—an input the function expects.
# Then I make a function body: Inside the function, we build the text in message. This code runs only when the function is called, not when it’s defined.
# Next create a return value: return message sends the finished result back to wherever the function was called. Without return, the function does work but doesn’t hand back a value.
# Calling the function: make_greeting("world") runs the function with the input "world". Wrapping it in print(...) shows the returned text on screen.
# The same function works for any name. Therefore changing the input changes the output, so I avoid rewriting logic multiple times!
# 
# I am going to put the code it gave me in below, using what I have also learnt from previous prompts:

# %%
# 1) Define a function
def make_greeting(name):
    """Return a greeting message for the given name."""
    message = "Hello, " + name + "!"
    return message

# 2) Use (call) the function
print(make_greeting("world"))

# 3) Reuse the same function with different inputs
print(make_greeting("Github"))
print(make_greeting("Alex"))

# 4) A cleaner version using f-strings
def make_greeting_fast(name):
    return f"Hello, {name}!"

print(make_greeting_fast("Python"))

# %% [markdown]
# **Key learning outcomes**
# - I can group instructions together under a name and run them whenever I need.
# - By passing in different inputs, the same function can produce different results without rewriting code.
# - A function can hand back a value that I can store in a variable, print, or use in other parts of my program.
# - Functions make programs easier to understand, organise, and maintain, especially as they grow larger.
# 

# %% [markdown]
# ### Loops
# **Initial Prompt:** Could you suggest a modification of the 
# Python code for “Hello, world!” to demonstrate the concept of loops to a 
# complete beginner in programming? Please explain the code step-by-step 
# highlighting any key aspects.
# 
# **Copilot Response:** Copilot explains that there is two simple ways to use loops: 'for loop' and 'while loop'.
# 
# **For Loop:** 
# - The Loop keyword 'for' starts a loop that goes through a sequence of values.
# - The Loop variable 'i' is a variable that takes each value from the sequence, one by one.
# - The Range function, for example range(5) creates the sequence 0, 1, 2, 3, 4 (five numbers, starting at 0).
# - The Loop body, the indented line print("Hello, world!", "Count:", i) runs once per value of i.
# - Output meaning, you’ll see five lines, each showing the message and the current count (0 to 4).
# 
# Here is an example of code using 'for loop':

# %%
# Example 1: Using a for loop with range
for i in range(5):
    print("Hello, world!", "Count:", i)

# %% [markdown]
# **Now Copilot explains 'while loop':**
# - Initialize a counter: count = 0 sets up a starting number.
# - Loop condition: while count < 5: keeps looping as long as the condition is true.
# - Loop body: The indented print runs each time the condition holds.
# - Update step: count += 1 increases the counter by 1, helping the loop eventually stop.
# - Stopping point: When count reaches 5, the condition becomes false, and the loop ends.
# 
# Here is an example of code using 'while loop':

# %%
# Example 2: Using a while loop
count = 0
while count < 5:
    print("Hello, world!", "Count:", count)
    count += 1

# %% [markdown]
# I am going to change the count and replace '5' with a different number to control how many times it prints, and edit the string to print a different message:

# %%
for i in range(11):
    print("Welcome to my Github!", "Count:", i)

# %% [markdown]
# This seems like it could be useful to repeat actions automatically instead of having to write the same line of code over and over, especially to process multiple items, check conditions repeatedly, or automate tasks that follow a pattern. I have asked Copilot how this could be used data collection or practically for reports.
# 
# **Initial Prompt:** How could loops in Python be applied practically and useful for things like projects and data collection?
# 
# **Copilot Response:** An example could be printing even numbers for a data collection report.
# 
# Here this is shown in the following code:

# %%
for i in range(0, 21, 2):   # start at 0, go up to 20, step by 2
    print("Even number:", i)

# %% [markdown]
# ### Lists
# **Initial Prompt:** Could you suggest a modification of the Python code for “Hello, world!” to demonstrate the concept 
# of lists to a complete beginner in programming? Please explain the code step-by-step highlighting any key aspects
# 
# **Copilot Response:** 


