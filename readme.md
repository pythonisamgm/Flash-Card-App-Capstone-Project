# Flash Card App

This Python script creates a flash card application to help you learn French words using a graphical user interface (GUI) built with Tkinter. The script reads data from a CSV file containing French-English word pairs, displays a random French word, and allows the user to flip the card to see the English translation. Users can mark words they know, and the script will save the progress to a new CSV file.

## Installation

1. Clone the repository or download the script files.
2. Make sure you have Python installed on your system. This script requires Python 3.x.
3. Install the necessary Python packages using pip:
    ```sh
    pip install pandas
    ```

## Usage

1. Ensure you have a CSV file named `french_words.csv` in the `./data` directory. The CSV should have the following format:
    ```
    French,English
    partir,leave
    faire,do
    ...
    ```

2. Run the script:
    ```sh
    python flash_card_app.py
    ```

## Script Details

The script performs the following operations:

1. **Reading Data from CSV:**
    ```python
    df = pandas.read_csv("./data/french_words.csv")
    to_learn = df.to_dict(orient="records")
    to_learn2 = []
    ```

2. **Selecting a Random Card:**
    ```python
    def next_card():
        global CURRENT_CARD, flip_timer
        window.after_cancel(flip_timer)
        CURRENT_CARD = random.choice(to_learn2)
        french_value = CURRENT_CARD["French"]
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(word, text=french_value, fill="black")
        window.after(3000, flip_card)
    ```

3. **Flipping the Card to Show the Translation:**
    ```python
    def flip_card():
        english_value = CURRENT_CARD["English"]
        canvas.itemconfig(canvas_image, image=card_back_img)
        canvas.itemconfig(title, text="English", fill="white")
        canvas.itemconfig(word, text=english_value, fill="white")
    ```

4. **Saving Known Words to a New CSV File:**
    ```python
    def is_known():
        to_learn.remove(CURRENT_CARD)
        data = pandas.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        next_card()
    ```

5. **Loading Known Words from CSV File:**
    ```python
    try:
        df2 = pandas.read_csv("data/words_to_learn.csv")
    except:
        data2 = pandas.DataFrame(to_learn)
        data2.to_csv("data/words_to_learn.csv", index=False)
        df2 = pandas.read_csv("data/words_to_learn.csv")
    to_learn2 = df2.to_dict(orient="records")
    ```

6. **Deleting Known Words from the List:**
    ```python
    def known_answer():
        to_learn2.remove(CURRENT_CARD)
        data2 = pandas.DataFrame(to_learn2)
        data2.to_csv("words_to_learn.csv", index=False)
    ```

7. **Setting Up the User Interface:**
    ```python
    window = Tk()
    window.title("Flashy")
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
    flip_timer = window.after(3000, flip_card)

    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_back_img = PhotoImage(file="./images/card_back.png")
    card_front_img = PhotoImage(file="./images/card_front.png")
    canvas_image = canvas.create_image(410, 270, image=card_front_img)
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    title = canvas.create_text(400, 150, fill="black", font=("Ariel", 40, "italic"))
    word = canvas.create_text(400, 263, fill="black", font=("Ariel", 60, "bold"))
    canvas.grid(column=0, columnspan=2, row=0)

    check_image = PhotoImage(file="./images/right.png")
    known_button = Button(image=check_image, highlightthickness=0, command=lambda: [next_card(), known_answer()])
    known_button.grid(column=1, row=1)

    cross_image = PhotoImage(file="./images/wrong.png")
    unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
    unknown_button.grid(column=0, row=1)

    next_card()

    window.mainloop()
    ```

## Example

Here is an example of how the script works:

- It selects a random French word from the CSV file and displays it.
- The user can click a button to see the English translation.
- The user can mark the word as known, and the script will remove it from the list of words to learn and save progress to a CSV file.

