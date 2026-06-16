import pandas as pd
df = pd.read_csv("questions.csv")

while True:
    print("\n===== DSA COACH =====")
    print("1. Show all questions")
    print("2. Mark question as solved")
    print("3. Show progress")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(df[["topic", "question", "completed"]])

    elif choice == "2":

        try:
            q = input("Enter question name: ").strip().lower()

            questions = df["question"].str.lower()

            if q not in questions.values:
                raise ValueError("Question not found!")

            df.loc[questions == q, "completed"] = "Yes"

            df.to_csv("questions.csv", index=False)

            print("Question marked as solved ")

        except ValueError as e:
            print(e)

    elif choice == "3":
        total = len(df)
        done = len(df[df["completed"] == "Yes"])

        print(f"Progress: {done}/{total}")

    elif choice == "4":
        break

    else:
        print("Please enter a valid choice!")